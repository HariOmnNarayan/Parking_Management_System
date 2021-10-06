from tkinter import *
#import tkinter.messagebox
from tkinter import messagebox



#from tkinter import ttk
#from ttk import *

from tkinter.ttk import *

import sqlite3
con=sqlite3.Connection('hrdb')
rootp=Tk()
coordinate_value=500
giant=PhotoImage(file='bg3.png')
Label(rootp,text="PARKING MANAGEMENT SYSTEM",font="Bold 30",borderwidth=3, relief="flat",image=giant).pack()

def fun8():
    rootp.destroy()
    root2=Tk()
    root2.title("Welcome,Customer To our Cancellation System")
    Label(root2,text="Enter your license number").grid(row=0,column=0)
    e1=Entry(root2)
    e1.grid(row=0,column=1)

    def fun2():
        d=e1.get()
        #b=w2.get()
        #c=w3.get()
        #cur=con.cursor()
        x=str(d)
        #y=str(c)
        #con.commit()
        if d=='' :#or b=='' or c=='':
             messagebox.showerror("Oops","You can't Enter the leave  field empty")
        else:
             cur=con.cursor()   
             cur.execute("select places from login where license =(?)",(d,))
             y=cur.fetchone()
             print(str(y))
             
             #desc = cur.description[0]
             
             if str(y) != 'None' :
                pl=y[0]  
                cur.execute("update choose set alot = alot + 1 where places =(?)",(pl,))
                cur.execute("delete  from login where license=(?)",(x,))
                messagebox.showinfo("your reservation is cancelled")
                con.commit()
             else:
                messagebox.showerror("no such liscense")   
             
                          
            
    Bc=Button(root2,text="Cancel Reservation",command=fun2).grid(row=4,column=0)
    root2.mainloop()
########################
def fun9():
    rootp.destroy()
    root4=Tk()
    root4.title("Welcome,to increase time")
    Label(root4,text="Enter License number").grid(row=0,column=0)
    #w1=Combobox(root4,height=5,width=15,values=["New York","Chicago","Dallas","San Francisco"])
    w1=Entry(root4,width=20)
    w1.grid(row=0,column=1)
    Label(root4,text="time increse by(in min)").grid(row=1,column=0)
    w2=Entry(root4,width=20)#w2=Combobox(root4,height=5,width=15,values=["New York","Chicago","Dallas","San Francisco"])
    w2.grid(row=1,column=1)
    #Label(root4,text="Choose day of travel").grid(row=2,column=0)
    #w3=Combobox(root4,text="choose day",height=5,width=15,values=["sunday","monday","tuesday","wensday","thursday","friday","saturday"])
    #w3.grid(row=2,column=1)
    def fun10():
        a=w1.get()#lic
        b=w2.get()#time
        
        #c=w3.get()
        cur=con.cursor()
        if a=='' or b=='':# or c=='':
            messagebox.showerror("Error","Cant leave any field empty")
           
                
        else:
             b=int(b)/60
             #cur.execute("select places from login where license =(?)",(a,))
             #yo=cur.fetchmany(size=1)
             cur.execute("update login set time = time + (?) where license = (?) ",(b,a,))
             messagebox.showinfo("your time is increased")
             cur.execute("select * from login where license=(?)",(a,))
             messagebox.showinfo("records",cur.fetchall())
             con.commit()
    Bs=Button(root4,text="Done",command=fun10).grid(row=3,column=0)
    root4.mainloop()
###########3##########
def fun5():
    rootp.destroy()
    root=Tk()
    root.title('Parking Slot search And booking')

    

    Label(root,text="Enter Your Name").grid(row=1,column=0)
#e1=Entry(root,width=20,bd=4,justify="right")
#e1.grid(row=1,column=1)
    w=Entry(root,width=40)#w=Combobox(root,height=5,width=15,values=["Dallas","Washington","New York","San Francisco"])
    w.grid(row=1,column=1)
    Label(root,text='Enter Licencse Number').grid(row=2,column=0)
#e2=Entry(root,width=20,justify='right')
#e2.grid(row=2,column=1)
    w1=Entry(root,width=20)#Combobox(root,height=5,width=15,values=["Dallas","Washington","New York","San Francisco"])
    w1.grid(row=2,column=1)
#e3=Entry(root,width=20,justify='right')
#e3.grid(row=3,column=1)

    #Label(root,text='Enter last 4 digit of your Citizenship Number').grid(row=3,column=0)
    #e=Entry(root,width=20)
    #e.grid(row=3,column=1)
    w2=Combobox(root,text='Type OF vehicle',height=5,width=15,values=["Two Wheeler","Four Wheeler"])
    w2.grid(row=4,column=1)
    Label(root,text='Type OF vehicle').grid(row=4,column=0)
    Label(root,text="Choose Places To Park").grid(row=5,column=0)
    w3=Combobox(root,text="choose ",height=5,width=15,values=["Galeria Mall","Gas Station","ABC Apartment","Big Bazzar","Cinepolis","XYZ Hotel"])
    w3.grid(row=5,column=1)
    Label(root,text="Enter Hours To Park").grid(row=6,column=0)
    w4=Entry(root,width=5)
    w4.grid(row=6,column=1)
    def fun():
        a=w.get()#nmae
        b=w1.get()#lic
        d=w2.get()#tpe
        f=w3.get()#places
        g=w4.get()#hour
        
        if str(d) =='Two Wheeler':
           price = int(g)*60*2+10;
        else :
           price = int(g)*120+40;
        x=(a,b,f,g)
        cur=con.cursor()
        cur.execute("select alot  from choose where places=(?)",(f,)) 
        #desc = cur.description[0] 
        rows= cur.fetchone()
        print(rows)
        #messagebox.showinfo(FieldType.get_info(desc[0]))
        #z=int(rows)      
        if a=='' or b=='' or d=='' or f=='' or g=='':
            messagebox.showerror("OOPS","you can't leave any field empty")
        else : 
                g=int(g)*60       
                if int(rows[0])>0:#(desc[0])>0:#rows is not NONE:
                    #cur.execute("create table login(name char(40),license char(20),places char(40),time number)")
                    cur.execute("insert into login values(?,?,?,?)",x)
                    cur.execute("update choose set alot = alot - 1 where alot > 0 and places =(?) ",(f,))
                    messagebox.showinfo("Congrats","your parking has been reserved")
                    con.commit()
                    cur.execute("select * from login where license=(?)",(b,))
                    messagebox.showinfo("records",cur.fetchall())
                    messagebox.showinfo("price",price)
                    con.commit()
                else:
                    messagebox.showerror("SORRY ","Parking Alotment is Fulled !! choose someother place ")
    Bi=Button(root,text="BOOK NOW",command=fun).grid(row=7,column=1)
#Bo=Button(root,text="See Flights",command=dis).grid(row=7,column=1)
#Bf=Button(root,text='Set fair range',command=fun1).grid(row=7,column=2)
    root.mainloop()

##############################3
    


B3=Button(rootp,text="Book Parking Slot",command=fun5).pack()
B2=Button(rootp,text="Increse Parking Duration",command=fun9).pack()
B1=Button(rootp,text="Cancel Booking",command=fun8).pack()
#B2=Button(rootp,text="Cancel Booking",height=4,width=35,font="Bold",bg="gray").pack()
#B3=Button(rootp,text="See flights",height=4,width=35,font="Bold",bg="gray").pack()


rootp.mainloop()
    
