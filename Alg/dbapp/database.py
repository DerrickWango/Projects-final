import sqlite3

import random

from Selection_sort import selection_sort

from tkinter import *


with sqlite3.connect('testdb.db') as db:

    cursor=db.cursor()



create=cursor.execute('''CREATE TABLE IF NOT EXISTS Identities(

                            id INTEGER PRIMARY KEY NOT NULL,

                            name TEXT NOT NULL,

                            id_no INTEGER NOT NULL

                            );''')


names=['Derrick','Warren','Ann','Kingboy','Carollyn','Benson','Mary','Teddy','Justin','Loise','Gina','Andrew','Vicky','Amin',

     'Samuel','Patricia','Washington','James','Christine','Lavender','Roy','David','Patsy','Ed','Philip','Cornellius','Alma',

     'Grace','Daphine','Zazi','Yvonne','Zuenna','Eric','Aden','Joe','Noel','Charles','Evans','Clinton','Paul','Simon','Acie',

     'Daniel','Janet','Maria','Joab','Ezekiel','Ezra','John','Moana','Nancy','Ivan','Edwin','Hillary','Sean','Phoebe','Asha',

     'Avan','Nina','Matilda','Elodie','Rahab','Keziah','Doreen','Jay','Enoch','Theodore','Mitchelle','Jackson','Lori','Amos',

     'Roxanne','Maureen','Everlyn','Esther','Francis','Norah','Joyce','Magdaline','Jacqline','Barrack','Betty','Saul','Ason',

     'Alan','Renny','Bill','William','Diana','Emma','Emm','Jo','Ryan','Nicole','Sophia','Donald','Luke','Edward','Bo','Cher',

     'Joel','Madilyn','Anastacia','Doug','Susan','Taby','Sharon','Bob','Fabiana','Shane','Mathew','Jason','Mark','Ty','Coby',

     'Abu','Timothy','Sarah','Faith','Bryan','Bernice','Elijah','Alvin','Yvette','Angela','Miriam','Adam','Lisa','An','Boyd',

     'Cathryn','Emmanuel','Keith','George','Ellen','Jessy','Solomon','Job','Derek','Felicia','Keisha','Leah','Sylvia','Carl',

     'Chandler','Vanessa','Ali','Victoria','Elizabeth','Laureen','Vincent','Elise','Lydia','Thomas','Marques','Beryl','Dora',

     'Vivian','Rick','Ben','Gerald','Nathan','Annabell','Damaris','Henry','Leonardo','Ivy','Nicholas','Morris','Wendy','Ida',

     'Gladwell','Rose','Branston','Rebecca','Cynthia','Moses','Peter','Anthony','Jack','Lenny','Isaac','Travis','Noah','Glen',

     ]

'''
y=selection_sort(names)

srt=y.sort('a')



for i in srt:

        cursor.execute('INSERT INTO Identities(name,id_no) VALUES(?,?)',[(i),(random.randint(67500,99999))])


db.commit()

db.close()



'''

cursor.execute('SELECT name FROM Identities')

master = Tk()

lst=[]



for optionList  in cursor.fetchall():

    lst.append(optionList)

    

v = StringVar()
v.set('__SELECT__')
om = OptionMenu(master, v,'__SELECT__', *lst).pack()






master.mainloop() 














