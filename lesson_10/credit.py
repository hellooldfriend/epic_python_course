#name,region,date,value
#определенить регион с максимальным количеством заявок на потребительские кредиты в 2017 году.

def file_read(what, when):

    # what – потребительские кредиты
    # when – в 2017
    # value – кол-во заявок

    import csv
    lst = list()

    try:
        with open('opendata.csv', encoding='cp1251') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == what:
                    year = row[2][:4]
                    if year == str(when):
                        dct = dict()

                        if row[1] == 'Россия':
                            continue

                        if row[1] in lst:
                            item = next(i for i in lst if i['region'] == row[1])
                            item['value'] += int(row[3])
                        else:
                            dct.setdefault('region', row[1])
                            dct.setdefault('value', int(row[3]))
                        lst.append(dct)

        return lst
    except Exception as e:
        return e




lst = file_read('Количество заявок на потребительские кредиты', 2017)


def get_value(lst):
    max_value = 0

    for i in lst:
        if i['value'] > max_value:
            max_value = i['value']
            x = i

    return x


answer = get_value(lst)
print(f"Чемпиона за 2017 по ипотечным кредитам – регион: {answer['region']}, показатель: {answer['value']}")
