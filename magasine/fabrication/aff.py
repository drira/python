 

from tkinter import *

from tkinter.ttk import *

import tkinter.messagebox as MessageBox

import mysql.connector as mysql

import sys

import traceback

 

fenetre = Tk()
fenetre.geometry("1920x1080")

fenetre.title('affichage d un produit')

#libelle = Label(fenetre, text = '******')

#libelle.pack(padx = 10, pady = 10)
#        cursor.execute("select (Ref_prod, design_prod) from fabrication where Ref_prod='"+ Ref_prod+"' group by Ref_prod")

 
tableau = Treeview(fenetre, columns=('Referance_prod', 'Referance_mat', 'Quantite' ), show = 'headings')

tableau.heading('Referance_prod', text='Referance_prod')


tableau.heading('Referance_mat', text='Referance_mat')


tableau.heading('Quantite', text='Quantité')



tableau['show'] = 'headings' 

con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
cursor = con.cursor()
#cursor.execute("select * from produit ")
cursor.execute("select * from fabrication  ")
#group by Ref_prod
rows = cursor.fetchall()
        
for row in rows:  
    tableau.insert('', 'end', iid=row, values=(row[1], row[0], row[2]))


con.close();

tableau.pack(padx = 10, pady = (0, 10))

 
bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)

bouton_terminer.pack(padx = 10, pady = (0, 10))


fenetre.mainloop()
