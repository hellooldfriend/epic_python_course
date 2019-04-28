#Дан список из 20 элементов.
#Найти пять соседних элементов, сумма значений которых максимальна.


def max_sequence(seq):
    """
    Функция ищет пять соседних элементов списка, сумма значений которых максимальна.
    >>> max_sequence([1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4])
    [4, 4, 4, 3, 4]
    >>> max_sequence([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5])
    [7, 2, 9, 2, 9]
    """
    max_seq = sum(seq[0:5])
    index = 0

    for i in range(1, len(seq), 1):
        x = seq[i:i + 5]
        s = sum(x)

        if len(x) < 5:
            break
        if s > max_seq:
            max_seq = s
            index = i

    return seq[index:index + 5]



if __name__ == '__main__':
    import doctest
    doctest.testmod()


# print(max_sequence([1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4]))
# print(max_sequence([-100, -100, -100, -100, -100, -1, -1, -1, 2, 0]))