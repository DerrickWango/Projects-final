from tkinter import *

from tkinter import ttk

from tkinter.font import Font

from database import Models

from tkinter import messagebox as ms





class main(Tk):

    def __init__(self,*args,**kwargs):

        Tk.__init__(self,*args,**kwargs)

        self.geometry("1280x550+50+50")

        #self.iconbitmap(self,default="logo.ico")

        main_frame = Frame(self)

        main_frame.pack(side=TOP,fill=BOTH,expand=YES)

        main_frame.grid_rowconfigure(0,weight=1)

        main_frame.grid_columnconfigure(0,weight=1)

        self.frames={}

        for F in (createdpage,startpage,create_database):

            frame=F(main_frame,self)

            self.frames[F]= frame

            frame.grid(row=0,column=0,sticky='nsew')
            
        self.title('supermarket system')

        self.show_frame(startpage)

        



    def show_frame(self,cont):
        
        frame=self.frames[cont]
        
        frame.tkraise()



class startpage(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.controller=controller

        l1 = ttk.Label(self,text="Supermarket system",style='HW.TLabel')

        l1.place(relx=0.42,rely=0.03)

        l2 = ttk.Label(self,text="Please click below to create an interface for your business",style='NW.TLabel')

        l2.place(relx=0.33,rely=0.3)

        l3 = ttk.Label(self,text="or",style='NW.TLabel' )

        l3.place(relx=0.53,rely=0.6)

        btn=ttk.Button(self,text="Create new interface",style="NORMAL.TButton",width=30,command=lambda:self.create_database(1))

        btn.place(relx=0.45,rely=0.5)
        
        btn1=ttk.Button(self,text="Open existing settings",style="NORMAL.TButton",width=30,command=lambda:self.create_database(2))

        btn1.place(relx=0.45,rely=0.7)

    def create_database(self,choice):

        if choice==1:

            return self.controller.show_frame(create_database)

        elif choice==2:

            return self.controller.show_frame(createdpage)

        else:

            pass



class createdpage(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.controller=controller

        ttk.Label(self,text='created page',style="LW.TLabel").place(relx=0.5,rely=0.1)

        btn=ttk.Button(self,text="^",style="SPECIAL.TButton",width=5,command=self.switch1)

        btn.place(relx=0.1,rely=0.1)


    def switch1(self):

        return self.controller.show_frame(startpage)


class create_database(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.database_name=StringVar()

        self.controller=controller

        lbl1=ttk.Label(self,text='Create your database',style='HW.TLabel').place(relx=0.4,rely=0.01)

        btn=ttk.Button(self,text='Z',style="SPECIAL.TButton",command=self.switch_home)

        btn.place(relx=0.007,rely=0.03)

        label1=ttk.Label(self,text='Create records name',style="LW.TLabel")

        label1.place(relx=0.007,rely=0.18)

        entry1=ttk.Entry(self,textvariable=self.database_name,width=25,style="TEntry")

        entry1.place(relx=0.13,rely=0.18)

        btn=Button(self,text='Commit',bg="sea green",fg="white",command=self.connect_db,font=("Comic Sans MS",10,"bold"),bd=0,padx=4,pady=4,width=15)

        btn.place(relx=0.85,rely=0.9)

        btn2=Button(self,text='Delete',bg="maroon",fg="white",command=self.connect_db,font=("Comic Sans MS",10,"bold"),bd=0,padx=4,pady=4,width=15)

        btn2.place(relx=0.007,rely=0.9)


        


    def switch_home(self):

        return self.controller.show_frame(startpage)

    def connect_db(self):

        if len(self.database_name.get())==0:

            return ms.showinfo("Error message","Please insert records name!")

        else:

            connection=Models('{}'.format(self.database_name.get()))

            return connection,ms.showinfo('sucess','Database created!')
      













app=main()

btn_font1=Font(family="Wingdings 3",size=10)

btn_font2=Font(family="Wingdings",size=12)

btn_normal=Font(family="Comic Sans MS",size=8)

txt_font = Font(family="Comic Sans MS", size=13)

lbl_font = Font(family="Comic Sans MS", size=10)

heading_font = Font(family="Comic Sans MS", size=22)

style = ttk.Style()
        
style.configure("SPECIAL.TButton", foreground="sea green", background="grey",font=btn_font1)

style.configure("TEntry",padding=5,background="grey")

style.configure("NORMAL.TButton", foreground="sea green", background="grey",font=btn_normal)

style.configure("HW.TLabel", foreground="sea green", font=heading_font)

style.configure("NW.TLabel", foreground="sea green", font=txt_font)

style.configure("LW.TLabel", foreground="white",background="sea green",padding=3, font=lbl_font)


app.mainloop()
