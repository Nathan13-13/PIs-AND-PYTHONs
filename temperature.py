
import time
from gpiozero import LED

RED_PIN = 16
BLUE_PIN = 12

red_led = LED(RED_PIN)
blue_led = LED(BLUE_PIN)
import time
import board
import digitalio
import adafruit_dht
from datetime import datetime

sensor = adafruit_dht.DHT11(board.D25)

red_led = digitalio.DigitalInOut(board.D16)
red_led.direction = digitalio.Direction.OUTPUT
blue_led = digitalio.DigitalInOut(board.D12)
blue_led.direction = digitalio.Direction.OUTPUT

def to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

with open("temperature.csv", "w") as file:
    file.write("time,temperature\n")

while True:
    try:
        celsius = sensor.temperature
        fahrenheit = to_fahrenheit(celsius)
        current_time = datetime.now()
        time_str = current_time.strftime('%H:%M:%S')

        output_line = f"{time_str},{fahrenheit:0.1f}\n"

        with open("temperature.csv", "a") as file:
            file.write(output_line)

        if fahrenheit > 72:
            red_led.value = True
            blue_led.value = False
        elif fahrenheit < 72:
            red_led.value = False
            blue_led.value = True
        else:
            red_led.value = False
            blue_led.value = False
