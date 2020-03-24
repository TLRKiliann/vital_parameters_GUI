#!/usr/bin/python3
#!-*-encoding:utf-8-*-


"""
this script is made to develop
other butons with functions
"""


import tkinter
from tkinter import *
import json
import os
import subprocess
import io
import sys
import time


def writeDate():
    """
    To export data in a json file
    and launching aspiFile.py
    """
    file = open('Main.json', 'a+')
    file.write(str("Date: "))
    file.write(textDate.get() + '\n')
    file.write(str("Prenom et Nom: "))
    file.write(textName.get() + '\n')
    file.write(str("TA: "))
    file.write(textTa.get() + " mmHg\n")
    file.write(str("Puls: "))
    file.write(textPuls.get() + "/min\n")
    file.write(str("SaO2: "))
    file.write(textSa.get() + "%\n")
    file.write(str("FR: "))
    file.write(textFr.get() + "/min\n")
    file.write(str("Temperature: "))
    file.write(textTemp.get() + "°C\n")
    file.write(str("Glycemie: "))
    file.write(textHgt.get() + " mmol/l\n")
    file.write(str("Douleurs: "))
    file.write(textDlrs.get() +"/10\n\n")
    file.close()

    try:
        if os.path.getsize('aspifile/tensor.json'):
            print("File 'tensor' exist !")
            with open('aspifile/tensor.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataTa = datastore
            dataTa['data'].append({'Date' : textDate.get(), 'Tension' : textTa.get()})
            with open('aspifile/tensor.json', 'w') as datafile2:
                json.dump(dataTa, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('Sorry the file you asked does not exist !')
        print(str(outcom))
        print("File tensor.json created !")
        dataTa = {}
        dataTa['data'] = []
        dataTa['data'].append({'Date' : textDate.get(), 'Tension' : textTa.get()})
        with open('aspifile/tensor.json', 'w') as datafile:
            json.dump(dataTa, datafile, indent=4)

    try:
        if os.path.getsize('aspifile/puls.json'):
            print("File 'puls' exist !")
            with open('aspifile/puls.json', 'r') as datapuls:
                datastore = json.load(datapuls)
                print(datastore)
            dataP = datastore
            dataP['data'].append({'Date' : textDate.get(), 'Puls' : textPuls.get()})
            with open('aspifile/puls.json', 'w') as datapuls2:
                json.dump(dataP, datapuls2, indent=4)
    except FileNotFoundError as errorfile:
        print('Sorry the file you asked does not exist !')
        print(str(errorfile))
        print("File puls.json created !")
        dataP = {}
        dataP['data'] = []
        dataP['data'].append({'Date' : textDate.get(), 'Puls' : textPuls.get()})
        with open('aspifile/puls.json', 'w') as datapuls3:
            json.dump(dataP, datapuls3, indent=4)

    try:
        if os.path.getsize('aspifile/sat.json'):
            print("File 'sat' exist !")
            with open('aspifile/sat.json', 'r') as datasat:
                datastore = json.load(datasat)
                print(datastore)
            dataS = datastore
            dataS['data'].append({'Date' : textDate.get(), 'SaO2' : textSa.get()})
            with open('aspifile/sat.json', 'w') as datasat2:
                json.dump(dataS, datasat2, indent=4)
    except FileNotFoundError as errorfile:
        print('Sorry the file you asked does not exist !')
        print(str(errorfile))
        print("File sat.json created !")
        dataS = {}
        dataS['data'] = []
        dataS['data'].append({'Date' : textDate.get(), 'SaO2' : textSa.get()})
        with open('aspifile/sat.json', 'w') as datasat3:
            json.dump(dataS, datasat3, indent=4)

    try:
        if os.path.getsize('aspifile/freq.json'):
            print("File 'freq' exist !")
            with open('aspifile/freq.json', 'r') as datafreq:
                datastore = json.load(datafreq)
                print(datastore)
            dataF = datastore
            dataF['data'].append({'Date' : textDate.get(), 'FR' : textFr.get()})
            with open('aspifile/freq.json', 'w') as datafreq2:
                json.dump(dataF, datafreq2, indent=4)
    except FileNotFoundError as errorfile:
        print('Sorry the file you asked does not exist !')
        print(str(errorfile))
        print("File freq.json created !")
        dataF = {}
        dataF['data'] = []
        dataF['data'].append({'Date' : textDate.get(), 'FR' : textFr.get()})
        with open('aspifile/freq.json', 'w') as datafreq3:
            json.dump(dataF, datafreq3, indent=4)

    try:
        if os.path.getsize('aspifile/temp.json'):
            print("File 'temp' exist !")
            with open('aspifile/temp.json', 'r') as datatemp:
                datastore = json.load(datatemp)
                print(datastore)
            dataTe2 = datastore
            dataTe2['data'].append({'Date' : textDate.get(), 'Temperature' : textTemp.get()})
            with open('aspifile/temp.json', 'w') as datatemp2:
                json.dump(dataTe2, datatemp2, indent=4)
    except FileNotFoundError as errorfile:
        print('Sorry the file you asked does not exist !')
        print(str(errorfile))
        print("File temp.json created !")
        dataTe2 = {}
        dataTe2['data'] = []
        dataTe2['data'].append({'Date' : textDate.get(), 'Temperature' : textTemp.get()})
        with open('aspifile/temp.json', 'w') as datatemp3:
            json.dump(dataTe2, datatemp3, indent=4)

    try:
        if os.path.getsize('aspifile/gly.json'):
            print("File 'gly' exist !")
            with open('aspifile/gly.json', 'r') as datagly:
                datastore = json.load(datagly)
                print(datastore)
            dataG = datastore
            dataG['data'].append({'Date' : textDate.get(), 'Glycemie' : textHgt.get()})
            with open('aspifile/gly.json', 'w') as datagly2:
                json.dump(dataG, datagly2, indent=4)
    except FileNotFoundError as errorfile:
        print('Sorry the file you asked does not exist !')
        print(str(errorfile))
        print("File gly.json created !")
        dataG = {}
        dataG['data'] = []
        dataG['data'].append({'Date' : textDate.get(), 'Glycemie' : textHgt.get()})
        with open('aspifile/gly.json', 'w') as datagly3:
            json.dump(dataG, datagly3, indent=4)

    try:
        if os.path.getsize('aspifile/dlr.json'):
            print("File 'dlr' exist !")
            with open('aspifile/dlr.json', 'r') as datadlr:
                datastore = json.load(datadlr)
                print(datastore)
            dataD = datastore
            dataD['data'].append({'Date' : textDate.get(), 'Douleurs' : textDlrs.get()})
            with open('aspifile/dlr.json', 'w') as datadlr2:
                json.dump(dataD, datadlr2, indent=4)
    except FileNotFoundError as errorfile:
        print('Sorry the file you asked does not exist !')
        print(str(errorfile))
        print("File dlr.json created !")
        dataD = {}
        dataD['data'] = []
        dataD['data'].append({'Date' : textDate.get(), 'Douleurs' : textDlrs.get()})
        with open('aspifile/dlr.json', 'w') as datadlr3:
            json.dump(dataD, datadlr3, indent=4)

    label['text'] = "All json files created !"

def appelTens():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('aspifile/aspidata.py', shell=True)

def appelPuls():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('aspifile/aspipuls.py', shell=True)

def appelSat():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('aspifile/aspisat.py', shell=True)

def appelFreq():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('aspifile/aspifreq.py', shell=True)

def appelTemp():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('aspifile/aspitemp.py', shell=True)

def appelGly():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('aspifile/aspigly.py', shell=True)

def appelDlr():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('aspifile/aspidlr.py', shell=True)

def delMain():
    """
    To earase Main.json
    """
    try:
        if os.path.getsize('Main.json'):
            os.remove('Main.json')
            label['text'] = "File Main.json has been deleted !"
            print("File Main.json has been deleted !")
            #time.sleep(2)
            #sys.exit(0)
    except FileNotFoundError:
        label['text'] = "Sorry the file you asked does not exist !"
        print('Sorry the file you asked does not exist !')

def delFile():
    """
    To earase tensor.json
    """
    try:
        if os.path.getsize('aspifile/tensor.json'):
            os.remove('aspifile/tensor.json')
            label['text'] = "File tensor.json has been deleted !"
            print("File tensor.json has been deleted !")
            #time.sleep(2)
            #sys.exit(0)
    except FileNotFoundError:
        label['text'] = "Sorry the file you asked does not exist !"
        print('Sorry the file you asked does not exist !')

def delPuls():
    """
    To earase puls.json
    """
    try:
        if os.path.getsize('aspifile/puls.json'):
            os.remove('aspifile/puls.json')
            label['text'] = "File puls.json has been deleted !"
            print("File puls.json has been deleted !")
            #time.sleep(2)
            #sys.exit(0)
    except FileNotFoundError:
        label['text'] = "Sorry the file you asked does not exist !"
        print('Sorry the file you asked does not exist !')

def delSat():
    """
    To earase sat.json
    """
    try:
        if os.path.getsize('aspifile/sat.json'):
            os.remove('aspifile/sat.json')
            label['text'] = "File sat.json has been deleted !"
            print("File sat.json has been deleted !")
            #time.sleep(2)
            #sys.exit(0)
    except FileNotFoundError:
        label['text'] = "Sorry the file you asked does not exist !"
        print('Sorry the file you asked does not exist !')

def delFreq():
    """
    To earase file
    """
    try:
        if os.path.getsize('aspifile/freq.json'):
            os.remove('aspifile/freq.json')
            label['text'] = "File freq.json has been deleted !"
            print("File freq.json has been deleted !")
            #time.sleep(2)
            #sys.exit(0)
    except FileNotFoundError:
        label['text'] = "Sorry the file you asked does not exist !"
        print('Sorry the file you asked does not exist !')

def delTemp():
    """
    To earase temp.json
    """
    try:
        if os.path.getsize('aspifile/temp.json'):
            os.remove('aspifile/temp.json')
            label['text'] = "File temp.json has been deleted !"
            print("File temp.json has been deleted !")
            #time.sleep(2)
            #sys.exit(0)
    except FileNotFoundError:
        label['text'] = "Sorry the file you asked does not exist !"
        print('Sorry the file you asked does not exist !')

def delGly():
    """
    To earase gly.json
    """
    try:
        if os.path.getsize('aspifile/gly.json'):
            os.remove('aspifile/gly.json')
            label['text'] = "File gly.json has been deleted !"
            print("File gly.json has been deleted !")
            #time.sleep(2)
            #sys.exit(0)
    except FileNotFoundError:
        label['text'] = "Sorry the file you asked does not exist !"
        print('Sorry the file you asked does not exist !')

def delDlr():
    """
    To earase dlr.json
    """
    try:
        if os.path.getsize('aspifile/dlr.json'):
            os.remove('aspifile/dlr.json')
            label['text'] = "File dlr.json has been deleted !"
            print("File dlr.json has been deleted !")
            #time.sleep(2)
            #sys.exit(0)
    except FileNotFoundError:
        label['text'] = "Sorry the file you asked does not exist !"
        print('Sorry the file you asked does not exist !')

def delEvery():
    """
    To delete all json files
    """
    delMain()
    delFile()
    delPuls()
    delSat()
    delFreq()
    delTemp()
    delGly()
    delDlr()
    label['text'] = "All json files are deleted !"

gui = Tk()
gui.title("Paramètres vitaux")
gui.configure(background='navy')
gui.geometry('620x520')

labelTitle = Label(gui, text="Paramètres vitaux", font=('Times', 18), bg='navy', fg='snow')
labelTitle.grid(row=0, column=2, pady=2)

label = Label(gui)
label = Label(text='Entrer la Date', font=('Times', 14), bg='aquamarine', width=15)
label.grid(row=1, column=1)

label1 = Label(gui)
label1 = Label(text='Entrer le Nom', font=('Times', 14), bg='aquamarine', width=15)
label1.grid(row=2, column=1)

label2 = Label(gui)
label2 = Label(text='Entrer la TA', font=('Times', 14), bg='aquamarine', width=15)
label2.grid(row=3, column=1)

label3 = Label(gui)
label3 = Label(text='Entrer les Puls', font=('Times', 14), bg='aquamarine', width=15)
label3.grid(row=4, column=1)

label4 = Label(gui)
label4 = Label(text='Entrer la SaO2', font=('Times', 14), bg='aquamarine', width=15)
label4.grid(row=5, column=1)

label5 = Label(gui)
label5 = Label(text='Entrer la FR', font=('Times', 14), bg='aquamarine', width=15)
label5.grid(row=6, column=1)

label6 = Label(gui)
label6 = Label(text='Entrer la T°C', font=('Times', 14), bg='aquamarine', width=15)
label6.grid(row=7, column=1)

label7 = Label(gui)
label7 = Label(text='Entrer la Hgt', font=('Times', 14), bg='aquamarine', width=15)
label7.grid(row=8, column=1)

label8 = Label(gui)
label8 = Label(text='Eva des Dlrs', font=('Times', 14), bg='aquamarine', width=15)
label8.grid(row=9, column=1)

textDate = Entry(gui)
textDate.grid(row=1, column=2)

textName = Entry(gui)
textName.grid(row=2, column=2)

textTa = Entry(gui)
textTa.grid(row=3, column=2)

textPuls = Entry(gui)
textPuls.grid(row=4, column=2)

textSa = Entry(gui)
textSa.grid(row=5, column=2)

textFr = Entry(gui)
textFr.grid(row=6, column=2)

textTemp = Entry(gui)
textTemp.grid(row=7, column=2)

textHgt = Entry(gui)
textHgt.grid(row=8, column=2)

textDlrs = Entry(gui)
textDlrs.grid(row=9, column=2)

button2Write = Button(gui)
button2Write.config(text='Quitter', width=15, bg='dark orange', fg='yellow', command=quit)
button2Write.grid(row=1, column=3)

buttonDel = Button(gui)
buttonDel.config(text='Tout réinitialiser', width=15, bg='salmon', fg='yellow', command=delEvery)
buttonDel.grid(row=1, column=4)

buttonWrite = Button(gui)
buttonWrite.config(text='Saisir les données', width=15, bg='dark turquoise', fg='blue2', command=writeDate)
buttonWrite.grid(row=2, column=3)

buttonDel = Button(gui)
buttonDel.config(text='Réinitialiser Main.txt', width=15, bg='salmon', fg='yellow', command=delMain)
buttonDel.grid(row=2, column=4)

button3Write = Button(gui)
button3Write.config(text='Graph TA', width=15, bg='lightblue', fg='blue2', command=appelTens)
button3Write.grid(row=3, column=3)

button4Write = Button(gui)
button4Write.config(text='Graph Puls', width=15, bg='lightblue', fg='blue2', command=appelPuls)
button4Write.grid(row=4, column=3)

button5Write = Button(gui)
button5Write.config(text='Graph SaO2', width=15, bg='lightblue', fg='blue2', command=appelSat)
button5Write.grid(row=5, column=3)

button6Write = Button(gui)
button6Write.config(text='Graph FR', width=15, bg='lightblue', fg='blue2', command=appelFreq)
button6Write.grid(row=6, column=3)

button7Write = Button(gui)
button7Write.config(text='Graph T°C', width=15, bg='lightblue', fg='blue2', command=appelTemp)
button7Write.grid(row=7, column=3)

button8Write = Button(gui)
button8Write.config(text='Graph Hgt', width=15, bg='lightblue', fg='blue2', command=appelGly)
button8Write.grid(row=8, column=3)

button9Write = Button(gui)
button9Write.config(text='Graph Dlrs', width=15, bg='lightblue', fg='blue2', command=appelDlr)
button9Write.grid(row=9, column=3)

button1Del = Button(gui)
button1Del.config(text='Réinitialiser TA', width=15, bg='salmon', fg='yellow', command=delFile)
button1Del.grid(row=3, column=4)

button2Del = Button(gui)
button2Del.config(text='Réinitialiser Puls', width=15, bg='salmon', fg='yellow', command=delPuls)
button2Del.grid(row=4, column=4)

button3Del = Button(gui)
button3Del.config(text='Réinitialiser SaO2', width=15, bg='salmon', fg='yellow', command=delSat)
button3Del.grid(row=5, column=4)

button4Del = Button(gui)
button4Del.config(text='Réinitialiser FR', width=15, bg='salmon', fg='yellow', command=delFreq)
button4Del.grid(row=6, column=4)

button5Del = Button(gui)
button5Del.config(text='Réinitialiser T°C', width=15, bg='salmon', fg='yellow', command=delTemp)
button5Del.grid(row=7, column=4)

button6Del = Button(gui)
button6Del.config(text='Réinitialiser Hgt', width=15, bg='salmon', fg='yellow', command=delGly)
button6Del.grid(row=8, column=4)

button7Del = Button(gui)
button7Del.config(text='Réinitialiser Dlrs', width=15, bg='salmon', fg='yellow', command=delDlr)
button7Del.grid(row=9, column=4)

lower_frame = Frame(gui, bg='#88c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.65, relwidth=0.95, relheight=0.3, anchor='n')

label = Label(lower_frame, font=('Courier', 12), bg='white', anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

gui.mainloop()
