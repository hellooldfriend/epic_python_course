import math

value = float(input("Enter the number: "))

def fun(value):
    if 0.2 < value < 0.9:
        return math.sin(value)
    else:
        return 1


print(fun(value))
