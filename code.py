import board
import time
from adafruit_hid.mouse import Mouse
import usb_hid
from usb_hid import devices
import digitalio
time.sleep(1)

mouse = Mouse(devices)

A = digitalio.DigitalInOut(board.A2)  
A.direction = digitalio.Direction.OUTPUT

B = digitalio.DigitalInOut(board.A3)
B.direction = digitalio.Direction.OUTPUT

C = digitalio.DigitalInOut(board.SDA)
C.direction = digitalio.Direction.OUTPUT

ONE = digitalio.DigitalInOut(board.SCL)
ONE.direction = digitalio.Direction.INPUT
ONE.pull = digitalio.Pull.DOWN

TWO = digitalio.DigitalInOut(board.TX)
TWO.direction = digitalio.Direction.INPUT
TWO.pull = digitalio.Pull.DOWN

THREE = digitalio.DigitalInOut(board.RX)
THREE.direction = digitalio.Direction.INPUT
THREE.pull = digitalio.Pull.DOWN

  # A B C outputs, cycle through, ONE TWO THREE Inputs, read any.

while True:
    
    A.value = True
    B.value = False
    C.value = False
    if ONE.value:
        mouse.move( 1, 0, 0)
    elif TWO.value:
        mouse.move(-1, 0, 0)
    elif THREE.value:
        mouse.click(Mouse.LEFT_BUTTON)
    else: 
        pass
        
    A.value = False
    B.value = True
    C.value = False
    if ONE.value:
        mouse.move( 0,-1, 0)
    elif TWO.value:
        mouse.move( 0, 1, 0)
    elif THREE.value:
        mouse.click(Mouse.RIGHT_BUTTON)
    else: 
        pass
    
    A.value = False
    B.value = False
    C.value = True
    if ONE.value:
        mouse.move( 0, 0, 1)
    elif TWO.value:
        mouse.move( 0, 0,-1)
    elif THREE.value:
        mouse.click(Mouse.MIDDLE_BUTTON)
    else: 
        pass

