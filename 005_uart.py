"""
RS232 Example
Pins from Raspberry Pi Pico
Pin 3: GND
Pin 6: UART1 TX (GPIO4)
Pin 7: UART1 RX (GPIO5)

Important! On RS232 converter: Change the jumper to 5V

RS232 : Pico
GND ---- GND
RX  ---- TX
TX  ---- RX

Run Picocom to read RS232 data:
picocom /dev/ttyUSB0

You should see "Hello from Pico" at 1Hz rate
Send "t" to toggle the LED on Pico
"""

from machine import Pin, UART
import time

uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart.init(parity=None, stop=1)
led = Pin("LED", Pin.OUT)

while True:
    uart.write("Hello from Pico\r\n")
    if uart.any():
        data = uart.read()
        if data == b"t":
            uart.write("Toggle LED\r\n")
            led.toggle()
    time.sleep(1)
