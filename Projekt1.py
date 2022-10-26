from pprint import pprint
from sys import displayhook
import os
from time import sleep
import keyboard

from Level import *

#main??

# jump = False
# def on_space():
#     return True
# keyboard.add_hotkey('space', on_space())

def wyczysc():
    clear = lambda: os.system(('cls'))
    clear()

def wyswietl(x):
    wyczysc()
    for i in range(len(x)):
        for j in range(len(x[i])):
            print(x[i][j],sep='',end='')
        print("\n")
    for i in range(20):
        print("=",end='',sep='')
    print("\n")

layout = Level(12, 100)
ptak = Bird(10)
collision = False
layout.addBird(ptak)


# print(boobs.viewMap())
wyswietl(layout.viewMap())

while collision==False:
    sleep(0.5)
    layout.move()
    layout.move()
    layout.move()
    layout.move()
    layout.move()
    layout.move()
    layout.move()
    layout.move()
    layout.move()
    layout.move()
    layout.addCorrectPipe()
    if jump == True:
        layout.jump(ptak)
    else:
        layout.fall(ptak)
    jump = False
    wyswietl(layout.viewMap())
