# Прочитайте содержимое файла moby_clean.txt, полученного в упражнении 10.3.
# Используйте словарь для подсчета вхождений каждого слова,
# выведите первые 5 самых частых и самых редких слов.

def read_file(file):
    try:
        with open(file, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return e


text = read_file('moby_clean.txt')
lst = text.split()
dct = dict()

for word in lst:
    dct.setdefault(word, 0)
    dct[word] += 1


#print(lst.sort())