#Напишите функцию для чтения CSV-файлов.

#В качестве входного аргумента функция принимает имя файла в формате CSV.
#Функция должна возвращать список словарей,
#интерпретируя первую строку файла как имена ключей,
#а каждую последующую строку как значения этих ключей.

#Для файла с данными:

#name,address,age
#Георгий,Невский проспект,22
#Иван,пр. Ветеранов,21

#будет возвращен следующий результат:

#[{'name': 'Георгий', 'age': '22', 'address': 'Невский проспект'}, {'name': 'Иван', 'age': '21', 'address': 'пр. Ветеранов'}]

#Обработайте возможные ошибки при работе с файлами.

import csv

def read_file(file):
    lst = list()
    try:
        with open(file, 'r') as new_file:
            reader = csv.DictReader(new_file)
            for row in reader:
                lst.append(dict(row))
            return lst
        print('Done')
    except Exception as e:
        print(e)




a = read_file('new_cvs.csv')
print(a)





