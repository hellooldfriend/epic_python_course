from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Orwell'



@app.route('/xxx')
def xxx():
    data = 'darkness'
    return render_template('index.html', name=data)



@app.route('/<string:name>')
def hello(name):
    return f'Hello, {name}!'



