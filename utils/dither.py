#!/usr/bin/env python3
import argparse
import logging
import os
import pathlib

import numpy as np
from PIL import Image


def get_new_val(old_val, nc):
    """
    Get the "closest" colour to old_val in the range [0,1] per channel divided
    into nc values.
    """
    return np.round(old_val * (nc - 1)) / (nc - 1)


def fs_dither(img, nc):
    """
    Floyd-Steinberg dither the image img into a palette with nc colours per
    channel.
    """
    arr = np.array(img, dtype=float) / 255

    for ir in range(new_height):
        for ic in range(new_width):
            # NB need to copy here for RGB arrays otherwise err will be (0,0,0)!
            old_val = arr[ir, ic].copy()
            new_val = get_new_val(old_val, nc)
            arr[ir, ic] = new_val
            err = old_val - new_val
            # In this simple example, we will just ignore the border pixels.
            if ic < new_width - 1:
                arr[ir, ic + 1] += err * 7 / 16
            if ir < new_height - 1:
                if ic > 0:
                    arr[ir + 1, ic - 1] += err * 3 / 16
                arr[ir + 1, ic] += err * 5 / 16
                if ic < new_width - 1:
                    arr[ir + 1, ic + 1] += err / 16

    carr = np.array(arr / np.max(arr, axis=(0, 1)) * 255, dtype=np.uint8)
    return Image.fromarray(carr)


def palette_reduce(img, nc):
    """Simple palette reduction without dithering."""
    arr = np.array(img, dtype=float) / 255
    arr = get_new_val(arr, nc)

    carr = np.array(arr / np.max(arr) * 255, dtype=np.uint8)
    return Image.fromarray(carr)


parser = argparse.ArgumentParser(
    """
    This script recursively traverses folders and creates dithered versions of the images it finds.
    These are stored in the same folder as the images in a folder called "dithers".
    """
)

parser.add_argument('-d', '--directory', help="Set the directory to traverse", default=".")
parser.add_argument('-o', '--output', help="Set the output directory to save dithered images.", default=".")
parser.add_argument('-c', '--colorize', help="Colorizes the dithered images", action="store_true")
parser.add_argument('-nc', '--nearest', help="Set the number of channels to dedicate to the nearest colour", default=2, type=int)
parser.add_argument('-v', '--verbose', help="Print out more detailed information about what this script is doing", action="store_true")
args = parser.parse_args()

content_dir = pathlib.Path(args.directory)
exclude_dirs = set([args.output])
image_ext = [".jpg", ".JPG", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".bmp"]

if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

logging.info(f"Dithering all images in {content_dir} and sub-folders.")
logging.debug(f"Excluding directories: {', '.join(exclude_dirs)}")

images = sorted([path for path in filter(lambda path: path.suffix in image_ext, content_dir.rglob('*'))])

for image in images:
    img = Image.open(image)
    width, height = img.size

    if not args.colorize:
        img = img.convert('L')

    width, height = img.size
    new_width = 800
    new_height = int(height * new_width / width)
    img = img.resize((new_width, new_height), Image.LANCZOS)

    logging.info(f"🖼Dithering '{image.name}'")
    dim = fs_dither(img, args.nearest)

    logging.info(f"💾Saving dithered image at '{image.parent}/{args.output}/{image.name}'")
    try:
        dim.save(f"{image.parent}/{args.output}/{image.name}")
    except FileNotFoundError:
        os.mkdir(f"{image.parent}/{args.output}")
        dim.save(f"{image.parent}/{args.output}/{image.name}")
