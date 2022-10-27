from pprint import pprint
from sys import displayhook
import os
from time import sleep
import keyboard
import curses

from Level import *

# main??

# addstr(y , x, string)


scr = curses.initscr()
scr.keypad(True)
curses.noecho()
curses.curs_set(0)
jump = False
x = False

def on_space():
    return True

def on_q():
    return True

def wyswietl(scr, x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            scr.addstr(i, j, x[i][j])
    scr.refresh()

x = 12
y =82
layout = Level(x,y)
ptak = Bird(x)
collision = False
layout.addBird(ptak)

wyswietl(scr, layout.viewMap())

counter = 0

while collision == False:
    counter+=1
    jump = keyboard.add_hotkey('space', on_space())
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
    wyswietl(scr, layout.viewMap())
    if counter>20:
        break
scr.getch()