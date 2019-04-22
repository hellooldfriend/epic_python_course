#Напишите функцию, которая для целочисленного списка из 1000 случайных элементов определяет,
#сколько отрицательных элементов располагается между его максимальным и минимальным элементами
# включительно.


import random

numbers = [random.randint(-500, 500) for i in range(1, 1001)]

max_n = max(numbers)
min_n = min(numbers)

t = 0
x = list()

for n in numbers:
    if n < 0:
        x.append(n)
        t += 1


print(len(x), t)
