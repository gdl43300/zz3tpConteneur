import mysql

config = {
        'user': 'admin',
        'password': 'test',
        'host': 'db',
        'database': 'database'
    }


def check_db():
    stmt = "SHOW TABLES LIKE 'IDENTIFICATION'"
    conn = mysql.connector.connect(**config)
    conn.execute(stmt)
    result = conn.fetchone()
    if result:
        return
    else:
        create_table()


def create_table():
    conn = mysql.connector.connect(**config)
    c = conn.cursor()
    c.execute('''CREATE TABLE IDENTIFICATION
            ( Id TEXT PRIMARY KEY NOT NULL, User TEXT NOT NULL)''')


def insert_into_db(id, user):
    check_db()
    conn = None
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        query = "INSERT INTO IDENTIFICATION (Id, User) VALUES('" + str(id) + "', '" + str(user) + "')"
        cursor.execute(query)
        conn.commit()
    except mysql.Error as error:
        print(error)

    finally:
        if conn:
            conn.close()


def get_all_from_db():
    check_db()
    conn = None
    values = []
    try:
        conn = mysql.connector.connect(**config)
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


