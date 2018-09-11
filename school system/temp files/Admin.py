



class signup(Frame):

    def __init__(self,parent,controller):

                Frame.__init__(self,parent)


                self.geometry("700x350+200+200")

                self.username=StringVar()

                self.firstname=StringVar()

                self.surname=StringVar()

                self.password=StringVar()

                label0=Label(self,text='Sign up',fg='steel blue',anchor='w',font='verdana 20 bold')

                label0.place(anchor='c',relx=0.5,rely=0.1)

                label1= Label(self,text='Username',font='verdana 10 bold',fg='steel blue')

                label1.place(anchor='c',relx=0.4,rely=0.4)

                label2= Label(self,text='Firstname',font='verdana 10 bold',fg='steel blue')

                label2.place(anchor='c',relx=0.4,rely=0.5)
                        
                label3= Label(self,text='surname',font='verdana 10 bold',fg='steel blue')

                label3.place(anchor='c',relx=0.4,rely=0.6)

                label4=Label(self,text='password',font='verdana 10 bold',fg='steel blue')

                label4.place(anchor='c',relx=0.4,rely=0.7)

                entry1=Entry(self,bd=10,textvariable=username)

                entry1.place(anchor='c',relx=0.6,rely=0.4)

                entry2=Entry(self,bd=10,textvariable=firstname)

                entry2.place(anchor='c',relx=0.6,rely=0.5)

                entry3=Entry(self,bd=10,textvariable=surname)

                entry3.place(anchor='c',relx=0.6,rely=0.6)

                entry4=Entry(self,bd=10,textvariable=password,show='*')

                entry4.place(anchor='c',relx=0.6,rely=0.7)

                btn1=ttk.Button(self,text='quit',command=self.destroy)

                btn1.place(anchor='c',relx=0.7,rely=0.9)

                btn2=ttk.Button(self,text='Sign up',command=self.sign_up)

                btn2.place(anchor='c',relx=0.9,rely=0.9)


    def validation(self):

                    return len(self.username.get()) != 0 and len(self.firstname.get()) != 0 and len(self.surname.get()) != 0 and len(self.password.get()) != 0

    def sign_up(self):

                    if self.validation():
                        
                                        
                                        found=0
                                        
                                        while found==0:

                                                with sqlite3.connect('eoq.db') as db:

                                                        cursor=db.cursor()

                                                finduser=("SELECT * FROM User WHERE username=?")

                                                cursor.execute(finduser,[(self.username.get())])

                                                results=cursor.fetchall()

                                                if results:

                                                        return ms.showinfo("Error","Already exists!"),self.username.set(''),self.firstname.set(''),self.surname.set(''),self.password.set('')
                                                
                                                else:
                                                        found=1



                                        
                                        new_user=("""INSERT INTO User(username,firstname,surname,password)

                                                                          VALUES(?,?,?,?)""") 

                                        cursor.execute(new_user,[(self.username.get()),(self.firstname.get()),(self.surname.get()),(self.password.get())])

                                        db.commit()

                                        cursor.close()

                                        db.close()

                                        ms.showinfo("confirm","Added to database.")

                    else:
                            

                                        return ms.showinfo("Error","Insert required details!")
                                                                                




                    
