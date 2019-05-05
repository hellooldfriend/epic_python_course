from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)



@app.route('/show_tasks/', methods=['GET'])
def show_tasks():
    conn = sqlite3.connect('../lesson_11/tasks.db')
    cursor = conn.cursor()
    result = cursor.execute('select * from tasks')
    data = result.fetchall()
    return render_template('index.html', name='show task worked', data=data)


@app.route('/')
def index():
    test = 'Works??'
    return render_template('index.html', name=test)



@app.route('/', methods=['POST'])
def add_task():
    conn = sqlite3.connect('../lesson_11/tasks.db')
    cursor = conn.cursor()

    # taskname = request.form['name']
    # category = request.form['category']
    # datetime = request.form['datetime']

    # print(taskname, category, datetime)

    cursor.execute("insert into tasks (id, category, name, time) values (NULL, ?, ?, ?)",
                    (request.form['name'], request.form['category'], request.form['datetime']))
    conn.commit()
    conn.close()
    return show_tasks()
    # return render_template('index.html', name='add_task worked')


