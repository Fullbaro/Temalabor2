from serial import *
import time
import sqlite3
from PIL import Image
import pyautogui
from time import sleep
from random import random
from mss import mss
import cv2
import numpy
import mss

print("Csatlakozás adatbázishoz")
con = sqlite3.connect('database.db')
cur = con.cursor()

print("Válassz a meüpontok közül")
print("1. Elemzés futtatása")
print("2. Eddigi adatok elemzése")
print("3. Eddigi adatok törlése")
choise = int(input())

if choise == 1:
    #print('Add meg a COM portot! (Pl.: COM6)')
    #com = input().upper()
    #print('Melyik monitor legyen vetítve? (Default: 1)')
    #mon = int(input())
    #print("Kapcsolodás")
    #ser = Serial(com,9600,timeout = 1)
    #print("Sikeresen kapcsolódva")
    mon = 1;

    while True:
        with mss.mss() as sct:
            myimg = sct.grab(sct.monitors[mon])
            avg_color_per_row = numpy.average(myimg, axis=0)
            avg_color = numpy.average(avg_color_per_row, axis=0)
            R = str(int(avg_color[0]))
            G = str(int(avg_color[1]))
            B = str(int(avg_color[2]))
            print(R, G, B, int(time.time()*1000.0))
            cur.execute('INSERT INTO data (R, G, B, time) VALUES ('+R+', '+G+', '+B+', '+str(int(time.time()*1000.0))+')')        
            con.commit()
            #dser.write(bytes(str(int(avg_color[0]))+"-"+str(int(avg_color[1]))+"-"+str(int(avg_color[2]))+"$", 'utf-8'))
    con.close()
elif choise == 2:
    # elemzés
    print('elemzés')
elif choise == 3:
    cur.execute('DELETE FROM data')
    con.commit()
    con.close()
