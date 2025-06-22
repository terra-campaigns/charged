```
dsix = {1-6}
dfour = {1-4}
dtwenty = {1-20}

chargedrpg_eb = {import:chargedrpg-eb}
chargedrpg_uvg = {import:chargedrpg-uvg}
chargedrpg_metamorphica = {import:chargedrpg-metamorphica}

background
  EB ^9
    bgname = [chargedrpg_eb.bgname]
    blurb = [chargedrpg_eb.blurb]
    bond = [chargedrpg_eb.debt]
    name = [chargedrpg_eb.name]
    event1 = [chargedrpg_eb.event1]
    event2 = [chargedrpg_eb.event2]
    equip = € 1000 (with interests), [chargedrpg_eb.equip]
  UVG ^2
    bgname = [chargedrpg_uvg.bgname]
    blurb = [chargedrpg_uvg.blurb]
    bond = [chargedrpg_uvg.bond]
    name = [chargedrpg_uvg.name]
    event1 = [chargedrpg_uvg.event1]
    event2 = [chargedrpg_uvg.event2]
    equip = [chargedrpg_uvg.equip]

physique
  athletic
  brawny
  flabby
  lanky
  rugged
  scrawny
  short
  statuesque
  stout
  towering

skin
  birthmarked
  marked
  oily
  rosy
  scarred
  soft
  tanned
  tattooed
  weathered
  webbed

hair
  no
  braided
  curly
  filthy
  frizzy
  long
  luxurious
  oily
  wavy
  wispy

face
  bony
  broken
  chiseled
  elongated
  pale
  perfect
  rakish
  sharp
  square
  sunken

speech
  blunt
  booming
  cryptic
  droning
  formal
  gravelly
  precise
  squeaky
  stuttering
  whispery

clothing
  antique clothing
  bloody clothing
  elegant clothing
  filthy clothing
  foreign clothing
  frayed clothing
  frumpy clothing
  livery
  rancid clothing
  soiled clothing

virtue
  ambitious
  cautious
  courageous
  disciplined
  gregareous
  honorable
  humble
  merciful
  serene
  tolerant

vice
  aggressive
  bitter
  craven
  deceitful
  greedy
  lazy
  nervous
  rude
  vain
  vengeful

mutation
  <b>You have no mutations</b> ^80
  [chargedrpg_metamorphica] <br><br> <i>Your mutation takes 1 of your inventory slots.</i> ^15
  [chargedrpg_metamorphica] <br><br> [chargedrpg_metamorphica] <br><br> <i>Your mutations take 2 of your inventory slots.</i> ^05
  
```