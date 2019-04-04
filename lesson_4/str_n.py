s = input("Write something: ")
n = int(input("Enter the number: "))

def fun(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s

print(fun(s, n))
