from tkinter import *
import tkinter.messagebox as MessageBox
import tkinter  as tk
from tkinter import ttk 
import os
import subprocess
import sys
import mysql.connector as mysql
        

def affip():
    command = "/home/pi/Desktop/employe/affichagep/affip.sh"
    #command2 = "/home/pi/Desktop/util/cbd.sh"
    subprocess.Popen(command)
    #subprocess.kill()
def commande():
    command = "/home/pi/Desktop/employe/commande/commande.sh"
    #command2 = "/home/pi/Desktop/util/cbd.sh"
    subprocess.Popen(command)
    #subprocess.kill()   
def dec():
    root.destroy()
    """
    con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
    cursor = con.cursor()
    cursor.execute("Delete  from Logging ")
    cursor.execute("commit");
    """
    

    
root = Tk()
root.geometry("1200x560")
root.title("Magasinie")

#creation image

width = 1200
height = 560
image = PhotoImage(file="/home/pi/Desktop/employe/00.png").zoom(1).subsample(1)
canvas = Canvas(root, width=width, height=height, bd=0 ,highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(expand=YES)




affip = Button(root, text="Afficher Produit", font=("calibri", 17), bg='#E9E9E9',fg='#000000', command=affip)
affip.place(x=82, y=398, width=433, height=51)

commande = Button(root, text="commander", font=("calibri", 17), bg='#E9E9E9',fg='#000000', command=commande)
commande.place(x=82, y=100, width=433, height=51)

bouton_terminer = Button(root, text = 'Déconnecter', bg='#E9E9E9',fg='#000000', command =dec)
bouton_terminer.place(x=1000, y=500)

root.mainloop()


