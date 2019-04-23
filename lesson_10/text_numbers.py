# Напишите функцию, которая
# вставляет нумерацию перед строками текстового файла.
#В функцию необходимо передать имя входного текстового файла и имя выходного текстового файла.
#Например, входной файл имеет имя text.txt и содержит следующий текст:

# Край любимый! Сердцу снятся
# Скирды солнца в водах лонных,
# Я хотел бы затеряться
# В зеленях твоих стозвонных.

#Имя выходного файла указываем update_text.txt и он будет содержать следующий текст:
#1 Край любимый! Сердцу снятся
#2 Скирды солнца в водах лонных,
#3 Я хотел бы затеряться
#4 В зеленях твоих стозвонных.

#Корректно обработайте возможность передачи несуществующего файла.



def read_file(file):
    try:
        with open(file, 'r') as file:
            lines = file.readlines()
        return lines
    except Exception as e:
        return e


def write_file(file, lst):
    try:
        with open(file, 'w') as out_file:
            for i, line in enumerate(lst):
                line = f'{i + 1} ' + line
                out_file.write(line)
        print('Done')
    except Exception as e:
        return e


def f(a, b):
    lst = read_file(a)

    new_file = write_file(b, lst)
    return new_file


f('text.txt', 'update_text.txt')



