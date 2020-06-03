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
    ref_mat = e_ref_mat.get();
    qte_mat = e_qte_mat.get();
    design_mat = e_design_mat.get()
    emp_mat = e_emp_mat.get()
   

    if(ref_mat=="" or qte_mat=="" or design_mat=="" or emp_mat=="" ):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        up = con.cursor()
        ins = con.cursor()
        coh = con.cursor()
        cursor.execute ("select * from matierePremiere where ref_mat="+ref_mat+";");
        account = cursor.fetchone()
        if account :
            up.execute( "UPDATE matierePremiere SET QTE_mat = qte_mat +"+qte_mat+" WHERE ref_mat='"+e_ref_mat.get()+"';" )
        else :
            ins.execute("insert into matierePremiere (REf_mat ,QTE_mat , Design_mat , Emp_mat ) values('"+ ref_mat +"','"+ qte_mat +"','"+ design_mat +"','"+ emp_mat +"')")
            coh.execute("update bonEntre set ref_mat='"+ref_mat+"' where ref_mat=NULL")
        cursor.execute("commit");
        up.execute("commit");
        ins.execute("commit");
        
        e_ref_mat.delete(0, 'end')
        e_qte_mat.delete(0, 'end')
        e_design_mat.delete(0, 'end')
        e_emp_mat.delete(0, 'end')
      
        MessageBox.showinfo("insert status", "Inserted successfully");
        insert.configure(state="disabled")        
        get.configure(state="normal")          
        con.close();
def get():    
    if(e_ref_mat.get() == ""):
         MessageBox.showinfo("Fetch Status", "entre la referance de la matiere premiere")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        cursor.execute("select * from matierePremiere where ref_mat='"+ e_ref_mat.get() +"'")
        rows = cursor.fetchall()
        e_design_mat.delete(0, 'end')
        e_emp_mat.delete(0, 'end')
        
        for row in rows:
            e_design_mat.insert(0, row[2])
            e_emp_mat.insert(0, row[3])
        con.close();
        
        get.configure(state="disabled")        
        insert.configure(state="normal")       

root = Tk()
root.geometry("1920x1080")
root.title("matiere_premiere")


           
ref_mat = Label(root,text='Referance',font=('bold', 10))
ref_mat.place(x=20,y=60)
             
qte_mat = Label(root,text='Quantité',font=('bold', 10))
qte_mat.place(x=20,y=90);

design_mat = Label(root,text='Designation',font=('bold', 10))
design_mat.place(x=20,y=120);

emp_mat = Label(root,text='Emplacement',font=('bold', 10))
emp_mat.place(x=20,y=150)


get = Button(root, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=400,y=60)


e_ref_mat = Entry()
e_ref_mat.place(x=200, y=60)             

e_qte_mat = Entry()
e_qte_mat.place(x=200, y=90)

e_design_mat = Entry()
e_design_mat.place(x=200, y=120)

e_emp_mat = Entry()
e_emp_mat.place(x=200, y=150)




insert = Button(root, text="ajouter", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=350)

insert.configure(state="disabled")        

bouton_terminer = Button(root, text = 'Terminer', command = root.destroy)

bouton_terminer.place(x=100, y=350)



    
root.mainloop()

