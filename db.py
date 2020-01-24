import sqlite3
import os

pathToDb = "/usr/db/database.db"


def check_db():
    if os.path.exists(pathToDb):
        if os.path.isfile(pathToDb):
            return
    create_table()


def create_table():
    conn = sqlite3.connect(pathToDb)

    c = conn.cursor()
    c.execute('''CREATE TABLE IDENTIFICATION
            ( Id TEXT PRIMARY KEY NOT NULL, User TEXT NOT NULL)''')


def insert_into_db(id, user):
    check_db()
    conn = None
    try:
        conn = sqlite3.connect(pathToDb)
        cursor = conn.cursor()
        query = "INSERT INTO IDENTIFICATION (Id, User) VALUES('" + str(id) + "', '" + str(user) + "')"
        cursor.execute(query)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

    finally:
        if conn:
            conn.close()


def get_all_from_db():
    check_db()
    conn = None
    values = []
    try:
        conn = sqlite3.connect(pathToDb)
        cursor = conn.cursor()
        query = "SELECT * FROM IDENTIFICATION;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            values.append(row)
        return values
    except sqlite3.Error as error:
        print(error)

    finally:
        if conn:
            conn.close()


