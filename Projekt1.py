from pprint import pprint
from sys import displayhook
import os
from time import sleep
import keyboard
import curses
import pygame

from Screen import *
from Level import *

# addstr(y , x, string)

screen = Screen()


pygame.init()
clock = pygame.time.Clock()

x = 20
y = 82
fps = 12

ptak = Bird(x)
layout = Level(x,y,ptak)
jump = None

counter = 0

while not layout.lost:
    if keyboard.is_pressed("space"):
        jump=True
    if keyboard.is_pressed("q"):
        break
    layout.move()
    counter += 1
    if counter%10==0:
        layout.addCorrectPipe()
        counter=0
    if jump == True:
        layout.jump()
    else:
        layout.fall()
    jump = False
    screen.showLevel(layout.viewMap())
    clock.tick(fps)
