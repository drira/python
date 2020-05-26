from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    travail = e_travail.get();
    description = e_description.get();

    if(travail=="" or description==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        cursor.execute("insert into rec (travail , description) values('"+ travail +"','"+ description +"')")
        cursor.execute("commit");
        
        e_travail.delete(0, 'end')
        e_description.delete(0, 'end')
        show()
        MessageBox.showinfo("insert status", "Inserted successfully");
        con.close();
        
def delete():
    if(e_id_rec.get() == ""):
         MessageBox.showinfo("Delete Status", "id_rec is compolsary for delete")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        cursor.execute("Delete from rec where id_rec='"+ e_id_rec.get() +"'")
        cursor.execute("commit");
        show()
        e_id_rec.delete(0, 'end')
        e_travail.delete(0, 'end')
        e_description.delete(0, 'end')
        
        MessageBox.showinfo("Delete status", "Deleteted successfully");
        con.close();
        
def update():
    id_rec = e_id_rec.get()
    travail = e_travail.get();
    description = e_description.get();

    if(id_rec=="" or travail=="" or description==""):
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor() 
        cursor.execute("update rec set travail='"+ travail +"', description='" +description +"' where id_rec='" + id_rec +"'")
        cursor.execute("commit");
        
        e_id_rec.delete(0, 'end')
        e_travail.delete(0, 'end')
        e_description.delete(0, 'end')
        show()
        MessageBox.showinfo("Update status", "Updated successfully");
        con.close();
        
def get():    
    if(e_id_rec.get() == ""):
         MessageBox.showinfo("Fetch Status", "id_rec is compolsary for delete")
    else:
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        cursor.execute("select * from rec where id_rec='"+ e_id_rec.get() +"'")
        rows = cursor.fetchall()
        
        for row in rows:
            e_travail.insert(0, row[1])
            e_description.insert(0, row[2])
            
        con.close();

def show():
    
        con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
        cursor = con.cursor()
        cursor.execute("select * from rec ")      
        rows = cursor.fetchall()
        list.delete(0, list.size())
        
        for row in rows:
            insertData = str (row[0])+ '         '+row[1]+'        '+row[2]
            list.insert(list.size()+1 ,insertData)
            
        con.close();
root = Tk()
root.geometry("1190x560")
root.title("rec")

id_rec = Label(root,text='rech id_rec',font=('bold', 10))
id_rec.place(x=20,y=30)
           
travail = Label(root,text='travail demander',font=('bold', 10))
travail.place(x=20,y=60)
             
description = Label(root,text='reclamation',font=('bold', 10))
description.place(x=20,y=90);
              
e_id_rec = Entry()
e_id_rec.place(x=150, y=30)

e_travail = Entry()
e_travail.place(x=150, y=60)             

e_description = Entry()
e_description.place(x=150, y=90)

insert = Button(root, text="ajouter", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

delete = Button(root, text="supprimer", font=("italic", 10), bg="white", command=delete)
delete.place(x=110, y=140)

update = Button(root, text="modifier", font=("italic", 10), bg="white", command=update)
update.place(x=230, y=140)

get = Button(root, text="rechercher", font=("italic", 10), bg="white", command=get)
get.place(x=340, y=140)

list = Listbox(root)
list.place(x=500, y=30)

show()

root.mainloop()


