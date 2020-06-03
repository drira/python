 

from tkinter import *

from tkinter.ttk import *

import tkinter.messagebox as MessageBox

import mysql.connector as mysql

import sys

import traceback

 

fenetre = Tk()
fenetre.geometry("1920x1080")

fenetre.title('matierePremiere')

#libelle = Label(fenetre, text = '******')

#libelle.pack(padx = 10, pady = 10)

 
tableau = Treeview(fenetre, columns=('CIN','REF_Prod', 'Qte_c'), show = 'headings')

tableau.heading('CIN', text='CIN')

tableau.heading('REF_Prod', text='REF_Prod ')

tableau.heading('Qte_c', text='Qte_c')



tableau['show'] = 'headings' 
con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
cursor = con.cursor()
cursor.execute('select * from commande where etat ="0" ')      
rows = cursor.fetchall()
        
for row in rows:  
    tableau.insert('', 'end', iid=row, values=(row[3], row[1], row[2]))


con.close();

tableau.pack(padx = 25, pady = (0, 25))

 
bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)

bouton_terminer.pack(padx = 25, pady = (0, 25))
def fenetrefn():
      CIN = e_CIN.get()
      PASSE = e_PASSE.get()
      

      if(CIN=="" or PASSE=="" ):
         MessageBox.showinfo("Insert Status", "All Fields are required")
  
      else:
          con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")      
          cursor = con.cursor()
          cursorUpdate = con.cursor()
          cursorlogout = con.cursor()
          cursorDelete = con.cursor()
          cursor.execute('select * from persons where CIN = %s AND PASSE = %s', (CIN,PASSE,))
          account = cursor.fetchone()
        
          if account :
             PASSE = account[9] 
             CIN = account[3]
             POSTE=account[8]
 
             if account[8] == 'Employe':
                  
                       
                  cursorVERIF = con.cursor() 
                  cursorVERIF.execute("select * from commande join (fabrication,matierePremiere) on( commande.REF_prod=fabrication.REF_prod and fabrication.REF_mat=matierePremiere.REF_mat) where etat =0 and cin ='"+str(CIN)+"'")      
                  rows1 = cursorVERIF.fetchall()
                
                  for row1 in rows1:
                
                      a = int(row1[12]) - (int(row1[2])*int(row1[9]))
                      cursorDelete.execute("update matierePremiere set QTE_mat ="+str(a)+" where REf_mat='"+str(row1[11])+"'")
                  
                  cursorUpdate.execute('update commande set etat =1 where cin ="'+str(CIN)+'"')
                  cursorUpdate.execute("commit");  
                  cursorlogout.execute('Delete  from Logging where cin ="'+str(CIN)+'"')
                  cursorlogout.execute("commit");       
          else:
               MessageBox.showinfo("insert status","CIN ou le Mot de passe est incorrect ");
               
          con.close();     




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


e_CIN= Entry(fenetre,textvariable=a)
e_CIN.place(x=141, y=292, width=297, height=41)
e_CIN.insert(0,"Entrez votre CIN")
e_CIN.bind("<Button>",userText)

#e_PASSE = Entry(show='*')
#e_PASSE.place(x=141, y=361, width=297, height=41)             
e_PASSE= Entry(fenetre,textvariable=b, show='*')
e_PASSE.place(x=141, y=361, width=297, height=41) 
e_PASSE.insert(0,"Enterez votre mot de passe")
e_PASSE.bind("<Button>",passText)

fenetre = Button(fenetre, text="valider", command=fenetrefn)
fenetre.place(x=196, y=450)

fenetre.mainloop()
