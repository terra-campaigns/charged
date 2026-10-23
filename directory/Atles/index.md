---
layout: default
template: 0.4
type: faction
nav_exclude: false
has_children: true
has_toc: false

parent: Directory
title: Atles' Catlord Caravan
role: 
status: 

images: 
- ../../imgs/gallery/Pasted%20image%2020250512113900.png

---

{% include header_directories.md %}

## Caravan Ledger & Inventory

The live expedition supplies, vehicles, sacks, personnel, and debt contracts for the caravan are tracked in the [UVG Atles Caravan Ledger](https://docs.google.com/spreadsheets/d/1TEx8ZmBq90Tyms3u5eVlM2OqpUIemsj6c04rmNXxg94/edit).

{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---
[index](../../campaigns/UVG24XX/index.md)
{% endcomment %}