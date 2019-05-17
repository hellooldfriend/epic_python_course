#Напишите программу для добавления задач (todo list).
#Для каждой из задач можно задать категорию и срок ее исполнения.
#Добавить возможность вывода списка задач.


tasks = ['description', 'category', 'date']

while True:
    inp = int(input('Enter the number: '))

    if inp == 1:
        task = list()
        desc = input('Add a description: ')
        task.append(desc)
        cat = input('Add a category: ')
        task.append(cat)
        date = input('Add a date: ')
        task.append(date)
        tasks.append(task)

    if inp == 2:
        new_tasks = tasks[3:]
        index = 0
        # print(index)
        for i in range(len(new_tasks)):
            print(f"Task: {new_tasks[index][0]}, category: {new_tasks[index][1]}, date: {new_tasks[index][2]}")
            index += 1

    if inp == 3:
        break

