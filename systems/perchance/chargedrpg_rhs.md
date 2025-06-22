```
<button onclick="update()">randomize</button>

<p align="left" >
  <b>[b = background.selectOne, b.name]</b>
  <br><br>
  
  <b>[b.bgname]:</b> [b.blurb]
  <br><br>
  
  You are [physique] with [skin] skin and [hair] hair.
  You have a [face] face and your speech is [speech].
  You are dressed in [clothing]. You are [virtue] but also [vice].
  You are [age=dtwenty.selectOne+dtwenty.selectOne+dtwenty.selectOne+10] years old.
  <br><br>

  [mutation]
  <br><br>
  
  <b>Attributes:
    STR [att1=[dsix.selectOne+dsix.selectOne+dsix.selectOne]]
    DEX [att2=[dsix.selectOne+dsix.selectOne+dsix.selectOne]]
    WIL [att3=[dsix.selectOne+dsix.selectOne+dsix.selectOne]]</b>
  <br>You can swap two of these.
  <br><br>
  
  <b>Hit Protection (HP): [hp=dsix.selectOne]</b>
  <br><br>
  
  <b>Starting Equipment</b><br>
  [b.equip]
  <br><br>
  
  [e1=b.event1]
  <br><br>
  [e2=b.event2]
  <br><br>

  [b.bond]
</p>

<!-- The line below makes it so if your device is in dark mode, then the default text color is switched to white, and the default background color is switch to black. -->
<style> html { color-scheme: light; font-family:Monospace; font-size:100%; color:#fc0fc0; } </style>

```