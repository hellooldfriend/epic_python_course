#Напишите функцию, которая для целочисленного списка из 1000 случайных элементов определяет,
#сколько отрицательных элементов располагается между его максимальным и минимальным элементами
# включительно.


import random
numbers = [random.randint(-500, 500) for i in range(1001)]

def f(lst):
    count = 0
    for n in lst:
        if n < 0:
            count += 1
    return count


min_values_count = f(numbers)

print(min_values_count)


