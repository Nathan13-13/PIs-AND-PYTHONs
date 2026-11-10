from gpiozero import LED
from time import sleep

led_pins = [4, 17, 27, 22, 5, 6, 13, 19]
leds = [LED(pin) for pin in led_pins]

def to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return to_binary(n // 2) + str(n % 2)

number = int(input("Enter a number between 0 and 255: "))

if number < 0 or number > 255:
    print("Please enter a number between 0 and 255.")

else:
    binary = to_binary(number)
    binary = binary.zfill(8)

    print("Binary:", binary)

    for i in range(8):
        if binary[i] == "1":
            leds[i].on()
        else:
            leds[i].off()

    sleep(10)

    for led in leds:
        led.off()
