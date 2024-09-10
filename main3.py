# Turn the board led on, when pressing the button
import machine

switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin('LED', machine.Pin.OUT)

while True:
    if switch.value():
        led.value(True)
    else:
        led.value(False)