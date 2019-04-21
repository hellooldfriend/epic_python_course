#Дано число, введенное с клавиатуры.
#Определить сумму квадратов нечетных цифр в числе.

val = int(input('Enter the number: '))
total = 0

for i in range(val + 1):
    if i % 2 != 0:
        n = i ** 2
        total += n

print(total)
