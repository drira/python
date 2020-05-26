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
          #con = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
          #con.execute('SELECT * FROM PERSONS WHERE CIN = %s AND PASSE = %s', (CIN,PASSE,))
          cursor = con.cursor()
          cursor.execute('select * from persons where CIN = %s AND PASSE = %s', (CIN,PASSE,))
          account = cursor.fetchone()
        
          if account :
             PASSE = account[8] 
             CIN = account[3]
             MessageBox.showinfo("insert status","hello  ");
          else:
              MessageBox.showinfo("insert status","no  ");
                
 
login = Tk()
login.geometry("700x700")
login.title("python+Tkinter+MySql")
#login.iconbitmap(" /home/pi/Desktop/util/b.ico")
login.config(background='#7AB5DE')


CIN = Label(login,text='CIN',font=('courrier', 15))
CIN.place(x=250,y=120);



PASSE = Label(login,text='MOT DE PASSE',font=('bold', 10))
PASSE.place(x=250,y=190)




e_CIN = Entry()
e_CIN.place(x=250, y=150)

e_PASSE = Entry( show='*')
e_PASSE.place(x=250, y=230)             





login = Button(login, text="SignIn", font=("italic", 10), bg="white", command=loginfn)
login.place(x=250, y=300)

photo = PhotoImage(file="/home/pi/Téléchargements/0.png")
canvas = Canvas(login,width=300, height=200)
canvas.create_image(10, 20, anchor=NW, image=photo)
canvas.pack()
    

login.mainloop()

