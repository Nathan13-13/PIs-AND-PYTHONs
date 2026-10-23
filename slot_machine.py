
import random
import time
import tm1637
from gpiozero import LED, Button

display = tm1637.TM1637(clk=23, dio=12)
display.brightness(7)
led = LED(21)

spin_button = Button(18, pull_up=True, bounce_time=0.1)

rigged_mode = False
last_press_time = 0
double_click_time = 1.0


def flash_led():
    end_time = time.monotonic() + 5

    while time.monotonic() < end_time:
        led.on()
        time.sleep(0.25)
        led.off()
        time.sleep(0.25)


def spin(rigged):
    if rigged:
        if random.random() < 0.5:
            number = random.randint(0, 9)
            numbers = [number, number, number, number]
        else:
            numbers = [random.randint(0, 9) for i in range(4)]

            while numbers[0] == numbers[1] == numbers[2] == numbers[3]:
                numbers = [random.randint(0, 9) for i in range(4)]
    else:
        numbers = [random.randint(0, 9) for i in range(4)]

    return numbers


def winner(numbers):
    return numbers[0] == numbers[1] == numbers[2] == numbers[3]


def button_pressed():
    global last_press_time, rigged_mode

    current_time = time.monotonic()

    if current_time - last_press_time < double_click_time:
        rigged_mode = True
        print("Hope Your Feeling Lucky!!!")
        last_press_time = 0
    else:
        last_press_time = current_time


spin_button.when_pressed = button_pressed

print("Welcome to the slot machine!")
print("Press the spin button to play.")

display.show("0000")

try:
    while True:
        spin_button.wait_for_press()
        spin_button.wait_for_release()

        time.sleep(double_click_time)

        if rigged_mode:
            print("!")
        else:
            print("Fair!")

        numbers = spin(rigged_mode)
        result = "".join(str(n) for n in numbers)

        display.show(result)
        print("You got:", result)

        if rigged_mode:
            print("Mode: Rigged")
        else:
            print("Mode: Fair")

        if winner(numbers):
            print("YOU WIN!")
            flash_led()
        else:
            print("You lost. Try again!")

        rigged_mode = False
        last_press_time = 0

except KeyboardInterrupt:
    print("Game stopped!")

finally:
    led.off()
    display.show("0000")
    led.close()
    spin_button.close()
