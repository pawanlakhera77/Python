from turtle import *
from Tkinter import *
import webbrowser 
from tkMessageBox import *
import time
import shutil
import os
import tkFileDialog
import pygame
import random
from pygame.locals import *
import tkFont

dat=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
     28,29,30,31]

da=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']

yer=[2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030]

cat=['Travel','Clothing','Entertainment','Food','Groceries','Sports','Club','Charity']

incat=['Salary','Borrowed','Items Sold','Betting','Bonus','Stock Market','Donation']

#Fin Man..
def FinMan():
    r3=Tk()

    r3.title('FinMan (Finance Manager)')
    r3.geometry('400x100')
    r3.config(bg='white')
    r3.resizable(0,0)

    def delinc():
        def dinc():
            finam=drop5.cget('text')+' '+drop6.cget('text')+' '+drop7.cget('text')+'.txt'
            compath="C:\\Income\\%s" %finam
            if drop5.cget('text')=='Select'  or drop6.cget('text')=='Select' or drop7.cget('text')=='Select':
                showerror('Eror','All Fields Must be specified')

            elif os.path.isfile(compath)==True:
                os.remove(compath)
                showinfo('Message','Record Deleted Successfuly')
            else:
                showerror("Error",'No Record')
        r5=Tk()
        r5.config(bg='white')
        r5.geometry('800x200')
        r5.title('Delete Income');
        r5.resizable(0,0)
        l4=Label(r5,text='Choose dd.mm.yyyy',font='calibri')
        l4.pack()
        l4.config(bg='white')
        l4.place(bordermode=OUTSIDE,x=100,y=10)
        var5=StringVar(r5)
        var5.set('Select')
        drop5=OptionMenu(r5,var5,*dat)
        drop5.pack()
        drop5.place(bordermode=OUTSIDE,x=270,y=10)

        var6=StringVar(r5)
        var6.set('Select')
        drop6=OptionMenu(r5,var6,*mon)
        drop6.pack()
        drop6.place(bordermode=OUTSIDE,x=360,y=10)

        var7=StringVar(r5)
        var7.set('Select')
        drop7=OptionMenu(r5,var7,*yer)
        drop7.pack()
        drop7.place(bordermode=OUTSIDE,x=440,y=10)

        
        bt3=Button(r5,text='Delete',command=dinc,width=10)
        bt3.pack()
        bt3.place(bordermode=OUTSIDE,x=350,y=100)
        
        r5.mainloop()

    def inview():
        def inviurec():
            finam=drop5.cget('text')+' '+drop6.cget('text')+' '+drop7.cget('text')+'.txt'
            path='C:\\Income';
            compath="C:\\Income\\%s" %finam
            print compath
            cd=os.getcwd();
            if drop5.cget('text')=='Select'  or drop6.cget('text')=='Select' or drop7.cget('text')=='Select':
                showerror('Eror','All Fields Must be specified')

            elif os.path.isfile(compath)==True:
                os.chdir(path)
                f=open(finam,'r')
                r=f.read()
                f.close()
                print r
                os.chdir(cd)
                r6=Tk()
                r6.geometry('500x400')
                r6.title('Income (%s)'%finam)
                l4=Label(r6,text=r)
                l4.pack()
                l4.config(bg='white')
                l4.place(bordermode=OUTSIDE,x=2,y=5)
                os.chdir(cd)
                r6.mainloop()
            else:
                showerror("Error",'No Record')
                
            
        r5=Tk()
        r5.config(bg='white')
        r5.geometry('800x200')
        r5.title('Income');
        r5.resizable(0,0)
        l4=Label(r5,text='Choose dd.mm.yyyy',font='calibri')
        l4.pack()
        l4.config(bg='white')
        l4.place(bordermode=OUTSIDE,x=100,y=10)
        var5=StringVar(r5)
        var5.set('Select')
        drop5=OptionMenu(r5,var5,*dat)
        drop5.pack()
        drop5.place(bordermode=OUTSIDE,x=270,y=10)

        var6=StringVar(r5)
        var6.set('Select')
        drop6=OptionMenu(r5,var6,*mon)
        drop6.pack()
        drop6.place(bordermode=OUTSIDE,x=360,y=10)

        var7=StringVar(r5)
        var7.set('Select')
        drop7=OptionMenu(r5,var7,*yer)
        drop7.pack()
        drop7.place(bordermode=OUTSIDE,x=440,y=10)

        
        bt3=Button(r5,text='View',command=inviurec,width=10)
        bt3.pack()
        bt3.place(bordermode=OUTSIDE,x=350,y=100)
        
        r5.mainloop()


    def inc():
       def inchknsave():
        if drop.cget('text')=='Select'  or drop2.cget('text')=='Select' or drop3.cget('text')=='Select' or drop4.cget('text')=='Select'or not e2.get():
            showerror('Eror','All Fields Must be specified')

        else:
            cd=os.getcwd();
            path='C:\\Income'
            if not os.path.exists(path):
                os.makedirs(path)
            fname=drop2.cget('text')+' '+drop3.cget('text')+' '+drop4.cget('text')+'.txt'
            exp=drop.cget('text')+': '+'Rs.'+e2.get()
            compath='C:\\Income\\%s' %fname;
            
            f=open('temp.txt','w')
            f.write(exp)
            f.write('\n')
            f.close()
            if  os.path.isfile(compath)==True: #if file already exist
                f=open('temp.txt','r')
                r=f.read();
                f.close()   
                
                os.chdir(path)      #directory changed
                g=open(fname,'a')
                g.write(r)
                g.close()
                os.chdir(cd)
                os.remove('temp.txt')
            else:
                os.rename('temp.txt',fname)
                shutil.move(fname,path);

       
       r6=Tk()
       r6.config(bg='white')
       r6.geometry('800x200')
       r6.title('Income')
       r6.resizable(0,0)

       l6=Label(r6,text='Category',font='ariel')
       l6.pack();
       l6.config(bg='white')
       l6.place(bordermode=OUTSIDE,x=50,y=10)

       l6=Label(r6,text='Date',font='ariel')
       l6.pack();
       l6.config(bg='white')
       l6.place(bordermode=OUTSIDE,x=150,y=10)



       l6=Label(r6,text='Month',font='ariel')
       l6.pack();
       l6.config(bg='white')
       l6.place(bordermode=OUTSIDE,x=250,y=10)

       l6=Label(r6,text='Year',font='ariel')
       l6.pack();
       l6.config(bg='white')
       l6.place(bordermode=OUTSIDE,x=350,y=10)

       l6=Label(r6,text='Income',font='ariel')
       l6.pack();
       l6.config(bg='white')
       l6.place(bordermode=OUTSIDE,x=450,y=10)


       var1 = StringVar(r6)
       var1.set('Select')
       drop = OptionMenu(r6,var1,*incat)
       drop.pack()
       drop.place(bordermode=OUTSIDE,x=50,y=30)

       var2 = StringVar(r6)
       var2.set('Select')
       drop2 = OptionMenu(r6,var2,*dat)
       drop2.pack()
       drop2.place(bordermode=OUTSIDE,x=150,y=30)

       var3 = StringVar(r6)
       var3.set('Select')
       drop3 = OptionMenu(r6,var3,*mon)
       drop3.pack()
       drop3.place(bordermode=OUTSIDE,x=250,y=30)

       var4 = StringVar(r6)
       var4.set('Select')
       drop4 = OptionMenu(r6,var4,*yer)
       drop4.pack()
       drop4.place(bordermode=OUTSIDE,x=350,y=30)


       e2=Entry(r6)
       e2.pack()
       e2.focus()
       e2.config(bg='cyan')
       e2.place(bordermode=OUTSIDE,x=450,y=30)
        
       bt4=Button(r6,text='Save',height=1,width=10,command=inchknsave)
       bt4.pack()
       bt4.place(bordermode=OUTSIDE,x=100,y=150)

       bt5=Button(r6,text='View Income',height=1,width=14,command=inview)
       bt5.pack()
       bt5.place(bordermode=OUTSIDE,x=300,y=150)

       bt6=Button(r6,text='Delete Income',height=1,width=14,command=delinc)
       bt6.pack()
       bt6.place(bordermode=OUTSIDE,x=500,y=150)

       r6.mainloop()


    def delexp():
        def dexp():
            finam=drop5.cget('text')+' '+drop6.cget('text')+' '+drop7.cget('text')+'.txt'
            compath="C:\\Expenses\\%s" %finam
            if drop5.cget('text')=='Select'  or drop6.cget('text')=='Select' or drop7.cget('text')=='Select':
                showerror('Eror','All Fields Must be specified')

            elif os.path.isfile(compath)==True:
                os.remove(compath)
                showinfo('Message','Record Deleted Successfuly')
            else:
                showerror("Error",'No Record')
        r5=Tk()
        r5.config(bg='white')
        r5.geometry('800x200')
        r5.title('View Expense');
        r5.resizable(0,0)
        l4=Label(r5,text='Choose dd.mm.yyyy',font='calibri')
        l4.pack()
        l4.config(bg='white')
        l4.place(bordermode=OUTSIDE,x=100,y=10)
        var5=StringVar(r5)
        var5.set('Select')
        drop5=OptionMenu(r5,var5,*dat)
        drop5.pack()
        drop5.place(bordermode=OUTSIDE,x=270,y=10)

        var6=StringVar(r5)
        var6.set('Select')
        drop6=OptionMenu(r5,var6,*mon)
        drop6.pack()
        drop6.place(bordermode=OUTSIDE,x=360,y=10)

        var7=StringVar(r5)
        var7.set('Select')
        drop7=OptionMenu(r5,var7,*yer)
        drop7.pack()
        drop7.place(bordermode=OUTSIDE,x=440,y=10)

        
        bt3=Button(r5,text='Delete',command=dexp,width=10)
        bt3.pack()
        bt3.place(bordermode=OUTSIDE,x=350,y=100)
        
        r5.mainloop()

    def view():
        def viurec():
            finam=drop5.cget('text')+' '+drop6.cget('text')+' '+drop7.cget('text')+'.txt'
            path='C:\\Expenses';
            compath="C:\\Expenses\\%s" %finam
            print compath
            cd=os.getcwd();
            if drop5.cget('text')=='Select'  or drop6.cget('text')=='Select' or drop7.cget('text')=='Select':
                showerror('Eror','All Fields Must be specified')

            elif os.path.isfile(compath)==True:
                os.chdir(path)
                f=open(finam,'r')
                r=f.read()
                f.close()
                print r
                os.chdir(cd)
                r6=Tk()
                r6.geometry('500x400')
                r6.title('Expenses (%s)'%finam)
                l4=Label(r6,text=r)
                l4.config(bg='white')
                l4.pack()
                l4.place(bordermode=OUTSIDE,x=2,y=5)
                os.chdir(cd)
                r6.mainloop()
            else:
                showerror("Error",'No Record')
                
            
        r5=Tk()
        r5.config(bg='white')
        r5.geometry('800x200')
        r5.title('Expense');
        r5.resizable(0,0)
        l4=Label(r5,text='Choose dd.mm.yyyy',font='calibri')
        l4.pack()
        l4.config(bg='white')
        l4.place(bordermode=OUTSIDE,x=100,y=10)
        var5=StringVar(r5)
        var5.set('Select')
        drop5=OptionMenu(r5,var5,*dat)
        drop5.pack()
        drop5.place(bordermode=OUTSIDE,x=270,y=10)

        var6=StringVar(r5)
        var6.set('Select')
        drop6=OptionMenu(r5,var6,*mon)
        drop6.pack()
        drop6.place(bordermode=OUTSIDE,x=360,y=10)

        var7=StringVar(r5)
        var7.set('Select')
        drop7=OptionMenu(r5,var7,*yer)
        drop7.pack()
        drop7.place(bordermode=OUTSIDE,x=440,y=10)

        
        bt3=Button(r5,text='View',command=viurec,width=10)
        bt3.pack()
        bt3.place(bordermode=OUTSIDE,x=350,y=100)
        
        r5.mainloop()


    def exp():
       def chknsave():
          if drop.cget('text')=='Select'  or drop2.cget('text')=='Select' or drop3.cget('text')=='Select' or drop4.cget('text')=='Select'or not e2.get():
               showerror('Eror','All Fields Must be specified')
          else:
               cd=os.getcwd();
               path='C:\\Expenses'
               if not os.path.exists(path):
                   os.makedirs(path)
               fname=drop2.cget('text')+' '+drop3.cget('text')+' '+drop4.cget('text')+'.txt'
               exp=drop.cget('text')+':'+'Rs.'+e2.get()
               compath='C:\\Expenses\\%s' %fname;
            
               f=open('temp.txt','w')
               f.write(exp)
               f.write('\n')
               f.close()
               if  os.path.isfile(compath)==True: #if file already exist
                   f=open('temp.txt','r')
                   r=f.read();
                   f.close()   
                
                   os.chdir(path)      #directory changed
                   g=open(fname,'a')
                   g.write(r)
                   g.close()
                   os.chdir(cd)
                   os.remove('temp.txt')
               else:
                   os.rename('temp.txt',fname)
                   shutil.move(fname,path);
            

       r4=Tk()
       r4.config(bg='white')
       r4.geometry('800x200')
       r4.title('Expense')
       r4.resizable(0,0)
       
       l4=Label(r4,text='Category',font='ariel')
       l4.pack();
       l4.config(bg='white')
       l4.place(bordermode=OUTSIDE,x=50,y=10)

       l4=Label(r4,text='Date',font='ariel')
       l4.pack();
       l4.config(bg='white')
       l4.place(bordermode=OUTSIDE,x=150,y=10)



       l4=Label(r4,text='Month',font='ariel')
       l4.pack();
       l4.config(bg='white')
       l4.place(bordermode=OUTSIDE,x=250,y=10)

       l4=Label(r4,text='Year',font='ariel')
       l4.pack();
       l4.config(bg='white')
       l4.place(bordermode=OUTSIDE,x=350,y=10)

       l4=Label(r4,text='Expenses',font='ariel')
       l4.pack();
       l4.config(bg='white')
       l4.place(bordermode=OUTSIDE,x=450,y=10)


       var1 = StringVar(r4)
       var1.set('Select')
       drop = OptionMenu(r4,var1,*cat)
       drop.pack()
       drop.place(bordermode=OUTSIDE,x=50,y=30)

       var2 = StringVar(r4)
       var2.set('Select')
       drop2 = OptionMenu(r4,var2,*dat)
       drop2.pack()
       drop2.place(bordermode=OUTSIDE,x=150,y=30)

       var3 = StringVar(r4)
       var3.set('Select')
       drop3 = OptionMenu(r4,var3,*mon)
       drop3.pack()
       drop3.place(bordermode=OUTSIDE,x=250,y=30)

       var4 = StringVar(r4)
       var4.set('Select')
       drop4 = OptionMenu(r4,var4,*yer)
       drop4.pack()
       drop4.place(bordermode=OUTSIDE,x=350,y=30)


       e2=Entry(r4)
       e2.pack()
       e2.focus()
       e2.config(bg='cyan')
       e2.place(bordermode=OUTSIDE,x=450,y=30)
        
       bt=Button(r4,text='Save',height=1,width=10,command=chknsave)
       bt.pack(side=BOTTOM)
       bt.place(bordermode=OUTSIDE,x=100,y=150)

       bt2=Button(r4,text='View Expense',height=1,width=14,command=view)
       bt2.pack()
       bt2.place(bordermode=OUTSIDE,x=300,y=150)

       bt3=Button(r4,text='Delete Expense',height=1,width=14,command=delexp)
       bt3.pack()
       bt3.place(bordermode=OUTSIDE,x=500,y=150)
       
       r4.mainloop()

        
    b1=Button(r3,text='Expenses',command=exp)
    b1.pack()
    b1.place(bordermode=OUTSIDE,height=30,width=60,x=30,y=40)


    b2=Button(r3,text='Income',command=inc)
    b2.pack()
    b2.place(bordermode=OUTSIDE,height=30,width=60,x=300,y=40)

    l=Label(r3,text='Mange Your Expenses And Your Income',font='ariel')
    l.pack(side=TOP)
    l.config(bg='white')

    r3.mainloop()

#Note Maker
def Note_Maker():
    

    sizes=[14,20,25,35,40,50,55,60,67,73,75]
    root=Tk()
    root.title('Note Maker')
    path='C:\\Docs'
    cd=os.getcwd()
    fnt='ariel'
    if not os.path.exists(path):
        os.makedirs(path)
    def denc():
             
        def opdenc():
            def dencr():
                
                if askquestion('Warning','Sure About Decrypting File')=='yes':
                    rd=Tk()
                    rd.title('Decryption')
                    l=[]
                    fns=e2.get()
                    os.chdir(path)
                    f=open(fns,'r')
                    re=f.read()
                    print re
                    for let in re:
                        l.append(let)
                    print l
                    
                                           
                    for i in range(len(l)-1):
                        for j in range(i):
                            l[j],l[i]=l[i],l[j]
                    print l

                    re=''
                    for i in l:
                        re+=i
                    


                    t=Text(rd)
                    t.insert('1.0',re)
                    t.pack()
                    showinfo('Decryption','File Decrypted')
                    
            fns=e2.get()
            if os.path.isfile(path+'\\%s'%fns)==True:
                dencr()
            else:
                showerror('Error','No file To Encrypt')

                
        red=Tk()
        red.title('Open')
        red.geometry('700x150')
        red.resizable(0,0)
        lo=Label(red,text='Enter the file name\n(file should exist in C:\Docs)')
        lo.pack()
        lo.place(bordermode=OUTSIDE,x=100,y=20)
        e2=Entry(red)
        e2.pack()
        e2.place(bordermode=OUTSIDE,x=250,y=20,width=300)
        e2.focus()
        e2.bind('<Return>',(lambda event:opdenc()))
        bo=Button(red,text='Open',width=20,command=opdenc)
        bo.pack()
        bo.place(bordermode=OUTSIDE,x=370,y=70)

    def enc():

        def openc():
            def encr():
                if askquestion('Warning','Sure About Encrypting File')=='yes':
                    l=[]
                    fns=e2.get()
                    os.chdir(path)
                    f=open(fns,'r')
                    re=f.read()
                    print re
                    for let in re:
                        l.append(let)
                    print l
                    for i in range(len(l)-1):
                        for j in range(i):
                            l[i],l[j]=l[j],l[i]


                    f=open(fns,'w')
                    for i in l:
                        f.write(i)
                    f.close()
                    showinfo('Encryption','File Encrypted')
            fns=e2.get()
            if os.path.isfile(path+'\\%s'%fns)==True:
               encr()
            else:
                showerror('Error','No file To Encrypt')

                
        re=Tk()
        re.title('Open')
        re.geometry('700x150')
        re.resizable(0,0)
        lo=Label(re,text='Enter the file name\n(file should exist in C:\Docs)')
        lo.pack()
        lo.place(bordermode=OUTSIDE,x=100,y=20)
        e2=Entry(re)
        e2.pack()
        e2.place(bordermode=OUTSIDE,x=250,y=20,width=300)
        e2.focus()
        e2.bind('<Return>',(lambda event:openc()))
        bo=Button(re,text='Open',width=15,command=openc)
        bo.pack()
        bo.place(bordermode=OUTSIDE,x=380,y=70)
        
    def open_command():
        
        fil=tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if fil==None:
            ren=Tk()
            ren.destroy()
        elif fil!=None:
                contents=fil.read()
               
        ren=Tk()
        ren.title('%s'%fil)
        frame = Frame(ren, bd=2, relief=SUNKEN)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        frame.grid_propagate(True) # not neccessary if height and width of frame is not defined

        frame.pack(fill=BOTH,expand=True)

        xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=E+W)

        yscrollbar = Scrollbar(frame)
        yscrollbar.grid(row=0, column=1, sticky=N+S)

        text = Text(frame, wrap=NONE, bd=0,font=fnt,
                    xscrollcommand=xscrollbar.set,
                    yscrollcommand=yscrollbar.set)

        text.grid(row=0, column=0, sticky=N+S+E+W)

        xscrollbar.config(command=text.xview)
        yscrollbar.config(command=text.yview)

        frame.pack()
        menubar = Menu(ren)

        # Pulldown menues

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=open_command)
        filemenu.add_command(label="Save", command=save_command)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=ren.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        fontmenu=Menu(menubar,tearoff=0)
        fontmenu.add_command(label='Font',command=fon_t)
        fontmenu.add_command(label='Size',command=fsiz)
        menubar.add_cascade(label='Font',menu=fontmenu)

        text.insert('1.0',contents)
        fil.close()
        # dispay the menu
        ren.config(menu=menubar)
        
        ren.mainloop()

                
        


    def fsiz():
        rf = Tk()
        rf.title('Size')
        rf.geometry('250x450')
        rf.resizable(1,1)

        f2=Frame(rf)

        l=Label(rf,text='Text Size',font='btangche')

        bft=Button(rf,text='OK',width=15,command=rf.destroy)
        bft.pack()
        bft.place(bordermode=OUTSIDE,x=60,y=390)


        siz=Listbox(f2)
        siz.pack(fill=BOTH,expand=YES, side=LEFT)

        scrolf=Scrollbar(f2)
        scrolf.pack(fill=BOTH,side=RIGHT,expand=NO)

        scrolf.config(command=siz.yview)
        siz.config(yscrollcommand= scrolf.set)


        for item in sizes:
            siz.insert(END ,item)
            
                
        def selsiz (event):
            global fnt
            for i in siz.curselection():
                sval=siz.get(i)
                print sval
                l.config(text='Abcd',font=('',sval))
                text.config(font=('',sval))

            
        l.pack()
        l.place(bordermode=OUTSIDE,x=10,y=250)

        f2.pack()
        f2.place(bordermode=OUTSIDE, x=50,y=20)

        siz.bind('<<ListboxSelect>>',selsiz)

        rf.mainloop()


    def fon_t():
        rf = Tk()
        rf.title('Font')
        rf.geometry('180x258')
        rf.resizable(0,0)

        f=Frame(rf)

        l=Label(rf,height=2,width=40,text='Font',font='btangche')

        
        fonts=list(tkFont.families())
        fonts.sort()

        disfont = Listbox(f)
        disfont.pack(fill=BOTH, expand=YES, side=LEFT)

        scroll = Scrollbar(f)
        scroll.pack(side=RIGHT, fill=BOTH, expand=NO)

        scroll.configure(command=disfont.yview)
        disfont.configure(yscrollcommand=scroll.set)


        for item in fonts:
            disfont.insert(END, item)

        def selfon(evnt):
            for i in disfont.curselection():
                val=disfont.get(i)
                try:
                    l.config(text='Abcd',font=val)
                    text.config(font=val)
                except:
                    l.config(text='Font Unavailable',font='calibri')    

        l.pack()

        

        bft=Button(rf,text='OK',width=5,command=rf.destroy)
        bft.pack()
        bft.place(bordermode=OUTSIDE,x=65,y=218)

        disfont.bind('<<ListboxSelect>>',selfon)
        f.pack()
        rf.mainloop()
        



    def save_command():
              file=tkFileDialog.asksaveasfile(mode='w')
              if file !=None:
                        data=text.get('1.0',END+'-1c')
                        file.write(data)
                        file.close()
       

    frame = Frame(root, bd=2, relief=SUNKEN)

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    frame.grid_propagate(True) # not neccessary if height and width of frame is not defined

    frame.pack(fill=BOTH,expand=True)

    xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
    xscrollbar.grid(row=1, column=0, sticky=E+W)

    yscrollbar = Scrollbar(frame)
    yscrollbar.grid(row=0, column=1, sticky=N+S)

    text = Text(frame, wrap=NONE, bd=0,font=fnt,
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)

    text.grid(row=0, column=0, sticky=N+S+E+W)
    text.focus()

    xscrollbar.config(command=text.xview)
    yscrollbar.config(command=text.yview)

    frame.pack()
    menubar = Menu(root)

    # Pulldown menues

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=open_command)
    filemenu.add_command(label="Save", command=save_command)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)

    fontmenu=Menu(menubar,tearoff=0)
    fontmenu.add_command(label='Font',command=fon_t)
    fontmenu.add_command(label='Size',command=fsiz)
    menubar.add_cascade(label='Font',menu=fontmenu)

    enc_r=Menu(menubar,tearoff=0)
    enc_r.add_command(label='Encrypt',command=enc)
    enc_r.add_command(label='Decryption',command=denc)
    menubar.add_cascade(label='Encrytion',menu=enc_r)

    # dispay the menu
    root.config(menu=menubar)
    ret = text.get("1.0","end-1c")

    root.mainloop()


#Snake Game
def snake():
        pygame.init()
        white=(255,255,255)
        red=(255,0,0)
        black=(0,0,0)
        green=(0,255,0)
        blue=(0,0,255)
        yellow=(125,125,0)
        display_width=800
        display_height=600
        gameDisplay=pygame.display.set_mode((display_width,display_height))
        pygame.display.set_caption('SNAKE IMPACT')

        FPS=100

        block_size=10
        clock=pygame.time.Clock()
        font=pygame.font.SysFont(None,45)
        up='up'
        down='down'
        right='right'
        left='left'
        direction=right
        head=0
        def drawScore(score):
                  titleFont = pygame.font.Font('freesansbold.ttf',20)
                  scoreSurf = titleFont.render('Score: %s' % (score), True, red)
                  scoreRect = scoreSurf.get_rect()
                  scoreRect.topleft = (display_width - 160, 1)
                  gameDisplay.blit(scoreSurf, scoreRect)                   
        def showStartScreen():
               
                  x=0
                  c=0
                  degrees1 = 0
                  loopExit=False
                  while not loopExit:
                            if  c<100:
                                      x+=1
                                      c+=1
                            if c>=100:
                                      x-=1
                                      c+=1
                            if c==199:
                                      c=0
                            titleFont = pygame.font.Font('freesansbold.ttf',x)
                            titleSurf1 = titleFont.render('Snake', True,red)
                            gameDisplay.fill(green)
                            rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
                            rotatedRect1 = rotatedSurf1.get_rect()
                            rotatedRect1.center = (display_width / 2, display_height / 2)
                            gameDisplay.blit(rotatedSurf1, rotatedRect1)

                            pressKey=font.render('press a key to play',True,red)
                            gameDisplay.blit(pressKey,(display_width - 400, display_height - 40))
                            for event in pygame.event.get():
                                      if event.type==QUIT :
                                                pygame.quit()
                                      elif event.type==KEYDOWN:
                                                return

                            pygame.display.update()
                            clock.tick(FPS)
                            degrees1 += 7 # rotate by 7 degrees each frame
                            
        def snake(block_size,snakelist):

                  for XnY in snakelist:
                            
                            pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],10,10])
                  
        def message_to_screen(msg,color):
                  screen_text=font.render(msg,True,color)
                  gameDisplay.blit(screen_text,[display_width/2-350,display_height/2])
        def gameLoop():
                  gameExit=False
                  gameOver=False
                  lead_x=display_width/2
                  lead_y=display_height/2
                  lead_x_change=0
                  lead_y_change=0
                  snakelist=[]
                  snakelength=1
                  randAppleX=random.randrange(0,display_width-block_size)
                  randAppleY=random.randrange(0,display_height-block_size)
                  showStartScreen()
               
                  direction=right
                  score=0


                  while not gameExit:
                            while gameOver==True:
                                      gameDisplay.fill(blue)
                                      font=pygame.font.SysFont(None,150)
                                      pressKey=font.render('GAME OVER',True,red)
                                      gameDisplay.blit(pressKey,(display_width/2 - 250, display_height/2-200 ))
                                      font=pygame.font.SysFont(None,50)
                                      pressKey=font.render('PRESS c to continue or q to quit',True,red)
                                      gameDisplay.blit(pressKey,(display_width/2 - 200, display_height/2+100 ))
                                      pygame.display.update()
                                      if event.type==QUIT:
                                                pygame.quit()
                                                

                                      for event in pygame.event.get():
                                                if event.type==pygame.KEYDOWN:
                                                          if event.key==pygame.K_q:
                                                                    gameExit=True
                                                                    gameOver=False
                                                          if event.key==pygame.K_c:
                                                                    gameLoop()
                                                          
                          

                            for event in pygame.event.get():
                                      
                                      if event.type ==pygame.QUIT:
                                                gameExit =True
                                      if event.type==pygame.KEYDOWN:
                                                if event.key==pygame.K_LEFT and direction !=right:
                                                          direction=left
                                                          lead_x_change=-1
                                                          lead_y_change=0
                                                elif event.key==pygame.K_RIGHT and direction !=left:
                                                          direction=right
                                                          lead_x_change=1
                                                          lead_y_change=0
                                                elif event.key==pygame.K_UP and direction !=down:
                                                          direction=up
                                                          lead_y_change=-1
                                                          lead_x_change=0
                                                elif event.key==pygame.K_DOWN and direction !=up:
                                                          direction=down
                                                          lead_y_change=1
                                                          lead_x_change=0
                                                elif event.key==pygame.K_p:
                                                          d=0
                                                          while d==0:
                                                                    gameDisplay.fill(blue)
                                                                    message_to_screen("Game pause ,press r for resume",black)
                                                                    pygame.display.update()
                                                                    for event in pygame.event.get():
                                                                              if event.type==pygame.KEYDOWN:
                                                                                        if event.key==pygame.K_r:
                                                                                                  d=1
                                                                              elif event.type==QUIT:
                                                                                        pygame.quit()
                                                                                          
                                                          
                            for event in pygame.event.get():
                                      if event.type==QUIT :
                                                pygame.quit()                   
                            if lead_x>=display_width-10 or lead_x<=3 or lead_y>=display_height-10 or lead_y<=3:
                                      time.sleep(1)

                                      gameOver=True
                            lead_x+=lead_x_change
                            lead_y+=lead_y_change
                            
                            if (lead_x>randAppleX-10 and lead_x<randAppleX+block_size) and (lead_y>randAppleY-10 and lead_y<randAppleY+block_size):
                                      gameDisplay.fill(blue)
                                      randAppleX=random.randrange(0,display_width-block_size)
                                      randAppleY=random.randrange(0,display_height-block_size)
                                      snakelength=snakelength+10
                                      score+=1
                            gameDisplay.fill(yellow)
                            pygame.draw.rect(gameDisplay,black,[randAppleX,randAppleY,block_size,block_size])
                            snakehead=[]
                            snakehead.append(lead_x)
                            snakehead.append(lead_y)
                            snakelist.append(snakehead)
                            if len(snakelist)>snakelength:
                                      del snakelist[0]
                            for eachSegment in  snakelist[:-1]:
                                      if eachSegment==snakehead:
                                                time.sleep(1)
                                                gameOver=True
                  


                            snake(block_size,snakelist)
                            drawScore(score)                                                
                            pygame.display.update()
                            clock.tick(FPS)

                  pygame.quit()
                  
        gameLoop()

def developer():
    dev=Tk()
    dev.title('Developers')
    dev.config(bg='green')
    dev.geometry('400x130')
    devp=Label(dev,text='Pawan Lakhera:\n\nWelcome Window\nSnake\nMaps\nMain Window\nGmail',bg='green')
    devp.pack()
    devp.place(bordermode=OUTSIDE,x=70,y=5)
    devr=Label(dev,text='Raja Rahul Ray:\n\nFinMan(Finance Manager)\nNote Maker\nGoogle Search',bg='green')
    devr.pack()
    devr.place(bordermode=OUTSIDE,x=200,y=5)
    dev.mainloop()
          

#developer info.
def developer():
    dev=Tk()
    dev.title('Developers')
    dev.config(bg='green')
    dev.geometry('400x130')
    devp=Label(dev,text='Pawan Lakhera:\n\nWelcome Window\nSnake\nMaps\nMain Window\nGmail',bg='green')
    devp.pack()
    devp.place(bordermode=OUTSIDE,x=70,y=5)
    devr=Label(dev,text='Raja Rahul Ray:\n\nFinMan(Finance Manager)\nNote Maker\nGoogle Search',bg='green')
    devr.pack()
    devr.place(bordermode=OUTSIDE,x=200,y=5)
    dev.mainloop()

#google search          
def webopen():
    webbrowser.open('http://www.google.com/#q=%s'%entry.get());

#Maps..
def world_map():
          webbrowser.open ('http://www.mapsofworld.com/')
def India_map():
          webbrowser.open('http://www.mapsofindia.com/')

#gmail..
def gmail():
          webbrowser.open('https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1')

#Window to call Maps..
def maps():
    rm=Tk()
    rm.title('Maps')
    rm.geometry('350x130')
    rm.resizable(0,0)
    rm.config(bg='green')
    bm=Button(rm,text='India',command=India_map,width=25,bg='yellow',fg='dark blue')
    bm.pack()
    bm.place(bordermode=OUTSIDE,x=70,y=20)
    bm=Button(rm,text='World',command=world_map,width=25,bg='yellow',fg='dark blue')
    bm.pack()
    bm.place(bordermode=OUTSIDE,x=70,y=70)
#Title Screen
pygame.init()
FPS =30
WINDOWWIDTH = 1200
WINDOWHEIGHT = 1200
 # R G B
WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
DARKGREEN = ( 0, 155, 0)
DARKGRAY = ( 40, 40, 40)
BGCOLOR = BLACK
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


titleFont = pygame.font.Font('freesansbold.ttf', 100)
titleSurf1 = titleFont.render('M', True, WHITE, DARKGREEN)
titleSurf2 = titleFont.render('A', True, WHITE, DARKGREEN)
titleSurf3 = titleFont.render('P', True, WHITE, DARKGREEN)

degrees = 0
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption('MAP')
c=0
DISPLAYSURF.fill(DARKGREEN)

rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees)

while c<360:
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees)
        DISPLAYSURF.blit(rotatedSurf1,(400,200))
        degrees += 1 # rotate by 3 degrees each frame
        pygame.display.update()
        c+=1
        time.sleep(.0006)

c=0
pygame.draw.circle(DISPLAYSURF, WHITE, (550,280), 10, 0)
time.sleep(.08)


while c<360:
        rotatedSurf1 = pygame.transform.rotate(titleSurf2, degrees)
        DISPLAYSURF.blit(rotatedSurf1,(600,200))
        degrees += 1 # rotate by 3 degrees each frame
        pygame.display.update()
        c+=1
        time.sleep(.0006)
time.sleep(.08)
c=0
pygame.draw.circle(DISPLAYSURF, WHITE, (750,280), 10, 0)
while c<360:
        rotatedSurf1 = pygame.transform.rotate(titleSurf3, degrees)
        DISPLAYSURF.blit(rotatedSurf1,(800,200))
        degrees += 1 # rotate by 3 degrees each frame
        pygame.display.update()
        c+=1

pygame.draw.lines(DISPLAYSURF, WHITE, True, [(300,400),(950,400) ], 20)
pygame.display.update()
time.sleep(1)

titleFont = pygame.font.Font('freesansbold.ttf', 40)
titleSurf4= titleFont.render('Multiple  Application  Program', True, WHITE, DARKGREEN)
DISPLAYSURF.blit(titleSurf4,(300,500))
pygame.display.update()
time.sleep(1)
titleSurf5= titleFont.render('Credit: Pawan AND Raja', True, RED, DARKGREEN)
DISPLAYSURF.blit(titleSurf5,(25,30))
pygame.display.update()
time.sleep(3)
pygame.quit()

#Main Window
window=Tk()
window.title('M.A.P (Multiple Application Program)')
window.minsize(1200,1200)
window.maxsize(1600,1200)
window.config(bg='SystemHighlight')
label=Label(window,text='Google     Search',fg='red',font=20,bg='SystemHighlight')
label.place(x=580,y=170)
button=Button(window,text='offline games',height=10,width=20,bg='chartreuse',command=snake)
button.place(x=100,y=300)

button=Button(window,text='Maps',height=10,width=20,bg='khaki4',command=maps)
button.place(x=300,y=300)
button=Button(window,text='GMAIL',height=10,width=20,bg='magenta',command=gmail)
button.place(x=500,y=300)
button=Button(window,text='Note Maker',height=10,width=20,bg='OliveDrab4',command=Note_Maker)
button.place(x=700,y=300)
button=Button(window,text='Finance Manager',height=10,width=20,bg='yellow',command=FinMan)
button.place(x=900,y=300)

button=Button(window,text='Developers',width=15,bg='orange',command=developer)
button.pack()
button.place(bordermode=OUTSIDE,x=800,y=5)
entry=Entry(window,width=50,bg='cyan')
entry.focus()
entry.bind('<Return>',(lambda event:webopen()))
entry.place(x=500,y=200)


window.mainloop()
