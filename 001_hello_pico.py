from machine import Pin
import time

led = Pin(25, Pin.OUT)

for i in range(0, 10):
    led.value(1)
    time.sleep(2)
    led.value(0)
    time.sleep(1)
    print("Hello world")
