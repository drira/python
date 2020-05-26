from tkinter import *
import tkinter.messagebox as MessageBox
import tkinter  as tk
from tkinter import ttk 
import os
import subprocess
import sys

        

def affichage():
    command = "/home/pi/Desktop/util/affichage/affi.sh"
    subprocess.Popen(command)
def ajouter():
    command = "/home/pi/Desktop/util/ajouter/ajouter.sh"
    subprocess.Popen(command)
def supprimer():
    command = "/home/pi/Desktop/util/supprimer/supprimer.sh"
    subprocess.Popen(command)
def modifier():
    command = "/home/pi/Desktop/util/modifier/modifier.sh"
    subprocess.Popen(command)        
    
    
    

root = Tk()
root.geometry("1190x560")
root.title("Directeur")
width = 1200
height = 550
image = PhotoImage(file="/home/pi/Desktop/util/0000.png").zoom(1).subsample(1)
canvas = Canvas(root, width=width, height=height, bd=0 ,highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(expand=YES)

affichage = Button(root, text=" Afficher ", font=("calibri", 17), bg='#E4E4E4',fg='#24627A', command=affichage)
affichage.place(x=966, y=242, width=189, height=42)

ajouter = Button(root, text="Ajouter", font=("calibri", 17), bg='#E9E9E9',fg='#24627A', command=ajouter)
ajouter.place(x=100, y=240, width=179, height=43)

modifier = Button(root, text="Modifier", font=("calibri", 17), bg='#E9E9E9',fg='#24627A', command=modifier)
modifier.place(x=390, y=242, width=174, height=42)

supprimer = Button(root, text="Supprimer", font=("calibri", 17), bg='#E9E9E9',fg='#24627A', command=supprimer)
supprimer.place(x=690, y=240, width=172, height=43)
 
bouton_terminer = Button(root, text = 'Retour', bg='#E9E9E9',fg='#24627A', command = root.destroy)
bouton_terminer.place(x=1050, y=500) 

#creation image


    
root.mainloop()

