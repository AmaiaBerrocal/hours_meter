import sqlite3

class Users:
    def createUsersTable(self):
        conn = sqlite3.connect('./data/bbdd.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Users (
	                id_user    INTEGER PRIMARY KEY AUTOINCREMENT,
	                user_name TEXT NOT NULL,
	                password    TEXT NOT NULL,
	                creation_date DATETIME NOW,
                    modification_date DATETIME NOW)''')
                    #al ponerlo con tres comillas simples, puedo escribir en strinfg en varias líneas sin necesidad de sumar cademas con  el signo +
        conn.commit()
        c.close()
        conn.close()

    def createUser(self, user_name, password):
        conn = sqlite3.connect('./data/bbdd.db')
        c = conn.cursor()
        c.execute('INSERT INTO Users (user_name, password) VALUES (?, ?)')
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