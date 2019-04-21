from random import randint
value = randint(1, 9)
count = 3

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
        else:
            print('Game over')




