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
    Ref_prod= e_Ref_prod.get()
    design_prod= e_design_prod.get()
   

    if(Ref_prod=="" or design_prod=="" ):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        up = con.cursor()
        ins = con.cursor()
        ins.execute("insert into produit (Ref_prod, design_prod) values('"+ Ref_prod+"','"+ design_prod+"')")
        cursor.execute("commit");
        up.execute("commit");
        ins.execute("commit");
        #e_Ref_prod.delete(0, 'end')
        #e_design_prod.delete(0, 'end')
      
        MessageBox.showinfo("nouveau produit ", e_design_prod.get() + " est le porduit ajouter avec une référance : " + e_Ref_prod.get());
        insert.configure(state="disabled")        
        get.configure(state="normal")
        intt.configure(state="disabled")        

        con.close();
        
def get():    
    if(e_Ref_prod.get() == ""):
       MessageBox.showinfo("Fetch Status", "Entré la Référance du produit")

        
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        cursor.execute("select * from produit where Ref_prod='"+ e_Ref_prod.get() +"'")
        rows = cursor.fetchall()
       # e_Design_prod.delete(0, 'end')
        
        for row in rows:
            e_design_prod.insert(0, row[1])
        con.close();
        
        get.configure(state="disabled")        
        insert.configure(state="normal")
        intt.configure(state="disabled")        


        
def mat():    
    if(e_Ref_prod.get() == ""):
       MessageBox.showinfo("Fetch Status", "Entrer la Référance de la matiere premiere")

        
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        cursor.execute("select * from matierePremiere where REF_mat='"+ e_REF_mat.get() +"'")
        rows = cursor.fetchall()
       # e_Design_prod.delete(0, 'end')
        
       # for row in rows:
      #      e_design_prod.insert(0, row[1])
        con.close();
        
        mat.configure(state="disabled")        
        intt.configure(state="normal")     



def intt():
    REF_mat= e_REF_mat.get()
    
    prod= e_Ref_prod.get()
    
    QTE_mp= e_QTE_mp.get()
    
   

    if(QTE_mp=="" ):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        up = con.cursor()
        ins = con.cursor()
        ins.execute("insert into fabrication (REF_mat, REF_prod , QTE_mp) values( '"+REF_mat +"','"+ prod +"' ,"+ QTE_mp +")")
        cursor.execute("commit");
        up.execute("commit");
        ins.execute("commit");
        MessageBox.showinfo("insert status", "produit ajouter",);

        e_REF_mat.delete(0, 'end')
        e_QTE_mp.delete(0, 'end')
      
        intt.configure(state="disabled")        
        mat.configure(state="normal")
        #update matierePremiere set qte_mat=qte_mat-qte_mp where ref_mat=REF_mat;
        con.close();
"""
def show():
    con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
    cursor = con.cursor()
    cursor.execute("select * from fabrication ")
    row = cursor.fetchall()
    list.delete(0, list.size())
    
    for row in rows:
        insertData = str (row[0])+row[1]+row[2]
        list.insert(list.size()+1 ,insertData)
    con.close();
    
 """   

root = Tk()
root.geometry("1920x1080")
root.title("matiere_premiere")



mat = Button(root, text="rech", font=("italic", 10), bg="white", command=mat)
mat.place(x=600,y=400)
Ref_mat= Label(root,text='Réferance matiere',font=('bold', 10))
Ref_mat.place(x=20,y=400);           
e_REF_mat= Entry()
e_REF_mat.place(x=180, y=400)


intt = Button(root, text="+", font=("italic", 10), bg="white", command=intt)
intt.place(x=600,y=450)
intt.configure(state="disabled")

QTE_mp= Label(root,text='Quantité',font=('bold', 10))
QTE_mp.place(x=20,y=450);           
e_QTE_mp= Entry()
e_QTE_mp.place(x=180, y=450)



Ref_prod= Label(root,text='Réferance produit',font=('bold', 10))
Ref_prod.place(x=20,y=120);

design_prod= Label(root,text='Designation',font=('bold', 10))
design_prod.place(x=20,y=150)


get = Button(root, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=400,y=120)



e_Ref_prod= Entry()
e_Ref_prod.place(x=200, y=120)

e_design_prod= Entry()
e_design_prod.place(x=200, y=150)




insert = Button(root, text="ajouter", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=200)

insert.configure(state="disabled")

def affip():
    command = "/home/pi/Desktop/magasine/fabrication/aff.sh"
    #command2 = "/home/pi/Desktop/util/cbd.sh"
    subprocess.Popen(command)
    #subprocess.kill()
    
affip = Button(root, text="Afficher ", font=("calibri", 17), bg='#E9E9E9',fg='#24627A', command=affip)
affip.place(x=1000, y=398)

bouton_terminer = Button(root, text = 'Terminer', command = root.destroy)
bouton_terminer.place(x=1000, y=500)
"""
list = Listbox(root)
list.place(x=500 , y=30)

show()
"""    
root.mainloop()


