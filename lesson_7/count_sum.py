#Дано число, введенное с клавиатуры.
#Определить сумму квадратов нечетных цифр в числе.

val = input('Enter the number: ')

def f(n):
    summ = 0

    for i in n:
        if int(i) % 2 != 0:
            summ += int(i) ** 2

    if summ == 0:
        return 'The number does not have odd numbers'
    return summ


###
print(f(val))