import json

from flask import Flask, request
from flask_restful import abort

from myapp.application.getHours import GetHours
from myapp.application.login import Login
from myapp.exceptions.exceptions import Unauthorized, BadRequest

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_world(name):
    return "Hello, {}!".format(name)


@app.route('/login', methods=['POST'])
def login():
    try:
        user_name = request.form['username']
        password = request.form['password']
        id_user = Login().execute(user_name, password)
        return {'id_user': id_user}
    except Unauthorized:
        return abort(401)
    except BadRequest:
        return abort(400)

@app.route('/hours', methods=['GET'])
def hours():
    try:
        id_user = request.form['id_user']
        date_init = request.form['date_init']
        date_finish = request.form['date_finish']
        results = GetHours().execute(id_user, date_init, date_finish)
        return listToJson(results)
    except BadRequest:
        return abort(400)

def listToJson(list):
    jsonResult = []
    for row in list:
        jsonResult.append(row.__dict__)
    return json.dumps(jsonResult)

if __name__ == '__main__':
    app.run()
