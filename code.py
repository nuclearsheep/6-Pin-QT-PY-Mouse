import time
import board
from adafruit_hid.mouse import Mouse
import usb_hid
from usb_hid import devices
from digitalio import DigitalInOut, Direction, Pull
time.sleep(1)
mouse = Mouse(devices)
A = DigitalInOut(board.D3)
B = DigitalInOut(board.D4)
C = DigitalInOut(board.D5)
D = DigitalInOut(board.D6)
ONE = DigitalInOut(board.D7)
TWO = DigitalInOut(board.D0)
THREE = DigitalInOut(board.D1)
FOUR = DigitalInOut(board.D2)
row_pins = [A,B,C,D]
col_pins = [ONE,TWO,THREE,FOUR]
rows = []
cols = []
j=0
for i in row_pins:
    rows.append(j)
    j += 1
j=0
for i in col_pins:
    cols.append(j)
    j += 1
j=0
print(rows, " ", cols)

def lookup(coordinates):
    if coordinates[0] == 0:
        if coordinates[1] == 0:
            pass  # Morse
        elif coordinates[1] == 1:
            pass
        elif coordinates[1] == 2:
            pass
        else:
            pass
    elif coordinates[0] == 1:
        if coordinates[1] == 0:
            pass
        elif coordinates[1] == 1:
            mouse.click(1)  # L.click, broken. Acts like r.click?
        elif coordinates[1] == 2:
            mouse.move(-3, 0, 0)  # Left
        else:
            mouse.move( 0, 0, 3)
    if coordinates[0] == 2:
        if coordinates[1] == 0:
            pass
        elif coordinates[1] == 1:
            mouse.move( 0,-1, 0)  # Up
        elif coordinates[1] == 2:
            mouse.click(Mouse.MIDDLE_BUTTON)
        else:
            mouse.move( 0, 1, 0)  # Down
    else:
        if coordinates[1] == 0:
            pass
        elif coordinates[1] == 1:
            mouse.click(Mouse.RIGHT_BUTTON)
        elif coordinates[1] == 2:
            mouse.move( 1, 0, 0)  # Right
        else:
            mouse.move( 0, 0,-1)

while True:
    # set all pins pins to be inputs w/pullups
    for i in row_pins:
        i.direction = Direction.INPUT
        i.pull = Pull.UP
    for i in col_pins:
        i.direction = Direction.INPUT
        i.pull = Pull.UP

    # set one row low at a time
    for row in rows:
        row_pins[row].direction = Direction.OUTPUT
        row_pins[row].value = False
        # time.sleep(0.1)
        # check the column pins, which ones are pulled down
        for col in cols:
            if not col_pins[col].value:
                coords = (row, col)
                print(coords)
                lookup(coords)
            else:
                pass
            # time.sleep(0.1)
        # reset the pin to be an input
        row_pins[row].direction = Direction.INPUT
        row_pins[row].pull = Pull.UP
        # time.sleep(0.1)


