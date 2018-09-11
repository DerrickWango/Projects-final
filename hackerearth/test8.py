from tkinter import *


from tkinter import ttk



class main(Tk):
    
    def __init__(self,*args,**kwargs):

        Tk.__init__(self,*args,**kwargs)

        self.title('flags')

        self.geometry('730x350+100+100')

        #self.resizable(width=False,height=False)
        
        main_frame = Frame(self,bg='white')

        main_frame.pack(side=TOP,fill=BOTH,expand=YES)

        main_frame.grid_rowconfigure(0,weight=1)

        main_frame.grid_columnconfigure(0,weight=1)

        self.frames={}

        for F in (startpage,german,italian,french,mali,latvia):

            frame=F(main_frame,self)

            self.frames[F]= frame

            frame.grid(row=0,column=0,sticky='nsew')
            
        self.show_frame(startpage)


    def show_frame(self,cont):
        
        frame=self.frames[cont]
        
        frame.tkraise()




class startpage(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.controller=controller


        ttk.Button(self,text='German Flag',width=20,command=lambda:self.controller.show_frame(german)).pack(side=TOP,padx=10,pady=10)

        ttk.Button(self,text='Italian Flag',width=20,command=lambda:self.controller.show_frame(italian)).pack(side=TOP,padx=10,pady=10)

        ttk.Button(self,text='French Flag',width=20,command=lambda:self.controller.show_frame(french)).pack(side=TOP,padx=10,pady=10)

        ttk.Button(self,text='Latvian Flag',width=20,command=lambda:self.controller.show_frame(latvia)).pack(side=TOP,padx=10,pady=10)

        ttk.Button(self,text='Malian Flag',width=20,command=lambda:self.controller.show_frame(mali)).pack(side=TOP,padx=10,pady=10)






class german(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.controller=controller

        ttk.Button(self,text='Home',width=20,command=lambda:self.controller.show_frame(startpage)).pack(side=TOP,padx=10,pady=10)

        self.label('black',TOP)

        self.label('red',TOP)

        self.label('yellow',TOP)


    def label(self,n,Side):

        return Label(self,bg=n).pack(side=Side,fill=BOTH,expand=YES)





class italian(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.controller=controller

        ttk.Button(self,text='Home',width=20,command=lambda:self.controller.show_frame(startpage)).pack(side=TOP,padx=10,pady=10)

        self.label('green',LEFT)

        self.label('white',LEFT)

        self.label('red',LEFT)


    def label(self,n,Side):

        return Label(self,bg=n).pack(side=Side,fill=BOTH,expand=YES)






class french(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.controller=controller

        ttk.Button(self,text='Home',width=20,command=lambda:self.controller.show_frame(startpage)).pack(side=TOP,padx=10,pady=10)

        self.label('blue',LEFT)

        self.label('white',LEFT)

        self.label('maroon',LEFT)


    def label(self,n,Side):

        return Label(self,bg=n).pack(side=Side,fill=BOTH,expand=YES)






class latvia(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.controller=controller

        ttk.Button(self,text='Home',width=20,command=lambda:self.controller.show_frame(startpage)).pack(side=TOP,padx=10,pady=10)

        self.label('maroon',TOP)

        self.label('white',TOP)

        self.label('maroon',TOP)


    def label(self,n,Side):

        return Label(self,bg=n).pack(side=Side,fill=BOTH,expand=YES)






class mali(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.controller=controller

        ttk.Button(self,text='Home',width=20,command=lambda:self.controller.show_frame(startpage)).pack(side=TOP,padx=10,pady=10)

        self.label('green',LEFT)

        self.label('yellow',LEFT)

        self.label('maroon',LEFT)


    def label(self,n,Side):

        return Label(self,bg=n).pack(side=Side,fill=BOTH,expand=YES)











app=main()

app.mainloop()











    
        
