import sqlite3

from myapp.model.user import User


class Users:
    def createUsersTable(self):
        with sqlite3.connect('../../data/bbdd.db') as conn:
            c = conn.cursor()
            c.execute('DROP TABLE IF EXISTS USERS')
            c.execute('''CREATE TABLE USERS (
                            ID_USER    INTEGER PRIMARY KEY AUTOINCREMENT,
                            USER_NAME TEXT NOT NULL UNIQUE,
                            PASSWORD    TEXT NOT NULL,
                            CREATION_DATE DATETIME DEFAULT CURRENT_TIMESTAMP,
                            MODIFICATION_DATE DATETIME DEFAULT CURRENT_TIMESTAMP)''') #DEFAULT CURRENT_TIMESTAMP pone por defecto la fecha actual
                            #al ponerlo con tres comillas simples, puedo escribir en string en varias líneas sin necesidad de sumar cademas con  el signo +
            conn.commit()

    def createUser(self, user_name, password):
        conn = sqlite3.connect('../../data/bbdd.db')
        try:
            c = conn.cursor()
            c.execute('INSERT INTO USERS (USER_NAME, PASSWORD) VALUES (?, ?)', [user_name, password]) #en la tabla USERS, en las columnas USER_NAME y PASSWORD meto los valores ?? que me pasaran como argumento user_name y password
            conn.commit()
        finally:
            conn.close()

    def retrieveUser(self, user_name, password):
        conn = sqlite3.connect('../../data/bbdd.db')
        try:
            c = conn.cursor()
            c.execute('SELECT * FROM Users where USER_NAME=? and PASSWORD=?', [user_name, password])
            rows = c.fetchall()
            user = None
            if len(rows) > 0:
                row = rows[0]
                user = User(row[0], row[1], row[2], row[3], row[4])
            return user
        finally:
            conn.close()

