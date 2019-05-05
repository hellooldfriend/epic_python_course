import sqlite3
import tkinter


def exit():
    window.destroy()

def clear_entry(entry):
     entry.delete(0, 'end')


def add_task():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("insert into tasks (id, category, name, time) values (NULL, ?, ?, ?)",
                    (entry_category.get(), entry_description.get(), entry_datetime.get()))
    conn.commit()
    conn.close()

    clear_entry(entry_description)
    clear_entry(entry_category)
    clear_entry(entry_datetime)


def show_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    result = cursor.execute('select * from tasks')
    data = result.fetchall()
    all_tasks = ''

    for task in data:
        s = f'task: {task[2]}, category: {task[1]}, date: {task[3]} \n'
        all_tasks += s
    text_box.config(text=all_tasks)

    conn.close()




window = tkinter.Tk()
window.title('Task manager')

frame = tkinter.Frame(window)
frame.pack()

frame4 = tkinter.Frame(window)
frame4.pack()

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

button_submit = tkinter.Button(frame, text='Add', command=add_task)
button_submit.pack()

###

button_list = tkinter.Button(frame, text='Show tasks', command=show_tasks)
button_list.pack()

###

button_exit = tkinter.Button(frame, text='Exit', command=exit)
button_exit.pack()

######

text_box = tkinter.Label(frame4)
text_box.pack()


window.mainloop()
