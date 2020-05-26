 

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

 
tableau = Treeview(fenetre, columns=('numéro bon d entre','Date bon d entre', 'numéro facture', 'date facture'), show = 'headings')

tableau.heading('numéro bon d entre', text='numéro bon d entre')

tableau.heading('Date bon d entre', text='Date bon d entre ')

tableau.heading('numéro facture', text='numéro facture')

tableau.heading('date facture', text='date facture')


tableau['show'] = 'headings' 

con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
cursor = con.cursor()
cursor.execute("select * from bonEntre ")      
rows = cursor.fetchall()
        
for row in rows:  
    tableau.insert('', 'end', iid=row, values=(row[0], row[1], row[2], row[3],))


con.close();

tableau.pack(padx = 25, pady = (0, 25))

 
bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)

bouton_terminer.pack(padx = 25, pady = (0, 25))


fenetre.mainloop()