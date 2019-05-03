# Напишите программу-игру.
# Компьютер загадывает случайное число, пользователь пытается его угадать.
# Пользователь вводит число несколько раз (количество попыток ограничено и указывается в программе),
# пока не угадает или не введёт слово Выход.
# Компьютер сравнивает число с введенным и сообщает пользователю больше оно или меньше загаданного.

from random import randint
value = randint(1, 9)
count = 3

print(value, count)
while count > 0:
    val = input('Enter the number or type stop: ')

    if val.lower() == 'stop':
        print('End')
        count = 0
    else:
        n = int(val)
        count -= 1

        if count != 0:
            if n == value:
                print('Correct. End.')
                count = 0
            elif n > value:
                print(f'Your number is bigger, you have {count} attempts.')

            elif n < value:
                print(f'Your number is smaller, you have {count} attempts.')

        elif count == 0:
            if n == value:
                print('Correct. End.')
            else:
                print('0 attempts. Game over')




