#Найдите сумму всех значений функции y(x) = x2 + 3 на интервале от 10 до 30 с шагом 2.

total = 0
def y(x):
    return x ** 2 + 3

for i in range(10, 31, 2):
    if 10 < i < 30:
        total += y(3)

print("Total:", total)


