"""
Press `t` to toggle the LED. Raspberry Pi Pico prints `LED toggled` from `/dev/ttyACM0` with baud rate 9600.

To read results from serial port (USB), run:
picocom -l /dev/ttyACM0
# `-l`: no(l)ocking

Source: https://electrocredible.com/raspberry-pi-pico-serial-uart-micropython/
"""

import select
import sys
import time
import machine

# Create an instance of a polling object
poll_obj = select.poll()
# Register sys.stdin (standard input) for monitoring read events with priority 1
poll_obj.register(sys.stdin, 1)
# Pin object for controlling onboard LED
led = machine.Pin("LED", machine.Pin.OUT)

while True:
    # Check if there is any data available on sys.stdin without blocking
    if poll_obj.poll(0):
        # Read one character from sys.stdin
        ch = sys.stdin.read(1)
        # Check if the character read is 't'
        if ch == "t":
            # Toggle the state of the LED
            led.value(not led.value())
            # Print a message indicating that the LED has been toggled
            print("LED toggled")
    # Small delay to avoid high CPU usage in the loop
    time.sleep(0.2)
