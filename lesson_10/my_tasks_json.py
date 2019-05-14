#Напишите программу для добавления задач (todo list).
#Для каждой из задач можно задать категорию и срок ее исполнения.
#Добавить возможность вывода списка задач.

def simple_read(file):
    import json
    data = list()

    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            return data
    except Exception as error:
        return error

# x = simple_read('tasks.json')
# print(x)

def read(file):
    import json

    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            for task in data:
                print(task)
    except Exception as error:
        return error


def write(file, lst):
    import json

    try:
        with open(file, 'w') as new_file:
            json.dump(lst, new_file)
        return 'Done'
    except Exception as error:
        return error



task = {
    'name': '',
    'category': '',
    'datetime': '',
}

lst = list()

while True:
    data = simple_read('tasks.json')

    inp = int(input('Enter the number: '))

    if inp == 1:
        desc = input('Add a description: ')
        task['name'] = desc
        cat = input('Add a category: ')
        task['category'] = cat
        date = input('Add a date: ')
        task['datetime'] = date
        data.append(task)
        write('tasks.json', data)

    if inp == 2:
        for task in data:
            print(task)
        # read('tasks.json')

    if inp == 3:
        break




