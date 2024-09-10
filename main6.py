import machine
import utime

pot_led = machine.PWM(machine.Pin(16)) # Setup GP16 as the LED pin with a PWM output
pot_led.freq(6000) # Set the frequency of the PWM pin
pot = machine.ADC(26)

while True:
    potValue = pot.read_u16() # Reads the voltage that the potentiometer is adjusted to
    print("Potentiometer Value:", potValue)
    pot_led.duty_u16(potValue)
    utime.sleep(1)
