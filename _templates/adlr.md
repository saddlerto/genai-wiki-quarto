<%*
let title;
if (!tp.file.title.startsWith("Untitled")){
	title = tp.file.title
} else {
	title = await tp.system.prompt("ADLR Title:")
}
let fileTitle = title;
fileTitle = fileTitle.replace(/ /g, "-").toLowerCase();
fileTitle = fileTitle.replace(/[&'’‘’:,–.;?()“”$]/g, "").toLowerCase();
fileTitle = fileTitle.replace(/--/g, "-").toLowerCase();
fileTitle = fileTitle.replace(/-—-/g, "-").toLowerCase();
await tp.file.rename(`${fileTitle}`);
-%>
---
title: "<% title %>"
alias:
- "<% title %>"
created: <% tp.file.creation_date("YYYY-MM-DDTHH:mm:ssZ") %>
modified: <% tp.file.creation_date("YYYY-MM-DDTHH:mm:ssZ") %>
tags:
- adlr
---

## Abstract


## Driving Event


## Lesson(s) Learned


## Recommendations


## Evidence of Recurrence Control Effectiveness

