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
    num_fact = e_num_fact.get();
    date_fact = e_date_fact.get();

       


    if(num_fact=="" or date_fact=="" ):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        
        cursor.execute("insert into bonEntre (date_bon  ,num_fact ,date_fact ) values( CURRENT_TIMESTAMP ,'"+ num_fact +"','"+ date_fact +"')")
        cursor.execute("commit");
      
        e_date_fact.delete(0, 'end')
        e_num_fact.delete(0, 'end')
        command = "/home/pi/Desktop/magasine/matiere_premiaire/mat.sh"
        subprocess.Popen(command)
        sys.exit()
       
     
        #MessageBox.showinfo("insert status", "Inserted successfully");
        con.close();
        

root = Tk()
root.geometry("1920x1080")
root.title("bon_d'entre")


           
NOM = Label(root,text='Numero de la facture ',font=('bold', 10))
NOM.place(x=20,y=60)
             
PRENOM = Label(root,text='date de la facture',font=('bold', 10))
PRENOM.place(x=20,y=90);




e_num_fact = Entry()
e_num_fact.place(x=200, y=60)             

e_date_fact = Entry()
e_date_fact.place(x=200, y=90)




insert = Button(root, text="suivant", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=350)


bouton_terminer = Button(root, text = 'Retour',  font=("italic", 10), bg="white", command = root.destroy)
bouton_terminer.place(x=100, y=350)



    
root.mainloop()

