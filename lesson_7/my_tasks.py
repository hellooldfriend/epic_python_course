#Напишите программу для добавления задач (todo list).
#Для каждой из задач можно задать категорию и срок ее исполнения.
#Добавить возможность вывода списка задач.


tasks = ['description', 'category', 'date']

while True:
    inp = int(input('Enter the number: '))

    if inp == 1:
        desc = input('Add a description: ')
        tasks.append(desc)
        cat = input('Add a category: ')
        tasks.append(cat)
        date = input('Add a date: ')
        tasks.append(date)

    if inp == 2:
        tasks = tasks[3:]
        index = 0

        for i in range(int(len(tasks) / 3)):
            print(f"Task: {tasks[index]}, category: {tasks[index + 1]}, date: {tasks[index + 2]}")
            index += 3

    if inp == 3:
        break

