from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

import subprocess



def loginfn():
   
    CIN = e_CIN.get()
    PASSE = e_PASSE.get()

    if(CIN=="" or PASSE==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        cursor.execute("select * from persons where CIN='"+ e_CIN.get() +"'")
        account = cursor.fetchone()
        
        if account  :
            
                
            if  account[8] == PASSE  and account[3] == CIN : 
                print(account)
                   # subprocess.call("cbd.py")
                MessageBox.showinfo("insert status","hello  ");
                    
            else:
                e_CIN.delete(0, 'end')
                e_PASSE.delete(0, 'end')
                MessageBox.showinfo("insert status", "Access denied ");
                    
        else:
            e_CIN.delete(0, 'end')
            e_PASSE.delete(0, 'end')
            MessageBox.showinfo("insert status", "Accessssssssssss denied ");
        
               
           
                    
        con.close();
 
login = Tk()
login.geometry("700x700")
login.title("python+Tkinter+MySql")



CIN = Label(login,text='CIN',font=('bold', 10))
CIN.place(x=250,y=120);



PASSE = Label(login,text='MOT DE PASSE',font=('bold', 10))
PASSE.place(x=250,y=190)




e_CIN = Entry()
e_CIN.place(x=250, y=150)

e_PASSE = Entry( show='*')
e_PASSE.place(x=250, y=230)             





signin = Button(login, text="SignIn", font=("italic", 10), bg="white", command=loginfn)
signin.place(x=250, y=300)




    
login.mainloop()


