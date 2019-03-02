from tkinter import *

from tkinter import ttk

import os

from tkinter import messagebox as ms

import sqlite3

from Userdb import userdb

import hashlib as h

m=h.md5()


class main(Tk):
    
    def __init__(self,*args,**kwargs):

        Tk.__init__(self,*args,**kwargs)

        self.iconbitmap(self,default="myicon.ico")

        self.geometry("1280x550+50+50")

        main_frame = Frame(self,bg='white')

        main_frame.pack(side=TOP,fill=BOTH,expand=YES)

        main_frame.grid_rowconfigure(0,weight=1)

        main_frame.grid_columnconfigure(0,weight=1)

        self.frames={}

        for F in (startpage,mainpage,signup,Class,student,attendance,view_records,Admin):

            frame=F(main_frame,self)

            self.frames[F]= frame

            frame.grid(row=0,column=0,sticky='nsew')
            
        self.title('attendance management system')
        
        with sqlite3.connect('maindb.db') as db:

            cursor=db.cursor()

        initialize=('SELECT * FROM User')

        cursor.execute(initialize)

        user=cursor.fetchall()

        if user:

            self.show_frame(startpage)

        else:

            self.show_frame(signup)


    def show_frame(self,cont):
        
        frame=self.frames[cont]
        
        frame.tkraise()



class startpage(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.bind("<Return>",lambda:self.login)

        self.config(height=350,width=700)

        self.controller = controller

        self.username=StringVar()

        self.password=StringVar()

        label0=Label(self,text='Attendance Management System ',fg='steel blue',anchor='w',font='Times 30 bold italic')

        label0.place(anchor='c',relx=0.5,rely=0.1)

        label0=Label(self,text='Login',fg='steel blue',anchor='w',font='Times 15 bold italic')

        label0.place(anchor='c',relx=0.5,rely=0.4)

        label1= Label(self,text='Username',font='verdana 10 bold',fg='steel blue')

        label1.place(anchor='c',relx=0.4,rely=0.5)

        label2=Label(self,text='password',font='verdana 10 bold',fg='steel blue')

        label2.place(anchor='c',relx=0.4,rely=0.6)

        entry1=ttk.Entry(self,textvariable=self.username,width=35)

        entry1.place(anchor='c',relx=0.6,rely=0.5)

        entry2=ttk.Entry(self,textvariable=self.password,show='*',width=35)

        entry2.place(anchor='c',relx=0.6,rely=0.6)

        entry1.focus()

        entry2.focus()

        btn1=ttk.Button(self,text='login',command=self.login,width=35)

        btn1.place(anchor='c',relx=0.6,rely=0.7)

        btn1=ttk.Button(self,text='Add new user',command=self.show_admin,width=35)

        btn1.place(anchor='c',relx=0.4,rely=0.7)

    def show_admin(self):

        return self.controller.show_frame(Admin),self.username.set(''),self.password.set('')


    
    def login(self,Event=None):

            while True:

                with sqlite3.connect('maindb.db') as db:

                    cursor=db.cursor()

                find_user= ("SELECT * FROM User WHERE username=? AND password =? ")

                passhash=bytes(self.password.get(),encoding='utf-8')

                m.update(passhash)

                cursor.execute(find_user,[(self.username.get()),(m.hexdigest())])

                result=cursor.fetchall()


                if result:

                    for i in result:
                        
                            return self.controller.show_frame(mainpage),self.username.set(''),self.password.set('')

                        
                            

                else:

                    return ms.showinfo("Error","User {} not found!".format(self.username.get())), self.password.set('')


            



class Admin(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.controller=controller

        self.password=StringVar()

        label1= Label(self,text='Enter Admin password',font='verdana 10 bold',fg='steel blue')

        label1.place(anchor='c',relx=0.4,rely=0.4)

        entry1=ttk.Entry(self,textvariable=self.password,show='*',width=30)

        entry1.place(anchor='c',relx=0.6,rely=0.4)

        entry1.focus()

        btn1=ttk.Button(self,text='login',command=self.Login,width=30)

        btn1.place(anchor='c',relx=0.6,rely=0.7)

        btn1=ttk.Button(self,text='back',command=self.back,width=30)

        btn1.place(anchor='c',relx=0.4,rely=0.7)

    def back(self):

        return self.controller.show_frame(startpage) ,self.password.set('')


    def Login(self):
        
            while True:

                        with sqlite3.connect('maindb.db') as db:

                            cursor=db.cursor()

                        find_user= ("SELECT * FROM User WHERE password =? ")

                        passhash=bytes(self.password.get(),encoding='utf-8')

                        m.update(passhash)

                        cursor.execute(find_user,[(m.hexdigest())])

                        result=cursor.fetchall()

                        if result:

                            for i in result:

                                    return self.controller.show_frame(signup),self.password.set('')

                        else:

                            return ms.showinfo('Error','User not found!'),self.password.set('')


class signup(Frame):

    def __init__(self,parent,controller):

                Frame.__init__(self,parent)

                self.controller = controller

                self.username=StringVar()

                self.firstname=StringVar()

                self.surname=StringVar()

                self.password=StringVar()

                label0=Label(self,text='Sign up',fg='steel blue',anchor='w',font='Times 20 bold italic')

                label0.place(anchor='c',relx=0.5,rely=0.1)

                label0=Label(self,text="Add Admin account if It's your first time",fg='steel blue',anchor='w',font='Arial 7 bold ')

                label0.place(anchor='c',relx=0.5,rely=0.3)

                label1= Label(self,text='Username',font='verdana 10 bold',fg='steel blue')

                label1.place(anchor='c',relx=0.4,rely=0.4)

                label2= Label(self,text='Firstname',font='verdana 10 bold',fg='steel blue')

                label2.place(anchor='c',relx=0.4,rely=0.5)
                        
                label3= Label(self,text='surname',font='verdana 10 bold',fg='steel blue')

                label3.place(anchor='c',relx=0.4,rely=0.6)

                label4=Label(self,text='password',font='verdana 10 bold',fg='steel blue')

                label4.place(anchor='c',relx=0.4,rely=0.7)

                entry1=ttk.Entry(self,width=35,textvariable=self.username)

                entry1.place(anchor='c',relx=0.6,rely=0.4)

                entry2=ttk.Entry(self,width=35,textvariable=self.firstname)

                entry2.place(anchor='c',relx=0.6,rely=0.5)

                entry3=ttk.Entry(self,width=35,textvariable=self.surname)

                entry3.place(anchor='c',relx=0.6,rely=0.6)

                entry4=ttk.Entry(self,width=35,textvariable=self.password,show='*')

                entry4.place(anchor='c',relx=0.6,rely=0.7)

                btn1=ttk.Button(self,text='Login instead',command=self.Return,width=35)

                btn1.place(anchor='c',relx=0.4,rely=0.85)

                btn2=ttk.Button(self,text='Sign up',command=self.sign_up,width=35)

                btn2.place(anchor='c',relx=0.6,rely=0.85)

                entry1.focus()

                entry2.focus()

                entry3.focus()

                entry4.focus()

    def Return(self):

        return self.controller.show_frame(startpage),self.username.set(''),self.firstname.set(''),self.surname.set(''),self.password.set('')


    def validation(self):

                    return len(self.username.get()) != 0 and len(self.firstname.get()) != 0 and len(self.surname.get()) != 0 and len(self.password.get()) != 0

    def sign_up(self):

                    if self.validation():
                        
                                        
                                        found=0

                                        while found==0:

                                                with sqlite3.connect('maindb.db') as db:

                                                        cursor=db.cursor()


                                                finduser=("SELECT * FROM User WHERE username=? AND password=?")

                                                cursor.execute(finduser,[(self.username.get()),(self.password.get())])

                                                results=cursor.fetchall()

                                                if results:

                                                        return ms.showinfo("Error","User already exists!"),self.username.set(''),self.firstname.set(''),self.surname.set(''),self.password.set('')
                                                
                                                else:
                                                        found=1


                                        found2=0

                                        len_pass=(8-len(self.password.get()))

                                        while found2==0:

                                            if len(self.password.get())<8:

                                                return ms.showinfo("Error","Password should be at least 8 characters! You have {} more to go!".format(len_pass)),self.password.set('')

                                            else:

                                                found2=1
                                                
                                        new_user=("""INSERT INTO User(username,firstname,surname,password)

                                                                          VALUES(?,?,?,?)""")

                                        passhash=bytes(self.password.get(),encoding='utf-8')

                                        m.update(passhash)

                                        cursor.execute(new_user,[(self.username.get()),(self.firstname.get()),(self.surname.get()),(m.hexdigest())])

                                        db.commit()

                                        cursor.close()

                                        db.close()

                                        ms.showinfo("confirm","Added to database.")

                                        self.username.set('')

                                        self.firstname.set('')

                                        self.surname.set('')

                                        self.password.set('')






                    else:
                            

                                        return ms.showinfo("Error","Insert required Fields!")
                                                                                



               

class mainpage(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.controller=controller

        btn=ttk.Button(self,text='log out',command=self.logout)

        btn.place(anchor='sw',relx=0.9,rely=0.99)



    def logout(self):

        return self.controller.show_frame(startpage)

    def session(self):

        with sqlite3.connect('maindb.db') as db:

                cursor=db.cursor()

        select_session=('SELECT * FROM Session')

        cursor.execute(select_session)

        lst=cursor.fetchall()

        lbl=Label(self,text=("Logged in as : {}".format(lst[0][0],lst[0][1])),font='verdana 10 bold',fg='steel blue')

        lbl.place(relx=0.01,rely=0.01)

        return lbl


        

        
        
    

        



class student(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)





class attendance(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

     

        
class Class(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

 
class view_records(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        








app=main()

app.mainloop()










                    
