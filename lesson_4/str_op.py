






s = "У лукоморья 123 дуб зеленый 456"

#1) Определить, встречается ли в строке буква 'я'.
# Вывести на экран ее позицию (индекс) в строке.
def fun_one(s):
    return s.find('я')

# 2) Определить, сколько раз в строке встречается буква 'у'.
def fun_two(s):
    return s.count('у')

# 3) Определить, состоит ли строка из букв, ЕСЛИ нет, ТО вывести строку в верхнем регистре.
def fun_three(s):
    if not s.isalpha():
        return s.upper()

# 4) Определить длину строки. ЕСЛИ длина строки превышает 4 символа, ТО вывести строку в нижнем регистре.
def fun_four(s):
    # swapcase also works here
    if len(s) > 4:
        return s.lower()

# 5) Заменить в строке первый символ на 'О'. Результат вывести на экран
def fun_five(string, letter):
    lst = string.split()
    lst[0] = letter
    string = ' '.join(lst)
    return string
################

def fun(s):
    return f'''
        1) {fun_one(s)}
        2) {fun_two(s)}
        3) {fun_three(s)}
        4) {fun_four(s)}
        5) {fun_five(s, 'О')}
    '''

print(fun(s))

