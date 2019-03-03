from tkinter import *

from tkinter import ttk

import math





class main(Tk):
    
    def __init__(self,*args,**kwargs):

        Tk.__init__(self,*args,**kwargs)

        self.title('EOQ calculator')

        self.geometry('730x350+150+150')

        Tk.iconbitmap(self,default='calculator_logo.ico')

        self.resizable(width=False,height=False)
        
        main_frame = Frame(self,bg='white')

        main_frame.pack(side=TOP,fill=BOTH,expand=YES)

        main_frame.grid_rowconfigure(0,weight=1)

        main_frame.grid_columnconfigure(0,weight=1)

        self.frames={}

        for F in (startpage,EOQ,EBQ,EOQ_with_discount,About):

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

        label0=Label(self,text='EOQ calculator',fg='steel blue',anchor='w',font='verdand 20 bold')

        label0.pack(padx=10,pady=10)

        label1=Label(self,text='Choose one of the options below',anchor='w')

        label1.pack(pady=10,padx=10)

        btn1=ttk.Button(self,text='EOQ',command= lambda: controller.show_frame(EOQ),width=30,style='TButton')

        btn1.pack(padx=10,pady=10)

        btn2=ttk.Button(self,text='EBQ',command= lambda: controller.show_frame(EBQ),width=30,style='TButton')

        btn2.pack(padx=10,pady=10)

        btn3=ttk.Button(self,text='EOQ(discounts)',command= lambda:controller.show_frame(EOQ_with_discount),width=30,style='TButton')

        btn3.pack(padx=10,pady=10)

        btn4=ttk.Button(self,text='About',command= lambda: controller.show_frame(About),width=30,style='TButton')

        btn4.pack(padx=10,pady=10)

        label06=Label(self,text="version 1.0.1",fg='steel blue').pack(side=BOTTOM,padx=10,pady=10)


        
class EOQ(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.a=StringVar()
        
        self.b=StringVar()
        
        self.c=StringVar()
        
        self.d=StringVar()
        
        self.display=StringVar()
        
        self.display1=StringVar()

        label01=Label(self,text='EOQ only',fg='steel blue',font='verdand 20 bold',anchor='w',padx=10,pady=10)

        label01.grid(row=0,column=1)

        lbl1=Label(self,text='Demand* :',font='arial 10 bold',fg='steel blue').grid(row=1,column=0)
        
        lbl2=Label(self,text='Order cost* :',font='arial 10 bold',fg='steel blue').grid(row=2,column=0)
        
        lbl3=Label(self,text='Holding cost* :',font='arial 10 bold',fg='steel blue').grid(row=1,column=2)
        
        lbl4=Label(self,text='Purchase cost* :',font='arial 10 bold',fg='steel blue').grid(row=2,column=2)
        
        lbl5=Label(self,text='EOQ :',font='arial 15 bold',fg='steel blue').grid(row=3,column=0)
        
        lbl6=Label(self,text='Total cost :',font='arial 15 bold',fg='steel blue').grid(row=4,column=0)

        ent1=Entry(self,textvariable=self.a,bg='white',bd=10).grid(row=1,column=1)
        
        ent2=Entry(self,textvariable=self.b,bg='white',bd=10).grid(row=2,column=1)
        
        ent3=Entry(self,textvariable=self.c,bg='white',bd=10).grid(row=1,column=3)
        
        ent4=Entry(self,textvariable=self.d,bg='white',bd=10).grid(row=2,column=3)
        
        ent5=Entry(self,textvariable=self.display,bg='steel blue',bd=10,font='arial 16 bold').grid(row=3,column=1)
        
        ent6=Entry(self,textvariable=self.display1,bg='steel blue',bd=10,font='arial 16 bold').grid(row=4,column=1)

        def eoq(event=None):
            
            try:
                
                x=float(self.a.get())#demand
                
                y=float(self.b.get())#order cost
                
                z=float(self.c.get())#holding cost
                
                zz=float(self.d.get())#purchase cost
                
                total=math.sqrt(float((2*x*y)/z))
                
                total2=((x*zz)+((y*x)/total)+((z*total)/2))
                
                self.display.set('%.1f units.'% total)
                
                self.display1.set('$ %.1f'% total2)


            except:
                 
                    self.display.set('Error!!')
                    
                    self.display1.set('Error!!')

        def reset1(event=None):

            self.a.set('')
            
            self.b.set('')
            
            self.c.set('')
            
            self.d.set('')
            
            self.display.set('')
            
            self.display1.set('')
            

        btn1=Button(self,bg='steel blue',bd=10,padx=20,pady=10,command=reset1,text='Reset',fg='black',font='arial 10 bold')
        
        btn1.grid(row=5,column=0)
        
        btn2=Button(self,bg='steel blue',bd=10,padx=20,pady=10,command=eoq,text='Calculate',fg='black',font='arial 10 bold')
        
        btn2.grid(row=5,column=1)

        btn5=Button(self,text='Return',bg='steel blue',fg='black',bd=10,padx=20,pady=10,command= lambda: controller.show_frame(startpage),font='arial 10 bold')

        btn5.grid(row=5,column=2)



        


        
class EBQ(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.a=StringVar()
        
        self.b=StringVar()
        
        self.c=StringVar()
        
        self.d=StringVar()
        
        self.display=StringVar()
        
        self.display1=StringVar()

        label01=Label(self,text='EBQ',fg='steel blue',font='verdand 20 bold',anchor='w',padx=10,pady=10)

        label01.grid(row=0,column=1)

        lbl1=Label(self,text='usage rate* :',font='arial 10 bold',fg='steel blue').grid(row=1,column=0)
        
        lbl2=Label(self,text='Order cost* :',font='arial 10 bold',fg='steel blue').grid(row=2,column=0)
        
        lbl3=Label(self,text='Holding cost* :',font='arial 10 bold',fg='steel blue').grid(row=1,column=2)
        
        lbl4=Label(self,text='production rate* :',font='arial 10 bold',fg='steel blue').grid(row=2,column=2)
                
        lbl6=Label(self,text='EBQ :',font='arial 15 bold',fg='steel blue').grid(row=4,column=0)

        ent1=Entry(self,textvariable=self.a,bg='white',bd=10).grid(row=1,column=1)
        
        ent2=Entry(self,textvariable=self.b,bg='white',bd=10).grid(row=2,column=1)
        
        ent3=Entry(self,textvariable=self.c,bg='white',bd=10).grid(row=1,column=3)
        
        ent4=Entry(self,textvariable=self.d,bg='white',bd=10).grid(row=2,column=3)
                
        ent5=Entry(self,textvariable=self.display,bg='steel blue',bd=10,font='arial 16 bold').grid(row=4,column=1)

        def ebq(event=None):
            
            try:
                
                x=float(self.a.get())#usage
                
                y=float(self.b.get())#order cost
                
                z=float(self.c.get())#holding cost
                
                zz=float(self.d.get())#demand
                
                total=math.sqrt(float((2*x*y)/(z*(1-(x/zz)))))
                
                self.display.set('%.1f units.'% total)
                

            except:
                 
                    self.display.set('Error!!')
                    

        def reset2(event=None):

            self.a.set('')
            
            self.b.set('')
            
            self.c.set('')
            
            self.d.set('')
            
            self.display.set('')
            
            self.display1.set('')
            

        btn1=Button(self,bg='steel blue',bd=10,padx=20,pady=10,command=reset2,text='Reset',fg='black',font='arial 10 bold')
        
        btn1.grid(row=5,column=0)
        
        btn2=Button(self,bg='steel blue',bd=10,padx=20,pady=10,command=ebq,text='Calculate',fg='black',font='arial 10 bold')
        
        btn2.grid(row=5,column=1)

        btn5=Button(self,text='Return',bg='steel blue',fg='black',bd=10,padx=20,pady=10,command= lambda: controller.show_frame(startpage),font='arial 10 bold')

        btn5.grid(row=5,column=2)





        
class EOQ_with_discount(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.a=StringVar()
        
        self.b=StringVar()
        
        self.c=StringVar()
        
        self.d=StringVar()

        self.e=StringVar()
        
        self.display=StringVar()
        
        self.display1=StringVar()

        label01=Label(self,text='EOQ with discount',fg='steel blue',font='verdand 20 bold',anchor='w',padx=10,pady=10)

        label01.grid(row=0,column=1)

        lbl1=Label(self,text='Demand* :',font='arial 10 bold',fg='steel blue').grid(row=1,column=0)
        
        lbl2=Label(self,text='Order cost* :',font='arial 10 bold',fg='steel blue').grid(row=2,column=0)
        
        lbl3=Label(self,text='Holding cost* :',font='arial 10 bold',fg='steel blue').grid(row=1,column=2)
        
        lbl4=Label(self,text='Purchase cost* :',font='arial 10 bold',fg='steel blue').grid(row=2,column=2)

        lbl5=Label(self,text='discount(%)* :',font='arial 10 bold',fg='steel blue').grid(row=3,column=0)
        
        lbl6=Label(self,text='EOQ :',font='arial 10 bold',fg='steel blue').grid(row=4,column=0)
        
        lbl7=Label(self,text='Total cost :',font='arial 15 bold',fg='steel blue').grid(row=5,column=0)

        ent1=Entry(self,textvariable=self.a,bg='white',bd=10).grid(row=1,column=1)
        
        ent2=Entry(self,textvariable=self.b,bg='white',bd=10).grid(row=2,column=1)
        
        ent3=Entry(self,textvariable=self.c,bg='white',bd=10).grid(row=1,column=3)
        
        ent4=Entry(self,textvariable=self.d,bg='white',bd=10).grid(row=2,column=3)

        ent5=Entry(self,textvariable=self.e,bg='white',bd=10).grid(row=3,column=1)
        
        ent6=Entry(self,textvariable=self.display,bg='white',bd=10).grid(row=4,column=1)
        
        ent7=Entry(self,textvariable=self.display1,bg='steel blue',bd=10,font='arial 16 bold').grid(row=5,column=1)

        def eoq(event=None):
            
            try:
                
                x=float(self.a.get())#demand
                
                y=float(self.b.get())#order cost
                
                z=float(self.c.get())#holding cost
                
                zz=float(self.d.get())#purchase cost

                zzz=float(self.e.get())#discount
                
                total=float(self.display.get())
                
                total2=((x*zz*((100-zzz)/100))+((y*x)/total)+((z*total*((100-zzz)/100))/2))
                
                self.display1.set('$ %.1f'% total2)

            except:
                    
                    self.display1.set('Error!!')

        def reset1(event=None):

            self.a.set('')
            
            self.b.set('')
            
            self.c.set('')
            
            self.d.set('')

            self.e.set('')
            
            self.display.set('')
            
            self.display1.set('')
            

        btn1=Button(self,bg='steel blue',bd=10,padx=20,pady=10,command=reset1,text='Reset',fg='black',font='arial 10 bold')
        
        btn1.grid(row=6,column=0)
        
        btn2=Button(self,bg='steel blue',bd=10,padx=20,pady=10,command=eoq,text='Calculate',fg='black',font='arial 10 bold')
        
        btn2.grid(row=6,column=1)

        btn5=Button(self,text='Return',bg='steel blue',fg='black',bd=10,padx=20,pady=10,command= lambda: controller.show_frame(startpage),font='arial 10 bold')

        btn5.grid(row=6,column=2)



        
class About(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        label04=Label(self,text='EOQ calculator',fg='steel blue',font='verdand 20 bold')

        label04.pack(padx=10,pady=10)

        label05=Label(self,text="""An Inventory control formulas calculator \n developed using tkinter in python.""",font='verdana 10 bold',fg='blue').pack(padx=10,pady=10)

        label06=Label(self,text="version 1.0.1",fg='steel blue').pack(padx=10,pady=10)

        btn8=ttk.Button(self,text='Back home',command= lambda: controller.show_frame(startpage))

        btn8.pack(side=BOTTOM)


app=main()

st=ttk.Style()

st.configure("TButton",foreground="steel blue",background="steel blue")

app.mainloop()

    
