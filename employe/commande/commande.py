from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter  as tk
from tkinter import ttk 

import os
import subprocess
import sys
import traceback

from datetime import datetime 
counter = -3600
running = False
time=""
idd=""

def insert():
    global idd
    Ref_prod= e_Ref_prod.get()
    Qte_c= e_Qte_c.get()
   

    if(Ref_prod=="" or Qte_c=="" ):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        up = con.cursor()
        ins = con.cursor()
        cursorSession =con.cursor()
        cursorVERIF = con.cursor()
        cursorSession.execute("select cin from Logging")
        session=cursorSession.fetchall()
        row =session[0]
        cursorVERIF.execute("select * from produit join (fabrication,matierePremiere) on( produit.REF_prod=fabrication.REF_prod and fabrication.REF_mat=matierePremiere.REF_mat) where produit.REF_prod='"+ e_Ref_prod.get()+"'")      
        rows1 = cursorVERIF.fetchall()
        a = True
        for row1 in rows1:
            if (int(row1[4])*int(e_Qte_c.get()) )> int(row1[7]):
                a = False
                break
        
        print(a)
        if a == True:
            ins.execute("insert into commande (Ref_prod, Qte_c,cin,BONNE,REJETER,ETAT,date,time) values('"+ Ref_prod+"','"+ Qte_c+"','"+ str(row[0])+"',NULL,NULL,0,CURRENT_TIMESTAMP,NULL)")
            cursor.execute("commit");
            up.execute("commit");
            ins.execute("commit");
            cursor.execute("select max(id_c) from commande")  
            #e_Ref_prod.delete(0, 'end')
            #e_Qte_c.delete(0, 'end')
            rows5 = cursor.fetchall()
            for row5 in rows5:
                idd =row5[0]
            print(idd)
            MessageBox.showinfo(" commande "," Vous avez commander : "+ e_Qte_c.get() +" "+ e_Ref_prod.get());
            insert.configure(state="disabled")        
            get.configure(state="normal")
        else:
            MessageBox.showinfo(" commande "," insuffisant");
        con.close();


    
def get():    
    if(e_Ref_prod.get() == ""):
       MessageBox.showinfo("Fetch Status", "Entré la Référance du produit")

        
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        cursor.execute("select * from produit where Ref_prod='"+ e_Ref_prod.get() +"'")
        
        rows = cursor.fetchall()
        
        for row in rows:
            if row[0] != "": # e_Qte_c.delete(0, 'end')
        
                get.configure(state="disabled")        
                insert.configure(state="normal")
                
            else:  
                get.configure(state="normal")        
                insert.configure(state="disabled")
            

    
def etat():
    BONNE= e_BONNE.get()
    REJETER= e_REJETER.get()
   

    if(BONNE=="" or REJETER=="" ):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        up = con.cursor()
        ins = con.cursor()
        if int(e_Qte_c.get()) == int(e_BONNE.get())+int(e_REJETER.get()):
            ins.execute("update commande set BONNE='"+ BONNE +"',REJETER='"+ REJETER +"'where id_c='"+ str(idd)+"' and etat=1 ")
            cursor.execute("commit");
            up.execute("commit");
            ins.execute("commit");
            MessageBox.showinfo("validation" , e_BONNE.get() + " piéces valider et : "+ e_REJETER.get() +" Rejeter ");
        else:
            MessageBox.showinfo("erreur" ,"valider vos données");
        con.close();
        
        


def counter_label(label):  
    def count():  
        if running:  
            global counter  
            global time
            # To manage the intial delay.  
            if counter== -3600:              
                display="Starting..."
            else: 
                tt = datetime.fromtimestamp(counter) 
                string = tt.strftime("%H:%M:%S") 
                display=string
                time=string
            label['text']=display   
            label.after(1000, count)   
            counter += 1
            
    
    # Triggering the start of the counter.  
    count()
    print(time)
    
# start function of the stopwatch  
def Start(label):  
    global running  
    running=True
    counter_label(label)  
    
    
# Stop function of the stopwatch  
def Stop():
    global running
    global time
    global idd
    running = False
    print(time)
    con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
    cursor = con.cursor()
    
    cursor.execute("update commande set time='"+ str(time) +"'where id_c='"+ str(idd)+"'")
    cursor.execute("commit");
    con.close();
    root.destroy()
    print(time)
    
root = Tk()

root.geometry("1920x1080")
root.title("Commande")


Ref_prod= Label(root,text='Réferance produit',font=('bold', 10))
Ref_prod.place(x=20,y=120);

Qte_c= Label(root,text='quantité',font=('bold', 10))
Qte_c.place(x=20,y=150)


get = Button(root, text="Rech", font=("italic", 10), bg="white", command=get)
get.place(x=400,y=120)



e_Ref_prod= Entry()
e_Ref_prod.place(x=200, y=120)

e_Qte_c= Entry()
e_Qte_c.place(x=200, y=150)




BONNE= Label(root,text='BONNE',font=('bold', 10))
BONNE.place(x=20,y=300)

REJETER= Label(root,text='REJETER',font=('bold', 10))
REJETER.place(x=20,y=350)

e_BONNE= Entry()
e_BONNE.place(x=200, y=300)

e_REJETER= Entry()
e_REJETER.place(x=200, y=350)

etat = Button(root, text="verifier", font=("italic", 10), bg="white", command=etat)
etat.place(x=20, y=400)






insert = Button(root, text="Commander", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=200)
insert.configure(state="disabled")


bouton_terminer = Button(root, text = 'Terminer', command = Stop )
bouton_terminer.place(x=1000, y=500)

# Fixing the window size.  
label = tk.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")  
label.pack()  
f = tk.Frame(root) 
Start(label)
#start = tk.Button(f, text='Start', width=6, command=lambda:Start(label))  
#stop = tk.Button(f, text='Stop',width=6,state='disabled', command=Stop)  
f.pack(anchor = 'center',pady=5) 


root.mainloop()







