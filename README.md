<h1 align="center">GenAI Wiki</h1>

<div align="center">
  <strong>A wiki built on <a href="https://quarto.org">Quarto.</a></strong>
</div>

<div align="center">
  <h3>
    <a href="https://saddlerto.github.io/genai-wiki-quarto">
      Website
    </a>
    <span> | </span>
    <a href="https://quarto.org/docs/guide/">
      Quarto Handbook
    </a>
  </h3>
</div>

<div align="center">
  <!-- <img src="" width="500"><br> -->
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a><br>
  <sub> Built with Obsidian and Quarto. Template by
  <a href="https://github.com/errbufferoverfl/garden.errbufferoverfl.me">errbufferoverfl</a>
</div>

## Introduction

This is a wiki about generative AI.

## Table of Contents

- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [DNS Configuration](#dns-configuration)
- [Common Issues](#common-issues)
  - [Error: Not Found](#error-not-found)
- [License](#license)
- [Contact](#contact)

## Tech Stack

Here's a brief high-level overview of the tech stack this site uses:

- [Quarto](https://quarto.org/docs/guide/) for theming, and static website generation.
- Content is managed using [Obsidian](https://obsidian.md/).
- Deployed to Github Pages.

## Getting Started

The website configuration can be found in the `_quarto.yml`, and `_quarto.yml.local`/. This provides website options as well as defaults for HTML documents created within the site.

To preview the website you can run:

```shell
quarto preview
```

To render, but not preview a website you can run:

```shell
quarto render 
```

## DNS Configuration

For more information on how to configure a custom domain for your own deployment, checkout the GitHub guide to ["Configuring a custom domain for your GitHub Pages site"](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).

```text
CNAME <subdomain> <username>.github.io
```

## Common Issues

### Error: Not Found

The following error often occurs when you're trying to preview or render the Quarto site while Obsidian is open. Likely due to a plugin that is installed or something about file resolution.

```shell
ERROR: NotFound: No such file or directory (os error 2), rename '/Users/.../.../garden.errbufferoverfl.me/CODE_OF_CONDUCT.html' -> '/Users/.../.../garden.errbufferoverfl.me/_site/CODE_OF_CONDUCT.html'

NotFound: No such file or directory (os error 2), rename '/Users/.../.../garden.errbufferoverfl.me/CODE_OF_CONDUCT.html' -> '/Users/.../.../garden.errbufferoverfl.me/_site/CODE_OF_CONDUCT.html'
    at Object.renameSync (deno:runtime/js/30_fs.js:175:9)
    at renderProject (file:///Users/.../Applications/quarto/bin/quarto.js:86832:22)
    at async Command.fn (file:///Users/.../Applications/quarto/bin/quarto.js:90856:32)
    at async Command.execute (file:///Users/.../Applications/quarto/bin/quarto.js:8437:13)
    at async quarto (file:///Users/.../Applications/quarto/bin/quarto.js:127545:5)
    at async file:///Users/.../Applications/quarto/bin/quarto.js:127563:9
```

To resolve this issue:

- Close Obsidian
- Delete the `_site`
- Rerun the command.

<!-- LICENSE -->

## License

Quarto >v1.4 is distributed under [MIT](https://quarto.org/license.html) license.

The Quarto/Obsidian conversion scripts on GenAI Wiki are licensed under [Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en) (CC BY-SA 4.0), unless otherwise specified.

<!-- CONTACT -->

## Contact

For issues relating to this repository and content hosted on [the GenAI Wiki](https://saddlerto.github.io/genai-wiki-quarto) please raise a [GitHub issue](https://github.com/saddlerto/genai-wiki-quarto) and use the provided templates to ensure your issue is promptly addressed.
