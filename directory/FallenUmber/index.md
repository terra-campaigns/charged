---
layout: default
template: 0.4
type: location
nav_exclude: false
has_children: true
has_toc: false

parent: Directory
title: Fallen Umber (12)
nav_order: 1012
role: 
status: 

hooks: Cosmic scales have been traded here.

images: 

---

{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---
[index](../../campaigns/UVG24XX/index.md)
{% endcomment %}
