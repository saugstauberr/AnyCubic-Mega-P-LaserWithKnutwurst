G28 X       ; Home X
G28 Y       ; Home Y
G28 Z       ; Home Z
G21         ; Set units to mm
G90         ; Absolute positioning
G0 Z5       ; Lift Laser so X and Y movements are possibale
G0 X10 Y80  ; go to new 0 0 5
G0 Z0       ; go to new 0 0 0
G92         ; set new 0 0 0
G0 Z50      ; lift laser to optimal hight