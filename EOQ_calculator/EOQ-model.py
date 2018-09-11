
#=================imports===================#
from tkinter import *
import time
import math
#===========================================#

#================configs====================#
root=Tk()
root.configure(bg='white')
root.title('EOQ calculator')
root.geometry("700x350+150+150")
root.resizable(height=False,width=False)
#===========================================#

#=============================variables and functionality===============================#
def label(n):
    lbll=Label(f1,text='Enter valid input!!',fg='white',bg=n).grid(row=2,column=2)
    lbllx=Label(f1,text='Required fields* !!',fg='white',bg=n).grid(row=3,column=2)

def eoq(event=None):
    try:
        x=float(a.get())#demand
        y=float(b.get())#order cost
        z=float(c.get())#holding cost
        zz=float(d.get())#purchase cost
        total=math.sqrt(float((2*x*y)/z))
        total2=((x*zz)+((y*x)/total)+((z*total)/2))
        display.set('%.1f units.'% total)
        display1.set('$ %.1f'% total2)

    except:
        display.set('Error!!')
        display1.set('Error!!')
        label('red')

def reset(event=None):
    a.set('')
    b.set('')
    c.set('')
    d.set('')
    display.set('')
    display1.set('')
    label('white')
    

a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
display=StringVar()
display1=StringVar()
#=============================================================================================#

#===============key bindings================#
root.bind('<Return>',eoq)
root.bind('<Escape>',reset)
#===========================================#

#================frames=====================#
f0=Frame(root,width=700,height=30,bg='powder blue')
f0.pack(side=TOP)
f1=Frame(root,width=700,height=250,bg='white')
f1.pack(side=BOTTOM)
#===========================================#

#================date=======================#
datelbl=time.strftime("%d/%m/%y")
#===========================================#

#==========================================info labels=================================================#
lblx=Label(f0,text='EOQ calculator',fg='steel blue',font='arial 24 bold',anchor='w',bg='white').grid()
lbly=Label(f0,text=datelbl,fg='steel blue',font='arial 10 bold',anchor='w',bg='white').grid()
#======================================================================================================#

#===========================================entries and labels======================================#
lbl1=Label(f1,text='Demand* :',font='arial 10 bold',bg='white',fg='steel blue').grid(row=0,column=0)
lbl2=Label(f1,text='Order cost* :',font='arial 10 bold',bg='white',fg='steel blue').grid(row=1,column=0)
lbl3=Label(f1,text='Holding cost* :',font='arial 10 bold',bg='white',fg='steel blue').grid(row=0,column=2)
lbl4=Label(f1,text='Purchase cost* :',font='arial 10 bold',bg='white',fg='steel blue').grid(row=1,column=2)
lbl5=Label(f1,text='EOQ :',font='arial 15 bold',bg='white',fg='steel blue').grid(row=3,column=0)
lbl6=Label(f1,text='Total cost :',font='arial 15 bold',bg='white',fg='steel blue').grid(row=4,column=0)


ent1=Entry(f1,textvariable=a,bg='white',bd=10).grid(row=0,column=1)
ent2=Entry(f1,textvariable=b,bg='white',bd=10).grid(row=1,column=1)
ent3=Entry(f1,textvariable=c,bg='white',bd=10).grid(row=0,column=3)
ent4=Entry(f1,textvariable=d,bg='white',bd=10).grid(row=1,column=3)
ent5=Entry(f1,textvariable=display,bg='powder blue',bd=10,font='arial 16 bold').grid(row=3,column=1)
ent6=Entry(f1,textvariable=display1,bg='powder blue',bd=10,font='arial 16 bold').grid(row=4,column=1)
#=====================================================================================================#

#===============================================buttons======================================================#
btn1=Button(f1,bg='powder blue',bd=10,padx=20,pady=10,command=reset,text='Reset',fg='steel blue',font='arial 10 bold').grid(row=5,column=0)
btn2=Button(f1,bg='powder blue',bd=10,padx=20,pady=10,command=eoq,text='Calculate',fg='steel blue',font='arial 10 bold').grid(row=5,column=1)
btn3=Button(f1,bg='powder blue',bd=10,padx=20,pady=10,command=root.destroy,text='Quit',fg='steel blue',font='arial 10 bold').grid(row=5,column=2)
#============================================================================================================#


root.mainloop()
