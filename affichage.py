from tkinter import *
 
class ComboBox(Frame):
  "Widget composite associant un champ d'entrée avec une boîte de liste"
  def __init__(self, boss, item='', items=[], command ='', width =10,
    listSize =5):
      Frame.__init__(self, boss)   # constructeur de la classe parente
           # (<boss> est la réf. du widget 'maître')
      self.items =items       # items à placer dans la boîte de liste
      self.command =command   # fonction à invoquer après clic ou <enter>
      self.item =item       # item entré ou sélectionné
 
      # Champ d'entrée :
      self.entree =Entry(self, width =width)          # largeur en caractères
      self.entree.insert(END, item)
      self.entree.bind("<Return>", self.sortieE)
      self.entree.pack(side =TOP)
 
      # Boîte de liste, munie d'un 'ascenseur' (scroll bar) :
      cadreLB =Frame(self)       # cadre pour l'ensemble des 2
      self.bListe =Listbox(cadreLB, height =listSize, width =width-1)
      scrol =Scrollbar(cadreLB, command =self.bListe.yview)
      self.bListe.config(yscrollcommand =scrol.set)
      self.bListe.bind("<ButtonRelease-1>", self.sortieL)
      self.bListe.pack(side =LEFT)
      scrol.pack(expand =YES, fill =Y)
      cadreLB.pack()
 
      # Remplissage de la boîte de liste avec les items fournis :
      for it in items:
         self.bListe.insert(END, it)
 
  def sortieL(self, event =None):
      # Extraire de la liste l'item qui a été sélectionné :
      index =self.bListe.curselection()      # renvoie un tuple d'index
      ind0 =int(index[0])         # on ne garde que le premier
      self.item =self.items[ind0]
      # Actualiser le champ d'entrée avec l'item choisi :
      self.entree.delete(0, END)
      self.entree.insert(END, self.item)
      # Exécuter la commande indiquée, avec l'item choisi comme argument :
      self.command(self.item)
 
  def sortieE(self, event =None):
      # Exécuter la commande indiquée, avec l'argument-item encodé tel quel :
      self.command(self.entree.get())
 
  def get(self):
      # Renvoyer le dernier item sélectionné dans la boîte de liste
      return self.item
 
if __name__ =="__main__":       # --- Programme de test ---
  def changeCoul(col):
      fen.configure(background = col)
 
  def changeLabel():
      lab.configure(text = combo.get())
 
  couleurs = ('navy', 'royal blue', 'steelblue1', 'cadet blue',
      'lawn green', 'forest green', 'yellow', 'dark red',
      'grey80','grey60', 'grey40', 'grey20', 'pink')
  fen =Tk()
  combo =ComboBox(fen, item ="néant", items =couleurs, command =changeCoul,
      width =15, listSize =6)
  combo.grid(row =1, columnspan =2, padx =10, pady =10)
  bou = Button(fen, text ="Test", command =changeLabel)
  bou.grid(row =2, column =0, padx =8, pady =8)
  lab = Label(fen, text ="Bonjour", bg ="ivory", width =15)
  lab.grid(row =2, column =1, padx =8)
  fen.mainloop()