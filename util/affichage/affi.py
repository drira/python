 

from tkinter import *

from tkinter.ttk import *
#from tkinter import ttk
import tkinter.messagebox as MessageBox

import mysql.connector as mysql

import sys

import traceback

 

fenetre = Tk()
fenetre.geometry("1920x1080")

fenetre.title('Person')

#libelle = Label(fenetre, text = '******')

#libelle.pack(padx = 10, pady = 10)

 
tableau = Treeview(fenetre, columns=('ID','NOM', 'PRENOM', 'CIN', 'DATE' ,'ADRESSE' ,'PORTABLE' ,'MAIL' ,'POSTE' ,'MOT_DE_PASSE'))

#'scroll = ttk.Scrollbar(fenetre, orient="vertical", command=tableau.yview)
#scroll.place (x=1165, y=22, width=20, height=200)
#tableau.configure (yscrollcommand=scroll.set)
#scroll = ttk.Scrollbar(fenetre, orient="horizontal", command=tableau.yview)
#scroll.place (x=100, y=22, width=1900, height=20)
#tableau.configure (yscrollcommand=scroll.set)#
tableau.column('ID', width=50, minwidth=50)

tableau.column('NOM', width=90, minwidth=90)

tableau.column('PRENOM', width=90, minwidth=90)

tableau.column('CIN', width=80, minwidth=80)

tableau.column('DATE', width=100, minwidth=100)

tableau.column('ADRESSE', width=150, minwidth=150)

tableau.column('PORTABLE', width=100, minwidth=100)

tableau.column('MAIL', width=200, minwidth=200)

tableau.column('POSTE', width=100, minwidth=100)

tableau.column('MOT_DE_PASSE', width=150, minwidth=150)


tableau.heading('ID', text='ID')

tableau.heading('NOM', text='NOM ')

tableau.heading('PRENOM', text='PRENOM')

tableau.heading('CIN', text='CIN')

tableau.heading('DATE', text='DATE')

tableau.heading('ADRESSE', text='ADRESSE')

tableau.heading('PORTABLE', text='PORTABLE')

tableau.heading('MAIL', text='MAIL')

tableau.heading('POSTE', text='POSTE')

tableau.heading('MOT_DE_PASSE', text='MOT_DE_PASSE')

tableau['show'] = 'headings' 

con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
cursor = con.cursor()
cursor.execute("select * from persons ")      
rows = cursor.fetchall()
        
for row in rows:  
    tableau.insert('', 'end', iid=row, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))


con.close();

tableau.pack(padx = 10, pady = (0, 10))

 
bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)

bouton_terminer.pack(padx = 10, pady = (0, 10))

#tableau.item(tableau.selection())['values']
#def selectedElement (event) :
#    select=tableau.item(tableau.selection())['values']
#    print(select)
#Bselect=Button(fenetre,text="élément sélectionné")
#Bselect.place (x=50, y=220)
#Bselect.bind ("<Button−1>" , selectedElement)

fenetre.mainloop()