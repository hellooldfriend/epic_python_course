#Напишите функцию, которая для целочисленного списка из 1000 случайных элементов определяет,
#сколько отрицательных элементов располагается между его максимальным и минимальным элементами
# включительно.


import random
numbers = [random.randint(-500, 500) for i in range(1001)]

def f(lst):
    '''
    >>> f([-1, 25, -100, 4, 7, -2, -9, -25, 200, -7, 30])
    4
    >>> f([100, -1, -2, -200, -4, -2, 2, 4, 1000, -4, 3])
    3
    '''
    max_index = lst.index(max(lst))
    min_index = lst.index(min(lst))


    lst = lst[min_index:max_index]
    count = 0

    for x in lst:
        if x < 0:
            count +=1
    return count



if __name__ == '__main__':
    print(f(numbers))

