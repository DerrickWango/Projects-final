
import sqlite3


def classdb():
        with sqlite3.connect('maindb.db') as db:
            cursor=db.cursor()




        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Class(
        Classname VARCHAR(20) NOT NULL,
        Subjects VARCHAR(20) NOT NULL,
        Startingrollno VARCHAR(20) NOT NULL);
        ''')

        #cursor.execute("""INSERT INTO User (username,firstname,surname,password)
        #VALUES('test_user','Bob','Marshall','123456')

        #""")

        #db.commit()

        #cursor.execute('SELECT * FROM Class')
        #print(cursor.fetchall())

if __name__=='__main__':

    classdb()













