# StreamPad
The StreamPad is an open source hackpad made for macros (designed for streaming). It has 16 keys (4x4) and an OLED screen.

# PCB
Designed with KiCad.

# Case
Designed with fusion 360.

The macropad is assembled by pressing heat-set inserts into the back of the top plate. Then, 16mm screws are inserted through the bottom of the base and the PCB, threading directly into the inserts to hold everything together.

# Firmware
To be completed.

# Build
To make it, you will need:
1x XIAO RP2040
16x Cherry MX Switches
16x DSA Keycaps
4x M3x5x4 Heatset inserts
4x M3x16mm screws
16x 1N4148 DO-35 Diodes (included in PCB design)
1x 0.91" 128x32 OLED Display
1x 3D printed case
4x Cables (Female)
1x Hot glue gun
recommended wire strippers
HIGHLY RECOMMENDED to also get my PCB design. (I used JLCPCB for the making process)

You will need to solder wires from: 
XIAO:  OLED:

GND -> GND
3v3 -> VCC
D4 -> SDA
D5 -> SCL

You will then need to hot glue the OLED onto the top half of the case, and it is recommended to glue the PCB to the bottom half, but is not required.

---

This was my first time ever using KiCad for PCB design, and my first time properly shipping an open source project like this. I learned a lot about this sort of stuff with this project, and made many mistakes I will remember not to make again lol.
Thanks to the Hackclub (and Stardance) team for providing these amazing resources that helped make this dream of mine come true :3
