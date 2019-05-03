# temper.txt

#В файле 10/ temper.stat представлена ежемесячная максимальная температура в градусах
#по Фаренгейту одного из аэропортов мира в период с 1948 по 2016.

#Необходимо определить максимальные и минимальные значения, среднюю температуру.
#Определить, сколько уникальных температур содержится в файле.

def read_file(file):
    lst = list()
    try:
        with open(file, 'r') as file:
            for line in file:
                lst.append(line.strip())


        return lst

    except Exception as e:
        return e

############################################
lst = read_file('temper.txt')

min = min(lst)
max = max(lst)

sum = 0
average = 0
dic = dict()
numbers = list()
for i in lst:
    i = float(i)

    sum += i
    average = round(sum / len(lst), 1)
    n = 1
    dic.setdefault(i, 0)
    dic[i] += 1

my_set = set(lst)
new_list = list(my_set)
len_of_uniq = len(new_list)

############################################
print(f'min: {min}, max: {max}, average: {average}, amount of uniq: {len_of_uniq}')
