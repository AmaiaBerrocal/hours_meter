from flask import Flask, request

from myapp.application.login import Login

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_world(name):
    return "Hello, {}!".format(name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    user_name = request.form['username']
    password = request.form['password']
    id_user = Login().execute(user_name, password)
    return id_user


if __name__ == '__main__':
    app.run()
