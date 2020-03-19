import pymysql

config = {
        'user': 'admin',
        'password': 'test',
        'host': 'mysql',
        'database': 'database'
    }

configWrite = {
    'user': 'admin',
    'password': 'test',
    'host': 'mysql-0.mysql',
    'database': 'database'
}


def check_db():
    conn = None
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        stmt = "SHOW TABLES LIKE 'IDENTIFICATION'"
        cursor.execute(stmt)
        result = cursor.fetchone()
        if result:
            return
        else:
            create_table()
    except pymysql.Error as error:
        print(error)

    finally:
        if conn:
            conn.close()


def create_table():
    conn = None
    try:
        conn = pymysql.connect(**configWrite)
        c = conn.cursor()
        c.execute('''CREATE TABLE IDENTIFICATION
                ( Id VARCHAR(200) PRIMARY KEY NOT NULL, User VARCHAR(200) NOT NULL)''')
    except pymysql.Error as error:
        print(error)

    finally:
        if conn:
            conn.close()


def insert_into_db(id, user):
    check_db()
    conn = None
    try:
        conn = pymysql.connect(**configWrite)
        cursor = conn.cursor()
        query = "INSERT INTO IDENTIFICATION (Id, User) VALUES('" + str(id) + "', '" + str(user) + "')"
        cursor.execute(query)
        conn.commit()
    except pymysql.Error as error:
        print(error)

    finally:
        if conn:
            conn.close()


def get_all_from_db():
    check_db()
    conn = None
    values = []
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        query = "SELECT * FROM IDENTIFICATION;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            values.append(row)
        return values
    except pymysql.Error as error:
        print(error)

    finally:
        if conn:
            conn.close()


