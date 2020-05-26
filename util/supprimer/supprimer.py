from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter  as tk
from tkinter import ttk 

import os
import subprocess
import sys


def insert():
    #ID = e_ID.get()
    NOM = e_NOM.get();
    PRENOM = e_PRENOM.get();
    CIN = e_CIN.get()
    DATE = e_DATE.get()
    ADRESSE = e_ADRESSE.get()
    PORTABLE = e_PORTABLE.get()
    MAIL = e_MAIL.get()
    POSTE = listeCombo.get()
    PASSE = e_PASSE.get()
   # ID=="" or   '"+ ID +"',

    if(NOM=="" or PRENOM=="" or CIN=="" or DATE=="" or ADRESSE=="" or PORTABLE=="" or MAIL=="" or PASSE==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        
        cursor.execute("insert into persons (NOM ,PRENOM , CIN , DATE ,ADRESSE ,PORTABLE ,MAIL ,POSTE ,PASSE ) values('"+ NOM +"','"+ PRENOM +"','"+ CIN +"','"+ DATE +"','"+ ADRESSE +"','"+ PORTABLE +"','"+ MAIL +"','"+ POSTE +"','"+ PASSE +"')")
        cursor.execute("commit");
        
        #e_ID.delete(0, 'end')
        e_NOM.delete(0, 'end')
        e_PRENOM.delete(0, 'end')
        e_CIN.delete(0, 'end')
        e_DATE.delete(0, 'end')
        e_ADRESSE.delete(0, 'end')
        e_PORTABLE.delete(0, 'end')
        e_MAIL.delete(0, 'end')
        listeCombo.delete(0, 'end')        
        e_PASSE.delete(0, 'end')
     
        show()
        MessageBox.showinfo("insert status", "Inserted successfully");
        con.close();
        
        
def delete():
    if(NOM=="" or PRENOM==""  or CIN=="" or DATE=="" or ADRESSE=="" or PORTABLE=="" or MAIL=="" or PASSE=="" ):
         MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        cursor.execute("Delete from persons where CIN='"+ e_CIN.get() +"'")
        cursor.execute("commit");
       # e_ID.delete(0, 'end')
        e_NOM.delete(0, 'end')
        e_PRENOM.delete(0, 'end')
        e_CIN.delete(0, 'end')
        e_DATE.delete(0, 'end')
        e_ADRESSE.delete(0, 'end')
        e_PORTABLE.delete(0, 'end')
        e_MAIL.delete(0, 'end')
        listeCombo.delete(0, 'end')        
        e_PASSE.delete(0, 'end')

        
        MessageBox.showinfo("Delete status", "Deleteted successfully");
        con.close();

        
def get():    
    if(e_RECH.get() == ""):
         MessageBox.showinfo("Fetch Status", "CIN is compolsary for delete")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        cursor.execute("select * from persons where CIN='"+ e_RECH.get() +"'")
        rows = cursor.fetchall()
        
        for row in rows:
            e_NOM.insert(0, row[1])
            e_PRENOM.insert(0, row[2])
            e_CIN.insert(0, row[3])
            e_DATE.insert(0, row[4])
            e_ADRESSE.insert(0, row[5])
            e_PORTABLE.insert(0, row[6])
            e_MAIL.insert(0, row[7])
            listeCombo.insert(0 ,row[8])
            e_PASSE.insert(0, row[9])
            
            
            
            
        con.close();
        
        
        get.configure(state="disabled")
        

    
root = Tk()
root.geometry("1920x1080")
root.title("supprimer")




           
NOM = Label(root,text='NOM',font=('bold', 10))
NOM.place(x=20,y=60)
             
PRENOM = Label(root,text='PRENOM',font=('bold', 10))
PRENOM.place(x=20,y=90);

CIN = Label(root,text='CIN',font=('bold', 10))
CIN.place(x=20,y=120);

DATE = Label(root,text='DATE DE NAISSANCE',font=('bold', 10))
DATE.place(x=20,y=150)

ADRESSE = Label(root,text='ADRESSE',font=('bold', 10))
ADRESSE.place(x=20,y=180)

PORTABLE = Label(root,text='N PORTABLE',font=('bold', 10))
PORTABLE.place(x=20,y=210)

MAIL = Label(root,text='E MAIL',font=('bold', 10))
MAIL.place(x=20,y=240)

PASSE = Label(root,text='MOT DE PASSE',font=('bold', 10))
PASSE.place(x=20,y=270)

post= Label(root,text='POSTE',font=('bold', 10))
post.place(x=20,y=300)




e_RECH = Entry()
e_RECH.place(x=400, y=30)

e_NOM = Entry()
e_NOM.place(x=170, y=60)             

e_PRENOM = Entry()
e_PRENOM.place(x=170, y=90)

e_CIN = Entry()
e_CIN.place(x=170, y=120)

e_DATE = Entry()
e_DATE.place(x=170, y=150)

e_ADRESSE = Entry()
e_ADRESSE.place(x=170, y=180)

e_PORTABLE = Entry()
e_PORTABLE.place(x=170, y=210)

e_MAIL = Entry()
e_MAIL.place(x=170, y=240)

e_PASSE = Entry()
e_PASSE.place(x=170, y=270)


listeProduits=["","Directeur","Employe","Magasinier"]
listeCombo = ttk.Combobox(root, values=listeProduits)
listeCombo.current(0)
listeCombo.pack()
listeCombo.place(x=170, y=300)



delete = Button(root, text="Delete", font=("italic", 10), bg="white", command=delete)
delete.place(x=20, y=350)



get = Button(root, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=570,y=30)

bouton_terminer = Button(root, text = 'Terminer', command = root.destroy)

bouton_terminer.place(x=100, y=350)

   
root.mainloop()

