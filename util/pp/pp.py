from tkinter import *
import tkinter.messagebox as MessageBox
import tkinter  as tk
from tkinter import ttk 
import os
import subprocess
import sys

        

def gestion():
    command = "/home/pi/Desktop/util/cbd.sh"
    subprocess.Popen(command)
def affichagep():
    command = "/home/pi/Desktop/magasine/fabrication/aff.sh"
    subprocess.Popen(command)
    
def affichagem():
    command = "/home/pi/Desktop/util/pp/affichageM/affim.sh"
    subprocess.Popen(command)
      
def affichagebf():
    command = "/home/pi/Desktop/util/pp/affichagebf/affbf.sh"
    subprocess.Popen(command)
    
def affichageprod():
    command = "/home/pi/Desktop/util/pp/production/prod.sh"
    subprocess.Popen(command)      
        
    

root = Tk()
root.geometry("1190x560")
root.title("Directeur")
width = 1200
height = 550
image = PhotoImage(file="/home/pi/Desktop/util/pp/110.png").zoom(1).subsample(1)
canvas = Canvas(root, width=width, height=height, bd=0 ,highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(expand=YES)

gestion = Button(root, text=" Gestion des employés ", font=("calibri", 17), bg='#E4E4E4',fg='#24627A', command=gestion)
gestion.place(x=60, y=150, width=250, height=42)

affichagep = Button(root, text="Affichage des produits", font=("calibri", 17), bg='#E9E9E9',fg='#24627A', command=affichagep)
affichagep.place(x=60, y=250, width=250, height=43)

affichagem = Button(root, text="Affichage matiére_P", font=("calibri", 17), bg='#E9E9E9',fg='#24627A', command=affichagem)
affichagem.place(x=60, y=350, width=250, height=43)

affichagebf = Button(root, text="Affichage Bon_E FACTURE", font=("calibri", 17), bg='#E9E9E9',fg='#24627A', command=affichagebf)
affichagebf.place(x=850, y=150, width=250, height=43)

affichageprod = Button(root, text="Production", font=("calibri", 17), bg='#E9E9E9',fg='#24627A', command=affichageprod)
affichageprod.place(x=850, y=250, width=250, height=43)




bouton_terminer = Button(root, text = 'Déconnecter', bg='#E9E9E9',fg='#24627A', command = root.destroy)
bouton_terminer.place(x=1050, y=500) 



root.mainloop()

