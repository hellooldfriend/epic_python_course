value = int(input("Enter the number:"))

def isEven(n):
    if n % 2 == 0:
        return f"The number {n} is EVEN"
    else:
        return f"The number {n} is ODD"

print(isEven(value))
