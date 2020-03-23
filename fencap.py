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
        if os.path.getsize('tensor.json'):
            print("File 'tensor' exist !")
            with open("tensor.json", 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataTa = datastore
            dataTa['data'].append({'Date' : textDate.get(), 'Tension' : textTa.get()})
            with open("tensor.json", 'w') as datafile2:
                json.dump(dataTa, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('Sorry the file you asked does not exist!')
        print(str(outcom))
        print("File is created !")
        dataTa = {}
        dataTa['data'] = []
        dataTa['data'].append({'Date' : textDate.get(), 'Tension' : textTa.get()})
        with open("tensor.json", 'w') as datafile:
            json.dump(dataTa, datafile, indent=4)

    try:
        if os.path.getsize('puls.json'):
            print("File 'puls' exist!")
            with open("puls.json", 'r') as datapuls:
                datastore = json.load(datapuls)
                print(datastore)
            dataP = datastore
            dataP['data'].append({'Date' : textDate.get(), 'Puls' : textPuls.get()})
            with open("puls.json", 'w') as datapuls2:
                json.dump(dataP, datapuls2, indent=4)
    except OSError as errorfile:
        print('Sorry the file you asked does not exist!')
        print(str(errorfile))
        print("File is created !")
        dataP = {}
        dataP['data'] = []
        dataP['data'].append({'Date' : textDate.get(), 'Puls' : textPuls.get()})
        with open("puls.json", 'w') as datapuls3:
            json.dump(dataP, datapuls3, indent=4)

    try:
        if os.path.getsize('sat.json'):
            print("File 'sat' exist!")
            with open("sat.json", 'r') as datasat:
                datastore = json.load(datasat)
                print(datastore)
            dataS = datastore
            dataS['data'].append({'Date' : textDate.get(), 'SaO2' : textSa.get()})
            with open("sat.json", 'w') as datasat2:
                json.dump(dataS, datasat2, indent=4)
    except OSError as errorfile:
        print('Sorry the file you asked does not exist!')
        print(str(errorfile))
        print("File is created !")
        dataS = {}
        dataS['data'] = []
        dataS['data'].append({'Date' : textDate.get(), 'SaO2' : textSa.get()})
        with open("sat.json", 'w') as datasat3:
            json.dump(dataS, datasat3, indent=4)

    try:
        if os.path.getsize('freq.json'):
            print("File 'freq' exist!")
            with open("freq.json", 'r') as datafreq:
                datastore = json.load(datafreq)
                print(datastore)
            dataF = datastore
            dataF['data'].append({'Date' : textDate.get(), 'FR' : textFr.get()})
            with open("freq.json", 'w') as datafreq2:
                json.dump(dataF, datafreq2, indent=4)
    except OSError as errorfile:
        print('Sorry the file you asked does not exist!')
        print(str(errorfile))
        print("File is created !")
        dataF = {}
        dataF['data'] = []
        dataF['data'].append({'Date' : textDate.get(), 'FR' : textFr.get()})
        with open("freq.json", 'w') as datafreq3:
            json.dump(dataF, datafreq3, indent=4)

    try:
        if os.path.getsize('temp.json'):
            print("File 'temp' exist!")
            with open("temp.json", 'r') as datatemp:
                datastore = json.load(datatemp)
                print(datastore)
            dataTe2 = datastore
            dataTe2['data'].append({'Date' : textDate.get(), 'Temperature' : textTemp.get()})
            with open("temp.json", 'w') as datatemp2:
                json.dump(dataTe2, datatemp2, indent=4)
    except OSError as errorfile:
        print('Sorry the file you asked does not exist!')
        print(str(errorfile))
        print("File is created !")
        dataTe2 = {}
        dataTe2['data'] = []
        dataTe2['data'].append({'Date' : textDate.get(), 'Temperature' : textTemp.get()})
        with open("temp.json", 'w') as datatemp3:
            json.dump(dataTe2, datatemp3, indent=4)

    try:
        if os.path.getsize('gly.json'):
            print("File 'gly' exist!")
            with open("gly.json", 'r') as datagly:
                datastore = json.load(datagly)
                print(datastore)
            dataG = datastore
            dataG['data'].append({'Date' : textDate.get(), 'Glycemie' : textHgt.get()})
            with open("gly.json", 'w') as datagly2:
                json.dump(dataG, datagly2, indent=4)
    except OSError as errorfile:
        print('Sorry the file you asked does not exist!')
        print(str(errorfile))
        print("File is created !")
        dataG = {}
        dataG['data'] = []
        dataG['data'].append({'Date' : textDate.get(), 'Glycemie' : textHgt.get()})
        with open("gly.json", 'w') as datagly3:
            json.dump(dataG, datagly3, indent=4)

    try:
        if os.path.getsize('dlr.json'):
            print("File 'dlr' exist!")
            with open("dlr.json", 'r') as datadlr:
                datastore = json.load(datadlr)
                print(datastore)
            dataD = datastore
            dataD['data'].append({'Date' : textDate.get(), 'Douleurs' : textDlrs.get()})
            with open("dlr.json", 'w') as datadlr2:
                json.dump(dataD, datadlr2, indent=4)
    except OSError as errorfile:
        print('Sorry the file you asked does not exist!')
        print(str(errorfile))
        print("File is created !")
        dataD = {}
        dataD['data'] = []
        dataD['data'].append({'Date' : textDate.get(), 'Douleurs' : textDlrs.get()})
        with open("dlr.json", 'w') as datadlr3:
            json.dump(dataD, datadlr3, indent=4)

def appelTens():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('python3 aspidata.py', shell=True)

def appelPuls():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('python3 aspipuls.py', shell=True)

def appelSat():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('python3 aspisat.py', shell=True)

def appelFreq():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('python3 aspifreq.py', shell=True)

def appelTemp():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('python3 aspitemp.py', shell=True)

def appelGly():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('python3 aspigly.py', shell=True)

def appelDlr():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    subprocess.call('python3 aspidlr.py', shell=True)

def delMain():
    """
    To earase file
    """
    try:
        if os.path.getsize('Main.json'):
            os.remove("Main.json")
            print("File Main.json has been deleted!!!")
            #time.sleep(2)
            #sys.exit(0)
        else:
            print('Sorry, file does not exist!')
    except OSError:
        # In case the file you asked does not exists!
        print('Sorry the file you asked does not exists!')

def delFile():
    """
    To earase file
    """
    try:
        if os.path.getsize('tensor.json'):
            os.remove("tensor.json")
            print("File tensor.json has been deleted!!!")
            #time.sleep(2)
            #sys.exit(0)
        else:
            print('Sorry, file does not exist!')
    except OSError:
        # In case the file you asked does not exists!
        print('Sorry the file you asked does not exists!')

def delPuls():
    """
    To earase file
    """
    try:
        if os.path.getsize('puls.json'):
            os.remove("puls.json")
            print("File puls.json has been deleted!!!")
            #time.sleep(2)
            #sys.exit(0)
        else:
            print('Sorry, file does not exist!')
    except OSError:
        # In case the file you asked does not exists!
        print('Sorry the file you asked does not exists!')

def delSat():
    """
    To earase file
    """
    try:
        if os.path.getsize('sat.json'):
            os.remove("sat.json")
            print("File sat.json has been deleted!!!")
            #time.sleep(2)
            #sys.exit(0)
        else:
            print('Sorry, file does not exist!')
    except OSError:
        # In case the file you asked does not exists!
        print('Sorry the file you asked does not exists!')

def delFreq():
    """
    To earase file
    """
    try:
        if os.path.getsize('freq.json'):
            os.remove("freq.json")
            print("File freq.json has been deleted!!!")
            #time.sleep(2)
            #sys.exit(0)
        else:
            print('Sorry, file does not exist!')
    except OSError:
        # In case the file you asked does not exists!
        print('Sorry the file you asked does not exists!')

def delTemp():
    """
    To earase file
    """
    try:
        if os.path.getsize('temp.json'):
            os.remove("temp.json")
            print("File temp.json has been deleted!!!")
            #time.sleep(2)
            #sys.exit(0)
        else:
            print('Sorry, file does not exist!')
    except OSError:
        # In case the file you asked does not exists!
        print('Sorry the file you asked does not exists!')

def delGly():
    """
    To earase file
    """
    try:
        if os.path.getsize('gly.json'):
            os.remove("gly.json")
            print("File gly.json has been deleted!!!")
            #time.sleep(2)
            #sys.exit(0)
        else:
            print('Sorry, file does not exist!')
    except OSError:
        # In case the file you asked does not exists!
        print('Sorry the file you asked does not exists!')

def delDlr():
    """
    To earase file
    """
    try:
        if os.path.getsize('dlr.json'):
            os.remove("dlr.json")
            print("File dlr.json has been deleted!!!")
            #time.sleep(2)
            #sys.exit(0)
        else:
            print('Sorry, file does not exist!')
    except OSError:
        # In case the file you asked does not exists!
        print('Sorry the file you asked does not exists!')

gui = Tk()
gui.title("Paramètres vitaux")
gui.configure(background='navy')
gui.geometry('620x320') 

labelTitle = Label(gui, text="Paramètres vitaux", font=('Times', 18), bg='cyan')
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

buttonWrite = Button(gui)
buttonWrite.config(text='Saisir les données', width=15, bg='cyan', fg='magenta', command=writeDate)
buttonWrite.grid(row=1, column=3)

button2Write = Button(gui)
button2Write.config(text='Quitter', width=15, bg='lightblue', fg='red', command=quit)
button2Write.grid(row=1, column=4)

button3Write = Button(gui)
button3Write.config(text='Graph TA', width=15, bg='lightblue', command=appelTens)
button3Write.grid(row=3, column=3)

button4Write = Button(gui)
button4Write.config(text='Graph Puls', width=15, bg='lightblue', command=appelPuls)
button4Write.grid(row=4, column=3)

button5Write = Button(gui)
button5Write.config(text='Graph SaO2', width=15, bg='lightblue', command=appelSat)
button5Write.grid(row=5, column=3)

button6Write = Button(gui)
button6Write.config(text='Graph FR', width=15, bg='lightblue', command=appelFreq)
button6Write.grid(row=6, column=3)

button7Write = Button(gui)
button7Write.config(text='Graph T°C', width=15, bg='lightblue', command=appelTemp)
button7Write.grid(row=7, column=3)

button8Write = Button(gui)
button8Write.config(text='Graph Hgt', width=15, bg='lightblue', command=appelGly)
button8Write.grid(row=8, column=3)

button9Write = Button(gui)
button9Write.config(text='Graph Dlrs', width=15, bg='lightblue', command=appelDlr)
button9Write.grid(row=9, column=3)

buttonDel = Button(gui)
buttonDel.config(text='Supprimer Main.txt', width=15, bg='orange', fg='navy', command=delMain)
buttonDel.grid(row=2, column=4)

button1Del = Button(gui)
button1Del.config(text='Réinitialiser TA', width=15, bg='orange', fg='navy', command=delFile)
button1Del.grid(row=3, column=4)

button2Del = Button(gui)
button2Del.config(text='Réinitialiser Puls', width=15, bg='orange', fg='navy', command=delPuls)
button2Del.grid(row=4, column=4)

button3Del = Button(gui)
button3Del.config(text='Réinitialiser SaO2', width=15, bg='orange', fg='navy', command=delSat)
button3Del.grid(row=5, column=4)

button4Del = Button(gui)
button4Del.config(text='Réinitialiser FR', width=15, bg='orange', fg='navy', command=delFreq)
button4Del.grid(row=6, column=4)

button5Del = Button(gui)
button5Del.config(text='Réinitialiser T°C', width=15, bg='orange', fg='navy', command=delTemp)
button5Del.grid(row=7, column=4)

button6Del = Button(gui)
button6Del.config(text='Réinitialiser Hgt', width=15, bg='orange', fg='navy', command=delGly)
button6Del.grid(row=8, column=4)

button7Del = Button(gui)
button7Del.config(text='Réinitialiser Dlrs', width=15, bg='orange', fg='navy', command=delDlr)
button7Del.grid(row=9, column=4)

gui.mainloop()
