from machine import Pin, Timer

led = Pin(15, Pin.OUT)
timer = Timer()


def blink(timer):
    led.toggle()


timer.init(freq=1, mode=Timer.PERIODIC, callback=blink)
