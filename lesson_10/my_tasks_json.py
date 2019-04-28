#Напишите программу для добавления задач (todo list).
#Для каждой из задач можно задать категорию и срок ее исполнения.
#Добавить возможность вывода списка задач.


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
    inp = int(input('Enter the number: '))

    if inp == 1:
        desc = input('Add a description: ')
        task['name'] = desc
        cat = input('Add a category: ')
        task['category'] = cat
        date = input('Add a date: ')
        task['datetime'] = date
        lst.append(task)
        write('tasks.json', lst)

    if inp == 2:
        for i in lst:
            print(f"Task: {i['name']}, category: {i['category']}, date: {i['datetime']}")

    if inp == 3:
        break




