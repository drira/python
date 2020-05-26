from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

import os
import subprocess
import sys

log="bonjour"


def loginfn():
      CIN = e_CIN.get()
      PASSE = e_PASSE.get()
      

      if(CIN=="" or PASSE=="" ):
         MessageBox.showinfo("Insert Status", "All Fields are required")
  
      else:
          con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")      
          cursor = con.cursor()
          cursorInsert = con.cursor() 
          cursor.execute('select * from persons where CIN = %s AND PASSE = %s', (CIN,PASSE,))
          account = cursor.fetchone()
        
          if account :
             PASSE = account[9] 
             CIN = account[3]
             POSTE=account[8]
             
             #cursor.execute('INSERT INTO presence (ID_P, in, out) VALUES (selecet id from persons , sysdate , sysdate')
             #account =cursor.fetchone()
             
             
             if account[8] == 'Directeur':
             
             #MessageBox.showinfo("insert status","hello  ");
             #exec(open("/home/pi/Desktop/util/cbd.py").read())
             #subprocess.run(['ls','/home/pi/Desktop/util/cbd.sh'],shell=True)
                 command = "/home/pi/Desktop/util/pp/pp.sh"
                 subprocess.Popen(command)

             elif account[8] == 'Magasinier':
                  command = "/home/pi/Desktop/magasine/magasiner.sh"
                  subprocess.Popen(command)
                  #sys.exit()
             elif account[8] == 'Employe':
                  cursorInsert.execute("insert into Logging (cin) values( "+ str(CIN) +")")
                  cursorInsert.execute("commit");        
                  command = "/home/pi/Desktop/employe/employe.sh"
                  subprocess.Popen(command)
                  #sys.exit()


                  
                  
          else:
               MessageBox.showinfo("insert status","CIN ou le Mot de passe est incorrect ");
               
          con.close();     
               
login = Tk()
login.geometry("1190x560")
login.title("Login+password")
login.config(background='#7AB5DE')
login.resizable(False,False)

#creation image

width = 1200
height = 560
image = PhotoImage(file="/home/pi/Desktop/1icon/1/58.png").zoom(1).subsample(1)
canvas = Canvas(login, width=width, height=height, bd=0 ,highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(expand=YES)

#CIN = Label(login,text='CIN',font=('courrier', 15), bg='#18BF22', fg='white')
#CIN.place(x=250,y=110);
#CIN.pack(expand=YES)

#PASSE = Label(login,text='MOT DE PASSE',font=('courrier', 15), bg='#18BF22', fg='white')
#PASSE.place(x=250,y=190)

#v = StringVar(login, value='dd')
#e_CIN = Entry(textvariable=v ,width=36)

def userText(event):
    e_CIN.delete(0,END)
    usercheck=True

def passText(event):
    e_PASSE.delete(0, END)
    passcheck=True


a=StringVar()
b=StringVar()
usercheck=False
passcheck=False


e_CIN= Entry(login,textvariable=a)
e_CIN.place(x=141, y=292, width=297, height=41)
e_CIN.insert(0,"Entrez votre CIN")
e_CIN.bind("<Button>",userText)

#e_PASSE = Entry(show='*')
#e_PASSE.place(x=141, y=361, width=297, height=41)             
e_PASSE= Entry(login,textvariable=b, show='*')
e_PASSE.place(x=141, y=361, width=297, height=41) 
e_PASSE.insert(0,"Enterez votre mot de passe")
e_PASSE.bind("<Button>",passText)



login = Button(login, text="Connexion", font=("courrier", 15), bg="white",fg='#1A2A3F', command=loginfn)
login.place(x=196, y=450)


login.mainloop()




