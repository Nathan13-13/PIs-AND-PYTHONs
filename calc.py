nate_input = input("Input: ")
x, y, z = nate_input.split(" ")
x = float(x)
z = float(z)
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    if z == 0:
        result = "no zeros"
    else:
        result = x / z
print(result)  