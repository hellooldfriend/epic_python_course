from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

file_address = '../lesson_11/tasks.db'

def read():
    conn = sqlite3.connect(file_address)
    cursor = conn.cursor()
    result = cursor.execute('select * from tasks')
    data = result.fetchall()
    return data

@app.route('/show_tasks/', methods=['GET'])
def show_tasks():
    data = read()
    return render_template('index.html', name='Shows task', data=data)


@app.route('/')
def index():
    title = 'I\'m your task manager, you may add a task.'
    return render_template('index.html', name=title)


@app.route('/', methods=['POST'])
def add_task():
    conn = sqlite3.connect(file_address)
    cursor = conn.cursor()

    cursor.execute("insert into tasks (id, category, name, time) values (NULL, ?, ?, ?)",
                    (request.form['name'], request.form['category'], request.form['datetime']))
    conn.commit()
    conn.close()
    return render_template('index.html', name='Task added')


