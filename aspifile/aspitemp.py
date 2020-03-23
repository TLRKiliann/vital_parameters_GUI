#!/usr/bin/python3
# -*- coding:utf-8 -*-


import os
import json
import time


file = open("temp.json")
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
    print("Temperature: " + str(value[0]["Temperature"]))
    print("\n")
    print("Date: " + str(value[1]["Date"]))
    print("Temperature: " + str(value[1]["Temperature"]))
    
print("\nDay LOOP\n")

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])
    print(value[0]['Date'])

print("\nThat seems ok!\n")

with open("data_datetemp.json", 'a+') as datafile:
    json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nTemperature LOOP\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Temperature'])
    print(value[0]['Temperature'])

print("\nThat seems correct!\n")

with open("data_temp.json", 'a+') as datafile:
    json.dump(data_list2, datafile, indent=4)

print("\nLancement du programme 'plot_temp.py'...")
# Un temps d'attente de 2 sec:
print("Chargement dans 2 secondes...")
time.sleep(2)
# Lancement du programme plot_temp.py
os.system('python3 plot_temp.py')
