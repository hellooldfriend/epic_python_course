#Дано число, введенное с клавиатуры. Определить сумму квадратов нечетных цифр в числе.
total = 0
value = int(input('Enter the number: '))
for i in range(1, value + 1):
    if i % 2 != 0:
        total += i ** 2

print(total)