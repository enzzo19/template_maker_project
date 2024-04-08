; Example G-code file
; This is a comment - comments start with a semicolon

; Set units to millimeters
G21

; Set absolute positioning
G90

; Rapid move to starting position
G0 X0 Y0 Z10

; Linear move to cutting position
G1 X50 Y50 Z5 F1000

; Start cutting operation
M3 S500 ; Spindle on, speed 500 RPM

; Begin cutting path
G1 X60 Y60 Z-2 F500 ; Move in a straight line while cutting

; End cutting operation
M5 ; Spindle off

; Move back to starting position
G0 X0 Y0 Z10

; End of program
M30
