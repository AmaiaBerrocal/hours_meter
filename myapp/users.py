import sqlite3

class Users:
    def createUsersTable(self):
        conn = sqlite3.connect('./data/bbdd.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS USERS (
	                ID_USER    INTEGER PRIMARY KEY AUTOINCREMENT,
	                USER_NAME TEXT NOT NULL,
	                PASSWORD    TEXT NOT NULL,
	                CREATION_DATE DATETIME DEFAULT CURRENT_TIMESTAMP,
                    MODIFICATION_DATE DATETIME DEFAULT CURRENT_TIMESTAMP)''') #DEFAULT CURRENT_TIMESTAMP pone por defecto la fecha actual
                    #al ponerlo con tres comillas simples, puedo escribir en string en varias líneas sin necesidad de sumar cademas con  el signo +
        conn.commit()
        c.close()
        conn.close()

    def createUser(self, user_name, password):
        conn = sqlite3.connect('./data/bbdd.db')
        c = conn.cursor()
        c.execute('INSERT INTO USERS (USER_NAME, PASSWORD) VALUES (?, ?)', [user_name, password]) #en la tabla USERS, en las columnas USER_NAME y PASSWORD meto los valores ?? que me pasaran como argumento user_name y password
        conn.commit()
        c.close()
        conn.close()

class User:
    def __init__(self, id_user, user_name, password, creation_date, modification_date):
        self.id_user = id_user
        self.user_name = user_name
        self.password = password
        self.creation_date = creation_date
        self.modification_date = modification_date
    
    def retriveUser(self):
        conn = sqlite3.connect('./data/bbdd.db')
        c = conn.cursor()
        c.execute('SELECT id_user, user_name, password FROM Users')
        conn.commit()
        c.close()
        conn.close()

users = Users()
users.createUsersTable()# creas tabla
users.createUser('Amaia', 'password')# mete usuario en tabla
'''
amaia = user.retrieveUser('Amaia')
#amaia tiene que ser de tipo 'User'
print(amaia)# pinte la info de amaia: id, nombre, pasword
user.retrieveUser('Amaia', 'password')
print(amaia)# pinte la info de amaia: id, nombre, password'''