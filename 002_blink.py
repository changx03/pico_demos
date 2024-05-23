from machine import Pin, Timer

led = Pin(25, Pin.OUT)
timer = Timer()


def blink(timer):
    led.toggle()


# frequency at 1Hz
timer.init(freq=1, mode=Timer.PERIODIC, callback=blink)
