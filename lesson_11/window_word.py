#Программа отображает случайное слово на английском языке (из заранее созданного словаря).
#Пользователь пытается угадать слово на русском языке.
import tkinter


dct = {
    'dog': 'собака',
    'cat': 'кошка',
    'mouse': 'мышь',
    'door': 'дверь',
    'button': 'кнопка',
}

def random(dct):
    import random
    return random.choice(list(dct.keys()))


def submit():
    user_word = entry.get()
    word = label_word.cget('text')

    if dct.get(word) == user_word:
        return label_res.config(text='Угадали!')
    else:
        return label_res.config(text="Sounds good, doesn't work.")

def exit():
    window.destroy()


def restart():
    random(dct)
    entry.delete(0, 'end')

window = tkinter.Tk()
window.title('tk')

frame = tkinter.Frame(window)
frame.pack()

label_task = tkinter.Label(frame, text="Случайное слово:")
label_task.pack()

label_word = tkinter.Label(frame, text=random(dct))
label_word.pack()


label_ins = tkinter.Label(frame, text="Укажите перевод слова:")
label_ins.pack()

entry = tkinter.Entry(frame)
entry.pack()

label_res = tkinter.Label(frame)
label_res.pack()

button_submit = tkinter.Button(frame, text="Готово!", command=submit)
button_submit.pack()

button_exit = tkinter.Button(frame, text="Выход", command=exit)
button_exit.pack()

window.mainloop()