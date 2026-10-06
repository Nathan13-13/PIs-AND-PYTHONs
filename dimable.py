from gpiozero import PWMLED, RotaryEncoder
from time import sleep
led = PWMLED(17)
rotor = RotaryEncoder(23, 18, wrap=True, max_steps=180)
def update_brightness(n):
        linear_val = n / 180.0
        led.value = linear_val ** 2
        print(rotor.steps)
        sleep(0.1)
while True:
        rotor.when_rotated = update_brightness(rotor.steps)
