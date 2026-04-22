---
layout: default
template: 0.4
type: faction
nav_exclude: false
has_children: true
has_toc: false

parent: Steppe of Lime Nomads (3)
title: Lime Clan
role: 
status: 

images: 
- ../../imgs/gallery/Pasted%20image%2020250822120449.png
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

A group of nomadic people from the [steppe](index.md).
They follow ceremonial raves and are respectful with their rituals.
They also consume a lot of vapours and powders to reach transcendence.
When they need to return to a sensible state, they consume lots of limes.