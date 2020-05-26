from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter  as tk
from tkinter import ttk 

import os
import subprocess
import sys
import traceback

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
        

root = Tk()
root.geometry("1190x560")
root.title("ajouter")

width = 1200
height = 560
image = PhotoImage(file="/home/pi/Desktop/util/ajouter/4.png").zoom(1).subsample(1)
canvas = Canvas(root, width=width, height=height, bd=0 ,highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(expand=YES)

           
NOM = Label(root,text='NOM',font=('calibri', 15), bg='#FFFFFF',fg='#000000')
NOM.place(x=40,y=60)
         
PRENOM = Label(root,text='PRENOM',font=('calibri', 15))
PRENOM.place(x=500,y=60);

CIN = Label(root,text='CIN',font=('calibri', 15))
CIN.place(x=40,y=140);

DATE = Label(root,text='DATE DE NAISSANCE',font=('calibri', 15))
DATE.place(x=500,y=140)

ADRESSE = Label(root,text='ADRESSE',font=('calibri', 15))
ADRESSE.place(x=40,y=220)

PORTABLE = Label(root,text='N PORTABLE',font=('calibri', 15))
PORTABLE.place(x=500,y=220)

MAIL = Label(root,text='E MAIL',font=('calibri', 15))
MAIL.place(x=40,y=300)

PASSE = Label(root,text='MOT DE PASSE',font=('calibri', 15))
PASSE.place(x=500,y=300)

post= Label(root,text='POSTE',font=('calibri', 15))
post.place(x=40,y=380)



e_NOM = Entry()
e_NOM.place(x=40, y=85, width=280, height=35)             

e_PRENOM = Entry()
e_PRENOM.place(x=500, y=85, width=280, height=35)

e_CIN = Entry()
e_CIN.place(x=40, y=165, width=280, height=35)

e_DATE = Entry()
e_DATE.place(x=500, y=165, width=280, height=35)

e_ADRESSE = Entry()
e_ADRESSE.place(x=40, y=245, width=280, height=35)

e_PORTABLE = Entry()
e_PORTABLE.place(x=500, y=245, width=280, height=35)

e_MAIL = Entry()
e_MAIL.place(x=40, y=325, width=280, height=35)

e_PASSE = Entry()
e_PASSE.place(x=500, y=325, width=280, height=35)


listeProduits=["","Directeur","Employe","Magasinier"]
listeCombo = ttk.Combobox(root, values=listeProduits)
listeCombo.current(0)
listeCombo.pack()
listeCombo.place(x=40, y=405, width=280, height=35)


insert = Button(root, text="Ajouter", font=("italic", 10), bg="white", command=insert)
insert.place(x=500, y=390, width=280, height=35)

bouton_terminer = Button(root, text = 'Retour', bg="white",command = root.destroy)

bouton_terminer.place(x=500, y=440, width=280, height=35)



    
root.mainloop()

