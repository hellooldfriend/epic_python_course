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


from collections import Counter
most_commom = Counter(lst).most_common(5)
least_common = Counter(lst).most_common()[:-5-1:-1]


print(f'5 most common:{most_commom} \n 5 least common {least_common}')
