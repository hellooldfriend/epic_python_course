a = int(input("Enter city code:"))
b = int(input("Enter call's duration in minutes:"))

def mul(minutes, price):
    return int(minutes) * int(price)


def fun(code, minutes):
    if code == 343:
        return f"The total price is {mul(minutes, 15)}"
    elif code == 381:
        return f"The total price is:{minutes * 18}"
    elif code == 473:
        return f"The total price is: {minutes * 13}"
    elif code == 485:
        return f"The total price is: {minutes * 11}"
    else:
        return "We couldn't find your code, because we don't care"


print(fun(a, b))
