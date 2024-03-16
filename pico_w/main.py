#machine.freq()  # get the current frequency of the CPU

import machine
import time
from machine import Pin
#led_pin = machine.Pin(25, machine.Pin.OUT) 
led25 = Pin("LED", Pin.OUT)
while True:
    print(machine.freq(),"MHz")
    led25.value(1)
    #led_pin.value(1)
    time.sleep_ms(100)
    led25.value(0)
    #led_pin.value(0)
    time.sleep_ms(100)