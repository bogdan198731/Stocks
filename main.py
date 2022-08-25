# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time

from general import create_data_files
from produs import *
from readExcel import *
from openExcel import openExcel, openExcel2, closeExcel

lista_prod = []
filename = 'C:/Users/bogda/Desktop/stocks4.xlsm'
NumeFisier='arhiva.xlsx'
Log = 'Log.txt'
ErrorLog = 'ErrorLog.txt'

# citire sau creare fisier arhiva
if os.path.isfile(NumeFisier):
    readArhiva(NumeFisier, lista_prod)
else:
    create_data_files(NumeFisier, 0)
#creare log
if not os.path.isfile(Log):
    create_data_files(Log, 0)

#creare log erori
if not os.path.isfile(ErrorLog):
    create_data_files(ErrorLog, 0)

#Nr iteratii
iteratii = 70
#Timp intre doua iteratii
SLEEPTIME = 300
#Iterator
k = 1
#Contor erori deschisere/citire fisier date
nrEroare = 0
#Nr maxim de erori deschidere/citire fisier date
#inainte ca programul sa se opreasca
nrMaxErori = 25
eroare = False
t = True
while t:
    try:
        openExcel(filename)
        print("Fisier data open ok")
    except:
        nrEroare += 1
        eroare = True
        if nrEroare > nrMaxErori:
            t = False
        data = "EROARE FISIER " + str(nrEroare)
        print(data)
        scrieEroare(ErrorLog, data)
    if not eroare:
        print("Iteratia : " + str(k))
        readExcel(filename, lista_prod)
        try:
            openExcel2(filename)
        except:
            data = "EROARE FISIER DELETE " + str(nrEroare)
            scrieEroare(ErrorLog, data)
        k = k + 1

        if k > iteratii:
            t = False
        else:
            time.sleep(SLEEPTIME)
    eroare = False

closeExcel(filename)
for prod in lista_prod:
    prod.afisareProdus()

produs_to_arhiva(lista_prod, NumeFisier)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
