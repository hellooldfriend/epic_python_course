#Напишите программу,
#выполняющую функции простейшего калькулятора.
#Программа получает два числа, а затем запрашивает оператор.
#Обеспечьте корректную обработку ввода, который не преобразуется в числа.
#Обработайте ошибки деления на ноль.

a = int(input('Enter first number: '))
b = int(input('Enter seconds number: '))
operator = input('Enter the operator: ')



def f(a, b, operator):
    lst = ['+', '-', '/', '*']

    if operator in lst:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '/':
            if b != 0:
                return a / b
            else:
                return 'You can not divide by zero'
        elif operator == '*':
            return a * b
    else:
        return "I'm to stupid to make this kind of calculation."



print(f(a, b, operator))
