#Найти сумму чисел, вводимых с клавиатуры.
#Количество вводимых чисел заранее неизвестно.
#Окончание ввода - слово “Стоп”.
#При ошибке ввода попросить повторить ввод числа.


def f(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

total = 0

while True:
    value = input('Enter here: ')

    if value.lower() == 'stop':
        print(f'total: {total}')
        break
    elif f(value):
        total += int(value)
    else:
        print('Error')




