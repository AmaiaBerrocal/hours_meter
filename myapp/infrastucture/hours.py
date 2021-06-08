import sqlite3

from myapp.model.hour import Hour


class Hours:
    def createHoursTable(self):
        with sqlite3.connect('../../data/bbdd.db') as conn:  # usamos with para que abra y cierre la bbdd al terminar
            c = conn.cursor()
            c.execute('DROP TABLE IF EXISTS HOURS')
            c.execute('''CREATE TABLE HOURS (
                            ID_HOURS INTEGER PRIMARY KEY AUTOINCREMENT,
                            ID_USER INTEGER REFERENCES USERS(ID_USER),
                            YEAR INT NOT NULL,
                            MONTH INT NOT NULL,
                            DAY INT NOT NULL,
                            HOURS INT,
                            MINUTES INT,
                            CREATION_DATE DATETIME DEFAULT CURRENT_TIMESTAMP,
                            MODIFICATION_DATE DATETIME DEFAULT CURRENT_TIMESTAMP)''')
            conn.commit()

    def insertHour(self, id_user, year, month, day, hours, minutes):
        conn = sqlite3.connect('../../data/bbdd.db')
        try:
            c = conn.cursor()
            c.execute('INSERT INTO HOURS (ID_USER, YEAR, MONTH, DAY, HOURS, MINUTES) VALUES (?, ?, ?, ?, ?, ?)',
                      [id_user, year, month, day, hours, minutes])
            conn.commit()
        finally:
            conn.close()

    def getHoursPerDay(self, user_id, year, month, day):
        conn = sqlite3.connect('../../data/bbdd.db')
        try:
            c = conn.cursor()
            c.execute('SELECT * FROM HOURS WHERE ID_USER=? AND YEAR=? AND MONTH=? AND DAY=?', [user_id, year, month, day])
            rows = c.fetchall()
            hour = None
            if len(rows) > 0:
                row = rows[0]
                hour = Hour(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            return hour
        finally:
            conn.close()
'''
    def getHoursPerMonth(self, user_id, year, month):
        conn = sqlite3.connect('../../data/bbdd.db')
        try:
            c = conn.cursor()
            c.execute('SELECT * FROM HOURS WHERE ID_USER=? AND YEAR=? AND MONTH=?', [user_id, year, month])
            rows = c.fetchall()
            hours = None
            if len(rows) > 0:
                row = rows[0]
            hours = Hours(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            return hours
        finally:
            conn.close()

    def getHoursPerYear(self, user_id, year):
            conn = sqlite3.connect('../../data/bbdd.db')
        try:
            c = conn.cursor()
            c.execute('SELECT * FROM HOURS WHERE ID_USER=? AND YEAR=?', [user_id, year])
            rows = c.fetchall()
            hours = None
            if len(rows) > 0:
                row = rows[0]
            hours = Hours(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            return hours
        finally:
            conn.close()
'''

hours = Hours()
hours.createHoursTable()

hours.insertHour(2, 2021, 6, 3, 3, 0)
hours.insertHour(2, 2021, 6, 3, 8, 0)
hours.insertHour(1, 2021, 6, 3, 5, 0)
hours.insertHour(1, 2021, 6, 3, 8, 0)

print("ee" + str(hours.getHoursPerDay(2, 2021, 6, 3)))