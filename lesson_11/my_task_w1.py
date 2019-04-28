
import tkinter

tasks = list()

def add():
    task = dict()
    task.setdefault('description', entry_description.get())
    task.setdefault('category', entry_category.get())
    task.setdefault('datetime', entry_datetime.get())
    tasks.append(task)

    clear_entry(entry_description)
    clear_entry(entry_category)
    clear_entry(entry_datetime)

    write_file('my_tasks.json', tasks)

    return tasks

def exit():
    window.destroy()

def clear_entry(entry):
     entry.delete(0, 'end')


def write_file(file, lst):
    import json

    try:
        with open(file, 'w') as new_file:
            json.dump(lst, new_file)
        return 'Done'
    except Exception as error:
        return error


def show_tasks():
    import json

    try:
        with open('my_tasks.json', 'r') as file:
            data = json.load(file)
            # return print(data, type(data))
            for task in data:
                print(task)
    except Exception as error:
        return error



window = tkinter.Tk()
window.title('Task manager')

frame = tkinter.Frame(window)
frame.pack()

label_description = tkinter.Label(frame, text='Task')
label_description.pack()

entry_description = tkinter.Entry(frame)
entry_description.pack()

###

label_category = tkinter.Label(frame, text='Category')
label_category.pack()

entry_category = tkinter.Entry(frame)
entry_category.pack()

###

label_datetime = tkinter.Label(frame, text='Time')
label_datetime.pack()

entry_datetime = tkinter.Entry(frame)
entry_datetime.pack()

####
####

button_submit = tkinter.Button(frame, text='Add', command=add)
button_submit.pack()

###

button_list = tkinter.Button(frame, text='Show tasks', command=show_tasks)
button_list.pack()

###

button_exit = tkinter.Button(frame, text='Exit', command=exit)
button_exit.pack()

######

window.mainloop()
