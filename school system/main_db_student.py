
import sqlite3


def studentdb():

        with sqlite3.connect('maindb.db') as db:
            cursor=db.cursor()



        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student(
        Grno VARCHAR(20) NOT NULL,
        firstname VARCHAR(20) NOT NULL,
        lastname VARCHAR(20) NOT NULL,
        class VARCHAR(20) NOT NULL,
        Rollno VARCHAR(20) NOT NULL);
        ''')

        #cursor.execute("""INSERT INTO User (username,firstname,surname,password)
        #VALUES('test_user','Bob','Marshall','123456')

        #""")

        #db.commit()

        #cursor.execute('SELECT * FROM Student')
        #print(cursor.fetchall())

if __name__=='__main__':

    student()














