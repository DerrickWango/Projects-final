
import sqlite3


def Attendancedb():

        with sqlite3.connect('maindb.db') as db:
            cursor=db.cursor()




        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Attendance(
        Month VARCHAR(20) NOT NULL,
        Lectures VARCHAR(20) NOT NULL,
        Attended VARCHAR(20) NOT NULL);
        ''')


        #cursor.execute("""INSERT INTO User (username,firstname,surname,password)
        #VALUES('test_user','Bob','Marshall','123456')

        #""")

        #db.commit()

        #cursor.execute('SELECT * FROM Attendance')
        #print(cursor.fetchall())




if __name__=='__main__':
    
    Attendancedb()










