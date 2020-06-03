import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 

from tkinter import *

from tkinter.ttk import *

import tkinter.messagebox as MessageBox

import mysql.connector as mysql

import sys

import traceback

msg = MIMEMultipart()
msg['From'] = 'aroteq1@gmail.com'
msg['To'] = 'youssef.drira1@gmail.com'

msg['Subject'] = 'Le sujet de mon mail'

con = mysql.connect(host="localhost",user="phpmyadmin" ,password="0000", database="phpmyadmin")
cursor = con.cursor()
cursor.execute("select * from commande ")      
rows = cursor.fetchall()
message = 'CIN \t               QTE    ref \t bonne \t rejeter \t durée \n'
for row in rows:  
    #tableau.insert('', 'end', iid=row, values=(row[3], row[4], row[5], row[6],))
    message += str(row[3])+'\t'+str(row[2])+'\t'+str(row[1])+'\t'+str(row[4])+'\t'+str(row[5])+'\t' +str(row[8])+'\n'
con.close()

#message = 'lll'

msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('aroteq1@gmail.com', 'B967E007')
mailserver.sendmail('aroteq1@gmail.com', 'aroteq1@gmail.com', msg.as_string())
mailserver.quit()
#aroteq1@gmail.com