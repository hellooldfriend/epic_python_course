
#Напиши программу для очистки и нормализации первой главы ‘Моби Дика’, находящегося в файле 10/ moby.txt.

# 1) Все символы должны относиться к одному регистру.
# 2) Удалить все знаки препинания.
# 3) Записать слова по одному на строку во второй файл с именем moby_clean.txt


def read_file(file):
    try:
        with open(file, 'r') as file:
            content = file.read()
        return content


    except Exception as e:
        return e


text = read_file('moby.txt')
############################################
text = text.lower()

from string import punctuation

for i in text:
    if i in punctuation:
        text = text.replace(i, '')



##########################################
def write_file(file, lst):
    try:
        with open(file, 'w') as new_file:
            for s in lst:
                new_file.write("%s\n" % s)

        return 'Writnig is done.'
    except Exception as e:
        return e


lst = text.split()

write_file('moby_clean.txt', lst)


