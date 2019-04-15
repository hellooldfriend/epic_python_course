
from random import randint
value = randint(1, 9)

while True:
    user_value = input("Enter the number: ")
    if user_value.lower() == 'exit':
        print('End')
        break
    else:
        val = int(user_value)
        if val == value:
            print('Correct. End.')
        elif val > value:
            print('Your number is bigger. Try again.')
        elif val < value:
            print('Your number is smaller. Try again.')

