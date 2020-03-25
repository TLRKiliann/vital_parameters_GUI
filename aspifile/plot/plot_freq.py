#!/usr/bin/python3
# -*- coding:utf-8 -*-


import json
import matplotlib.pyplot as plt
import os


print("\nListe1 = dates :")
print("--------------")
fileO = open('./aspifile/data_datefr.json')
list1 = json.load(fileO)
#f.close

for letter in list1:
    print("list1: " + letter)

print("\nList2 = FR :")
print("--------------------")

fileO = open('./aspifile/data_fr.json')
list2 = json.load(fileO)
#f.close

for letter in list2:
    print("List2: " + letter)

dicolist = {}

for list1, list2 in zip(list1, list2):
    dicolist[list1] = list2

print("\nAffichage du dictionnaire :")
print("---------------------------")
print(dicolist)

list1 = []
list2 = []

for key, value in dicolist.items():
    list1.append(key)
    list2.append(value)
    
print("\nListe des dates dans l'ordre des entrées :")
print("----------------------------------")
print(list1)
# How to sort data of list1 to correspond whith list2 ???
# And for list2 ??? Is it with array ??? 
print("\nListe des frequences respiratoires :")
print("------------------------")
print(list2)

#list3 = [int(list2) for list2 in list2]
list2 = list(map(int, list2))

show_grid = True
with plt.style.context(('seaborn-darkgrid')):
    plt.plot(list1, list2)
    plt.ylabel('FR/min')
    plt.xlabel('Dates')
    plt.title('Relevé des fréquences resp (FR/min) par date')
    plt.xticks(rotation=45)
    plt.grid(show_grid)
    plt.show()

os.remove('./aspifile/data_datefr.json')
print("+ File data_datefr.json removed !")
os.remove('./aspifile/data_fr.json')
print("+ File data_fr.json removed !\n")
