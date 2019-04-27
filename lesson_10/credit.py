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
                        dct.setdefault('region', row[1])
                        dct.setdefault('value', row[3])
                        lst.append(dct)
        return lst
        print('so done')
    except Exception as e:
        return e




lst = file_read('Количество заявок на потребительские кредиты', 2017)


def get_value(lst):

    item = [item for item in lst if int(item['value']) == max([int(x['value']) for x in lst])]
    item = dict(item[0])
    return item





answer = get_value(lst)
print(f'Регион: {answer["region"]}, кол-во: {answer["value"]}')

