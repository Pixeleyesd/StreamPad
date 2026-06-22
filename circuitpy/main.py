import board
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# oled
displayio.release_displays()
i2c = busio.I2C(board.D5, board.D4)  # scl, sda
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# splash screen
splash = displayio.Group()

title = label.Label(
    terminalio.FONT,
    text="StreamPad",
    color=0xFFFFFF,
    scale=2,        # big but wont clip (9 chars * 6px * 2 = 108px wide, fits in 128)
    x=10,
    y=22,
)

sub = label.Label(
    terminalio.FONT,
    text="Sub 2 Pixeleyesd",
    color=0xFFFFFF,
    scale=1,        # 17 chars * 6px = 102px wide, fits fine
    x=13,
    y=48,
)

splash.append(title)
splash.append(sub)
display.show(splash)

# keyboard
keyboard = KMKKeyboard()

keyboard.col_pins = (board.D10, board.D9, board.D8, board.D7)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# f13-f24 for rows 1-3, numpad 1-4 for row 4
keyboard.keymap = [
    [
        KC.F13, KC.F14, KC.F15, KC.F16,  # row 1
        KC.F17, KC.F18, KC.F19, KC.F20,  # row 2
        KC.F21, KC.F22, KC.F23, KC.F24,  # row 3
        KC.P1,  KC.P2,  KC.P3,  KC.P4,   # row 4
    ]
]

if __name__ == "__main__":
    keyboard.go()