---
layout: default
template: 0.4
type: location
nav_exclude: false
has_children: true
has_toc: false

parent: Directory
title: The Last Serai (8)
nav_order: 1008
role: 
status: 

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
