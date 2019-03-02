import sqlite3

def userdb():
        with sqlite3.connect('maindb.db') as db:
            cursor=db.cursor()



        cursor.execute('''
        CREATE TABLE IF NOT EXISTS User(
        username VARCHAR(20) NOT NULL,
        firstname VARCHAR(20) NOT NULL,
        surname VARCHAR(20) NOT NULL,
        password VARCHAR(20) NOT NULL);
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Session(
        firstname VARCHAR(20) NOT NULL,
        lastname VARCHAR(20) NOT NULL);
        ''')


userdb()
