from tkinter import *

from tkinter import ttk

import random


rand=random.randint(0,12)

colors=['red','orange','yellow','green','blue','indigo','violet','tan','purple','navy blue','steel blue','pink']

txt=colors[rand]

root=Tk()

root.geometry('200x200+200+200')

lbl=Label(root,text=txt,bg=txt,font='arial 15 bold').pack(side=LEFT,expand=YES,fill=BOTH)


root.mainloop()
