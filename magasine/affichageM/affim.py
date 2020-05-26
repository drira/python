 

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

 
tableau = Treeview(fenetre, columns=('Referance','Quantite', 'Designation', 'Emplacement'), show = 'headings')

tableau.heading('Referance', text='Referance')

tableau.heading('Quantite', text='Quantité ')

tableau.heading('Designation', text='Designation')

tableau.heading('Emplacement', text='Emplacement')


tableau['show'] = 'headings' 

con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
cursor = con.cursor()
cursor.execute("select * from matierePremiere ")      
rows = cursor.fetchall()
        
for row in rows:  
    tableau.insert('', 'end', iid=row, values=(row[0], row[1], row[2], row[3],))


con.close();

tableau.pack(padx = 10, pady = (0, 10))

 
bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)

bouton_terminer.pack(padx = 10, pady = (0, 10))


fenetre.mainloop()