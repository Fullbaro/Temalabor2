import serial
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
    print("Legyen élő elemző ablak megnyitva? y/n")
    window = input()

    print("Csatlakozzon a LED-hez? y/n")
    led = input()

    if led == "y":
        print('Add meg a COM portot! (Pl.: COM4)')
        com = input().upper()        
        print("Kapcsolodás")
        ser = serial.Serial(com,9600,timeout = 1)
        print("Sikeresen kapcsolódva")    

    if window == "y":
        plt.ion()  # enable interactivity
        fig = plt.figure()  # make a figure
        plt.show()    
    while True:
        with mss.mss() as sct:
            myimg = sct.grab(sct.monitors[1])
            avg_color_per_row = np.average(myimg, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            R = str(int(avg_color[0]))
            G = str(int(avg_color[1]))
            B = str(int(avg_color[2]))
            #print(R, G, B, int(time.time()*1000.0))
            if led == "y":
                ser.write(bytes(str(int(avg_color[0]))+"-"+str(int(avg_color[1]))+"-"+str(int(avg_color[2]))+"$", 'utf-8'))
            cur.execute('INSERT INTO data (R, G, B, time) VALUES ('+R+', '+G+', '+B+', '+str(int(time.time()*1000.0))+')')        
            con.commit()

            if window == "y":
                cur.execute('SELECT R, G, B, time FROM data ORDER BY ID DESC LIMIT 50')
                dataa = cur.fetchall()            
                Rr = np.array([], dtype=np.int64)
                Gg = np.array([])
                Bb = np.array([])
                timee = np.array([])
                for linee in dataa:
                    Rr = np.append(Rr, linee[2], axis=None)
                    Gg = np.append(Gg, linee[1], axis=None)
                    Bb = np.append(Bb, linee[0], axis=None)
                    timee = np.append(timee, linee[3], axis=None)
                plt.clf()
                plt.plot(timee, Rr, "r")    
                plt.plot(timee, Gg, "g")
                plt.plot(timee, Bb, "b")
                plt.pause(0.0001) #Note this correction                                            
    con.close()
elif choise == 2:
    # elemzés
    fig = plt.figure()
    cur.execute('SELECT R, G, B, time FROM data')
    data = cur.fetchall()    
    R = np.array([], dtype=np.int64)
    G = np.array([])
    B = np.array([])
    time = np.array([])
    time2 = np.array([])
    median = np.array([])
    avg = np.array([])
    flash = np.array([])
    for i in range(len(data)-1):
        R = np.append(R, data[i][2], axis=None)
        G = np.append(G, data[i][1], axis=None)
        B = np.append(B, data[i][0], axis=None)
        time = np.append(time, data[i][3], axis=None)
        median = np.append(median, np.median([data[i][0],data[i][1],data[i][2]]) ,axis=None)
        avg = np.append(avg, np.average([data[i][0],data[i][1],data[i][2]]) ,axis=None)
        if(i > 1):
            actual = np.average([data[i][0],data[i][1],data[i][2]])
            before = np.average([data[i-1][0],data[i-1][1],data[i-1][2]])
            after = np.average([data[i+1][0],data[i+1][1],data[i+1][2]])
            if np.absolute(actual-before) > 5:
                if np.absolute(after-actual) < 5:
                    flash = np.append(flash, actual, axis=None)
                    time2 = np.append(time2, data[i][3], axis=None)

    #plt.plot(time, R, "r")
    #plt.plot(time, G, "g")
    #plt.plot(time, B, "b")
    #plt.plot(time, median, "yellow")
    fig.suptitle(str(round(len(time2)/len(time)*100, 2))+" % a kiugró érték", fontsize=20)
    plt.plot(time, avg, "black")
    plt.plot(time2, flash, "red", linestyle='None', marker='o')    
    plt.show()    
elif choise == 3:
    cur.execute('DELETE FROM data')
    con.commit()
    con.close()























