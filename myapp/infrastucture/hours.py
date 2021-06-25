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
                            DATE TEXT NOT NULL,
                            HOURS INT,
                            MINUTES INT,
                            CREATION_DATE DATETIME DEFAULT CURRENT_TIMESTAMP,
                            MODIFICATION_DATE DATETIME DEFAULT CURRENT_TIMESTAMP)''')
            conn.commit()

    def insertHour(self, id_user, date, hours, minutes):
        conn = sqlite3.connect('../../data/bbdd.db')
        try:
            c = conn.cursor()
            c.execute('INSERT INTO HOURS (ID_USER, DATE, HOURS, MINUTES) VALUES (?, ?, ?, ?)',
                      [id_user, date, hours, minutes])
            conn.commit()
        finally:
            conn.close()

    def getHours(self, user_id, date_init, date_finish):
        conn = sqlite3.connect('../../data/bbdd.db')
        try:
            c = conn.cursor()
            c.execute('SELECT * FROM HOURS WHERE ID_USER=? AND DATE BETWEEN ? AND ?',
                      [user_id, date_init, date_finish])
            rows = c.fetchall()
            results = []
            for row in rows:
                results.append(Hour(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            return results
        finally:
            conn.close()
'''
h = Hours()
h.createHoursTable()
h.insertHour(1,"2021-03-01",3,0)
h.insertHour(1,"2021-03-02",3,0)
h.insertHour(1,"2021-03-03",3,0)
h.insertHour(1,"2021-03-04",3,0)
h.insertHour(1,"2021-03-05",3,0)
'''