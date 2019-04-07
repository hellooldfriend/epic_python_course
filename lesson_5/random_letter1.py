import random

arr = ['самовар', 'весна', 'лето']

def fun(arr):
    item = random.choice(arr)
    letter = random.choice(item)

    new_item = list(item)
    new_item[item.index(letter)] = '?'
    new_item = "".join(new_item)

    user_value = input("Enter the letter: ")
    nl = '\n'

    if letter == user_value:
        return f'Win! {nl}Word: {item}'
    else:
        return f'You lost! {nl}Word: {item}'


print(fun(arr))
