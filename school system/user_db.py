
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



        #cursor.execute("""INSERT INTO User (username,firstname,surname,password)
        #VALUES('test_user','Bob','Marshall','123456')

        #""")

        #db.commit()

        #cursor.execute('SELECT * FROM User')
        #print(cursor.fetchall())
if __name__=='__main__':

    userdb()














