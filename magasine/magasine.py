from tkinter import *
import tkinter.messagebox as MessageBox
import tkinter  as tk
from tkinter import ttk 
import os
import subprocess
import sys
import mysql.connector as mysql

        
def commande():
    command = "/home/pi/Desktop/magasine/bon_commande/bon.sh"
    #command2 = "/home/pi/Desktop/util/cbd.sh"
    subprocess.Popen(command)
    #subprocess.kill()
           

def affim():
    command = "/home/pi/Desktop/magasine/affichageM/affim.sh"
    #command2 = "/home/pi/Desktop/util/cbd.sh"
    subprocess.Popen(command)
    #subprocess.kill()
    
def fabrication():
    command = "/home/pi/Desktop/magasine/fabrication/fabrication.sh"
    #command2 = "/home/pi/Desktop/util/cbd.sh"
    subprocess.Popen(command)
    #subprocess.kill()
    
def affip():
    command = "/home/pi/Desktop/magasine/affichagep/affip.sh"
    #command2 = "/home/pi/Desktop/util/cbd.sh"
    subprocess.Popen(command)
    #subprocess.kill()
def comman():
    command = "/home/pi/Desktop/magasine/commande/commande.sh"
    #command2 = "/home/pi/Desktop/util/cbd.sh"
    subprocess.Popen(command)
    #subprocess.kill()
    
   
def show():
    
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        cursor.execute("select * from rec ")      
        rows = cursor.fetchall()
        list.delete(0, list.size())
        
        for row in rows:
            insertData = str (row[1]+'        '+row[2])
            list.insert(list.size()+1 ,insertData)
            
        con.close();    
   
    
root = Tk()
root.geometry("1200x560")
root.title("Magasinie")

#creation image

width = 1200
height = 560
image = PhotoImage(file="/home/pi/Desktop/magasine/66.png").zoom(1).subsample(1)
canvas = Canvas(root, width=width, height=height, bd=0 ,highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(expand=YES)


commande = Button(root, text="Ajouter Matiere Premier", font=("calibri", 17), bg='#E4E4E4',fg='#24627A', command=commande)
commande.place(x=83, y=111, width=435, height=51)

affim = Button(root, text="Afficher Matiere Premiere", font=("calibri", 17), bg='#E9E9E9',fg='#24627A', command=affim)
affim.place(x=83, y=204, width=435, height=52)

fabrication = Button(root, text="Fabriquer Produit", font=("calibri", 17), bg='#E9E9E9',fg='#24627A', command=fabrication)
fabrication.place(x=81, y=299, width=435, height=52)

affip = Button(root, text="Afficher Produit", font=("calibri", 17), bg='#E9E9E9',fg='#24627A', command=affip)
affip.place(x=82, y=398, width=433, height=51)

comman = Button(root, text="commande", font=("calibri", 17), bg='#E9E9E9',fg='#24627A', command=comman)
comman.place(x=1000, y=35)

bouton_terminer = Button(root, text = 'Déconnecter', bg='#E9E9E9',fg='#24627A', command = root.destroy)
bouton_terminer.place(x=1000, y=500)


list = Listbox(root)
list.place(x=800, y=30)

show()
root.mainloop()


