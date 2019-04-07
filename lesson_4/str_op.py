
s = "У лукоморья 123 дуб зеленый 456"

def fun_one(s):
    return s.find('я')

def fun_two(s):
    return s.count('у')

def fun_three(s):
    # swapcase also works here
    if s.islower():
        return s.upper()

def fun_four(s):
    # swapcase also works here
    if len(s) > 4:
        return s.lower()

def fun_five(s):
    return s.replace( s[0], 'О')
################

def fun(s):
    return f'''
        1) {fun_one(s)}
        2) {fun_two(s)}
        3) {fun_three(s)}
        4) {fun_four(s)}
        5) {fun_five(s)}
    '''

print(fun(s))

