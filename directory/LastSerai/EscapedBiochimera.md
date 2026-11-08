---
layout: default
template: 0.4
type: creature
nav_exclude: false
has_children: true
has_toc: false

parent: The Last Serai (8)
title: Escaped Biochimera
role: Giant centipede-like creature
status: Burrowed underground, whereabouts unknown
footer_content: Image adapted from <a href="https://commons.wikimedia.org/wiki/File:The_Naturalist%27s_Miscellany_Vol.1_Centipede.jpg" target="_blank">Scolopendra morsitans (1789)</a> by Frederick Polydore Nodder, <em>The Naturalist's Miscellany</em>, Vol. 1 (photo via Biodiversity Heritage Library / Wikimedia Commons, Public Domain).

images: 
- ../../imgs/gallery/escaped_biochimera_ultraviolet_resonance.jpg

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

Something like a colossal centipede climbed out of a window of the [Ignored Tower](IgnoredTower.md), descended the outside slowly and [burrowed into the ground](../../campaigns/UVG24XX/ep_012.md).

The event became known as the Escaped Biochimera.
Everyone in the Last Serai is used to ignoring the tower, so they ignored this too.
Where it went underground, and what it was, is not known.

It burrows.
It waits.
