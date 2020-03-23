#!/usr/bin/python3
# -*- coding:utf-8 -*-


import os
import json
import time


file = open("tensor.json")
data = json.load(file)
#file.close

for (key, value) in data.items():
    print("Key: " + key)
    print("Valeur: " + str(value))
    print("\nTo represent the data_get:\n")
    print(data.get("data"))
    print("\n")
    print("Valeur: " + str(value[0]))
    print("Valeur: " + str(value[1]))
    print("\n")
    print("Date: " + str(value[0]["Date"]))
    print("Tension: " + str(value[0]["Tension"]))
    print("\n")
    print("Date: " + str(value[1]["Date"]))
    print("Tension: " + str(value[1]["Tension"]))
    
print("\nDay LOOP\n")

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])
    
with open("data_date.json", 'a+') as datafile:
    json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nTension LOOP\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Tension'])

print("\nThat seems correct!\n")

with open("data_tension.json", 'a+') as datafile:
    json.dump(data_list2, datafile, indent=4)

print("\nLancement du programme 'plot_prog.py'...")
# Un temps d'attente de 2 sec:
print("Chargement dans 2 secondes...")
time.sleep(2)
# Lancement du programme plot_prog.py
os.system('python3 plot_prog.py')
