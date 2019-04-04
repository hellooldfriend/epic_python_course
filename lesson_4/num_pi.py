import math

number = int(input("Enter the number:"))

def fun(number):
    pi = math.pi
    return f"{round(pi, number)}"

print(fun(number))
