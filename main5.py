# Turn on the external led when pressing the button
import machine

switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)

while True:
    if switch.value():
        led.value(True)
    else:
        led.value(False)