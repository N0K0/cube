import pprint

# Fetched from https://ruwix.com/the-rubiks-cube/rubiks-cube-patterns-algorithms/more-rubiks-patterns/
PATTERNS = {
    "2-small-cubes-in-scrambled": "U U Li U U Li U U F F D L Fi L F R R Di B B Di L L Di L L F F R R",
    "3t": "B U U L L F F R R F D D F F R R Fi R R U U",
    "4-crosses": "F F B B R F F B B R F F B B R F F B B R F F B B R F F B B R",
    "4-plus-2-dots": "F U U D D R L Ui D F B R U U R R U U F F L L U U F F L L B B",
    "4t-around": "F F D D Fi L L D D U U R R Bi U U F F",
    "6ts": "F F R R U U Fi B D D L L F B",
    "antipodal-chaos": "U U L L U U L L U U F F R R F F U U F F",
    "c-spirals-3d": "Bi Fi L L D D Bi F U U R R F F",
    "crossing-snake": "R L U U R Li U U F F R R D D B B D D B B L L D D R R",
    "doubler": "R L U U R Li D D R R F F U U F F U U L L F F U U L L",
    "edge-hexagon-of-order-2": "U B B Ui Fi Ui D Li D D L U Di F Di L L B B Di",
    "edge-hexagon-of-order-3": "D Li U Ri Bi R B U U D B Di Bi L U Di",
    "elegant-cube-in-cube": "U U F F D D B B R R U U B B R R U U R R",
    "exchanged-chicken-feet": "F Li Di Bi L F U Fi Di F L L Bi Ri U L L Di F",
    "exchanged-duck-feet": "U F R R Fi Di R U B B U U Fi R R F D B B R Bi",
    "exchanged-peaks": "F U U L F Li B L U Bi Ri Li U Ri Di Fi B R R",
    "exchanged-rings": "Bi Ui Bi Li D B U D D B U L Di Li Ui L L D",
    "facing-checkerboards": "U U F F U U F F B B U U F F D D",
    "flower-field-power": "M S Mi Si R R L L U U D D F F B B",
    "four-twisted-peaks": "Ui D B Ri F R Bi Li Fi B L F Ri Bi R Fi Ui D",
    "glider-conways-life": "D D R R F F R R U U B B D D F F L L U U R R U U",
    "glitch-corners": "Fi Li Bi Ri Ui R B L F U",
    "headlights": "U U F F U U D D B B D D",
    "henrys-snake": "R R F F Ui Di B B L L F F L L U D R R F F",
    "henrys-zigzag-with-checkerboard": "R R L L F F B B U F F B B U U F F B B U",
    "hi-ohio-peace": "U U F F L L R R F F U U",
    "loose-strap": "F F U U B B U U F F U U",
    "matching-pictures": "Ri D D R L D D Li",
    "megatron": "U L D Ri F D D R R F F Ri F D D B L L U U Di R R U R R B B L L",
    "mirror": "U D F F B B Ui Di R R L L B B",
    "opposite-pillars-mem": "R R F F L L R R F F L L",
    "percent-sign": "R L U U R Li U U F F L L U U F F U U F F R R U U R R",
    "picnic": "D D R R L L F F B B",
    "plus-minus-check": "U D R R L L U D R R L L",
    "plus-with-dot": "R L F F U U Ri Li F F U U R R F F U R R L L F F B B Di",
    "rockets": "U R R F F R R Ui D F F R R F F D",
    "rons-cube-in-a-cube": "F Di Fi R D Fi Ri D R D Li F L D Ri F Di",
    "six-two-one": "U B B D D L Bi Li Ui Li B D D B B",
    "slash": "R L F B R L F B R L F B",
    "snake-eyes": "R R U U R R U U R R U U",
    "staircase-steps": "L L F F Di L L B B Di Ui R R B B Ui Li B B L D L Bi D Li U",
    "stripe-dot-solved": "D U B B F F Di Ui",
    "the-pillars": "L L R R B B F F",
    "tiny-worms-perpendicular": "Ui F F L L U D D F F B B U F F L L D",
    "toms-stripes": "L U F F R Li U U Bi U D B B L F Bi Ri L Fi R",
    "twinpeaks": "U L L B B R R U R R Di U L Fi U Li D Bi U L Bi L Ri Ui",
    "twisted-chicken-feet": "F Li D Fi Ui B U F Ui F Ri F F L Ui Ri D D",
    "twisted-corners": "F U D R R F F Ui B U B U R R Bi U L L U B B U U F F L L Ui",
    "twisted-duck-feet": "F Ri B R U Fi Li Fi U U Li Ui D D B Di F Bi U U",
    "twisted-rings": "F D Fi D D Li Bi U L D R U Li Fi U L U U",
    "two-twisted-peaks": "F Bi U F U F U L B L L Bi U Fi L U Li B",
    "viaduct-u": "R R U U L L D B B L L B B R R Di U Li D Fi Ui R R Fi U B B U U Ri",
    "weirdo": "Ri Fi U F F Ui F Ri F F D D F F D D F F D F F R R U U",
    "wrapped2x2cube": "Di B B F F L L Ui F F R R D F F U U Li B Ri Ui Li F Di F L D D",
    "yan-ying": "L R F B Ui Di Li Ri",
    "yin-yang": "R L B F R L Ui Di Fi Bi U D",
    "zz-line": "R L U U R Li U U F F R R U U F F D D B B L L U U L L",
}
