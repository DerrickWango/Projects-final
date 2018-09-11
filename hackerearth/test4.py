from tkinter import *

from tkinter import ttk

import math

from tkinter import messagebox as ms



root=Tk()

root.title("Factorial calculator")

result=StringVar()

fact=StringVar()

def factorial(event=None):

        try:

                n=int(fact.get())

                count=0

                while count==0:

                        if n>=1000:

                                return ms.showinfo('error',"{} is too large a number!".format(n))

                        else:
                                count=1

                x=math.factorial(n)

                return result.set(x)

        except:

                result.set('ERROR!!')

                fact.set('ERROR!!')


def reset(event2=None):

        fact.set("")

        result.set("")

root.geometry("550x350+100+100")

root.bind('<Escape>',reset)

root.bind('<Return>',factorial)

label=Label(root,text='Enter number',bd=5,font='chiller 15 bold',bg='steel blue',width=20)

label.place(relx=0.1,rely=0.1)

label2=Label(root,text='Result',bd=5,font='chiller 15 bold',bg='steel blue',width=20)

label2.place(relx=0.1,rely=0.3)

ent1=Entry(root,textvariable=result,bd=10,width=30,bg='steel blue',font='arial 10 bold')

ent1.place(relx=0.5,rely=0.3)

ent2=Entry(root,textvariable=fact,bd=10,width=30)

ent2.place(relx=0.5,rely=0.1)

btn=ttk.Button(root,text='calculate',command=factorial,width=70)

btn.place(relx=0.1,rely=0.6)

btn=ttk.Button(root,text='reset',command=reset,width=70)

btn.place(relx=0.1,rely=0.5)


root.mainloop()
















