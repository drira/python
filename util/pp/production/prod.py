 

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

 
tableau = Treeview(fenetre, columns=('CIN','P_Bonne', 'P_Rejeter', 'Temps'), show = 'headings')

tableau.heading('CIN', text='CIN')

tableau.heading('P_Bonne', text='P_Bonne ')

tableau.heading('P_Rejeter', text='P_Rejeter')

tableau.heading('Temps', text='Temps')


tableau['show'] = 'headings' 

con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
cursor = con.cursor()
cursor.execute("select * from commande ")      
rows = cursor.fetchall()
        
for row in rows:  
    tableau.insert('', 'end', iid=row, values=(row[3], row[4], row[5], row[6],))


con.close();

tableau.pack(padx = 25, pady = (0, 25))

 
bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)

bouton_terminer.pack(padx = 25, pady = (0, 25))


fenetre.mainloop()