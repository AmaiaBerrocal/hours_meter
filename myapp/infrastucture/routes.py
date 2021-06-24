from flask import Flask, request
from flask_restful import abort

from myapp.application.login import Login
from myapp.exceptions.exceptions import Unauthorized

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_world(name):
    return "Hello, {}!".format(name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        user_name = request.form['username']
        password = request.form['password']
        id_user = Login().execute(user_name, password)
        return {"id_user": id_user}
    except Unauthorized:
        return abort(401)


if __name__ == '__main__':
    app.run()
