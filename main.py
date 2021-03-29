from serial import *
import time
import sqlite3
from PIL import Image
import pyautogui
from time import sleep
from random import random
from mss import mss
import cv2
import numpy as np
import mss
import matplotlib.pyplot as plt

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
    #print('Mely3ik monitor legyen vetítve? (Default: 1)')
    #mon = int(input())
    #print("Kapcsolodás")
    #ser = Serial(com,9600,timeout = 1)
    #print("Sikeresen kapcsolódva")
    mon = 1;

    plt.ion()  # enable interactivity
    fig = plt.figure()  # make a figure
    plt.show()
    while True:
        with mss.mss() as sct:
            myimg = sct.grab(sct.monitors[mon])
            avg_color_per_row = np.average(myimg, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            R = str(int(avg_color[0]))
            G = str(int(avg_color[1]))
            B = str(int(avg_color[2]))
            print(R, G, B, int(time.time()*1000.0))
            cur.execute('INSERT INTO data (R, G, B, time) VALUES ('+R+', '+G+', '+B+', '+str(int(time.time()*1000.0))+')')        
            con.commit()
            
            cur.execute('SELECT R, G, B, time FROM data')
            dataa = cur.fetchall()            
            Rr = np.array([], dtype=np.int64)
            Gg = np.array([])
            Bb = np.array([])
            timee = np.array([])
            for linee in dataa:
                Rr = np.append(Rr, linee[0], axis=None)
                Gg = np.append(Gg, linee[1], axis=None)
                Bb = np.append(Bb, linee[2], axis=None)
                timee = np.append(timee, linee[3], axis=None)
            plt.plot(timee, Rr, "r")
            plt.plot(timee, Gg, "g")
            plt.plot(timee, Bb, "b")
            plt.pause(0.0001) #Note this correction
            
                    
            #dser.write(bytes(str(int(avg_color[0]))+"-"+str(int(avg_color[1]))+"-"+str(int(avg_color[2]))+"$", 'utf-8'))
    con.close()
elif choise == 2:
    # elemzés
    cur.execute('SELECT R, G, B, time FROM data')
    data = cur.fetchall()
    print(len(data))
    R = np.array([], dtype=np.int64)
    G = np.array([])
    B = np.array([])
    time = np.array([])
    for line in data:
        R = np.append(R, line[0], axis=None)
        G = np.append(G, line[1], axis=None)
        B = np.append(B, line[2], axis=None)
        time = np.append(time, line[3], axis=None)
            
    #plt.figure()   
    #plt.plot(time, R, "r")
    #plt.plot(time, G, "g")
    #plt.plot(time, B, "b")    
    #plt.show(block=False)
    plt.scatter(time, R)
    plt.show()
elif choise == 3:
    cur.execute('DELETE FROM data')
    con.commit()
    con.close()
