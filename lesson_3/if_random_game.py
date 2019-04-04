import random

def fun():
    value = random.randint(1, 4)
    user_value = int(input("Enter the number: "))


    if value == user_value:
        return "You win"
    else:
        if value > user_value:
            return "You lost, try again. You number was smaller"
        else:
            return "You lost, try again. You number was bigger"

print(fun())
