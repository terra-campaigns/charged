---
layout: default
template: 0.4
type: creature
nav_exclude: false
has_children: true
has_toc: false

parent: 2 The Low Road and The High
title: Shaggy
role: Man-Eating Molluscs
status: 

hooks: 

images: 
- ../../imgs/gallery/Pasted%20image%2020250718085258.png
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
