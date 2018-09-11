
import sqlite3


with sqlite3.connect('maindb.db') as db:
    cursor=db.cursor()



cursor.execute('''
CREATE TABLE IF NOT EXISTS useradmin(
password_admin VARCHAR(20) NOT NULL);
''')



#cursor.execute("""INSERT INTO User (username,firstname,surname,password)
#VALUES('test_user','Bob','Marshall','123456')

#""")

#db.commit()

cursor.execute('SELECT * FROM useradmin')
print(cursor.fetchall())















