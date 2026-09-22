temp_input = input("Enter the high temperature for the day in Fahrenheit: ")
temp = float(temp_input)

if temp < 0 or temp > 140:
    print("invalid input")
elif temp < 60:
    print("you need to bring a sweater")
else:
    print("you do not need to bring a sweater")