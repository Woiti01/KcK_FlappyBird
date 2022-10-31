import logging
from pprint import pprint
from sys import displayhook
from random import *
from Bird import *
import keyboard
import pygame

class Level:
    layout = []
    pipe = ['|', 'v', '^']
    blank = ' '
    lost = False
    opening = 3

    #    M - ilość kolumn, N - ilość wierszy
    def __init__(self, a, b, bird):
        pygame.init()
        self.N = a
        self.M = b
        self.bird = bird
        for i in range(self.N):
            x = []
            for j in range(self.M):
                x.append(self.blank)
            self.layout.append(x)
        for i in range(len(bird.body)):
            self.layout[int(bird.position)][i + 1] = bird.body[i]

    def addCorrectPipe(self):
        size = 6  # Opcja pozwalająca EWENTUALNIE zmienić rozmiar otworu
        x = randint(1, self.N - (size + 2))  #
        for i in range(x):
            self.layout[i][self.M - 1] = self.pipe[0]
        self.layout[x][self.M - 1] = self.pipe[1]
        for i in range(x + 1, x + (size + 1)):
            self.layout[i][self.M - 1] = self.blank
        self.layout[x + (size + 1)][self.M - 1] = self.pipe[2]
        for i in range(x + (size + 2), self.N):
            self.layout[i][self.M - 1] = self.pipe[0]

    def move(self):
        for i in range(self.N):
            for j in range(1, self.M):
                if self.layout[i][j - 1] not in self.bird.body:
                    self.layout[i][j - 1] = self.layout[i][j]
                else:
                    if self.layout[i][j] in self.pipe:
                        self.lost=True
            self.layout[i][j] = self.blank
            self.layout[i][0] = self.blank

    def addBird(self):
        side = 1                                                               #Odleglosc od krawedzi?
        for i in range(len(self.bird.body)):
            self.layout[int(self.bird.position)][i + side] = self.bird.body[i]

    def jump(self):
        self.bird.jump()
        for i in range(len(self.bird.body)):
            if self.layout[int(self.bird.position)][i] in self.pipe:
                self.lost = True
            self.layout[int(self.bird.position + 1)][i] = self.blank
            self.layout[int(self.bird.position + 1)][i+1] = self.blank
        self.addBird()

    def fall(self):
        self.bird.gravity()
        for i in range(len(self.bird.body)):
            if self.layout[int(self.bird.position)][i] in self.pipe:
                self.lost = True
            self.layout[int(self.bird.position - 1)][i] = self.blank
            self.layout[int(self.bird.position - 1)][i+1] = self.blank
        self.addBird()

    def changeBird(self, id):
        self.bird.changeSkin(id)

    def newGame(self):
        tab = []
        for i in range(self.N):
            x = []
            for j in range(self.M):
                x.append(self.blank)
            tab.append(x)
        self.layout = tab
        for i in range(len(self.bird.body)):
            self.layout[int(self.bird.position)][i + 1] = self.bird.body[i]
        self.lost = False

    def play(self,screen,fps):

        clock = pygame.time.Clock()
        score = 0
        jump = None

        while not self.lost:
            if keyboard.is_pressed("space"):
                jump = True
            if keyboard.is_pressed("q"):
                break
            self.move()
            score += 1
            if score % 10 == 0:
                self.addCorrectPipe()
            if jump == True:
                self.jump()
            else:
                self.fall()
            jump = False
            screen.showLevel(self.viewMap(),score)
            clock.tick(fps)
        screen.showPostGameScreen(score)
        while True:
            if keyboard.is_pressed("q"):
                break
        self.newGame()
        screen.clear()

    def viewMap(self):
        return self.layout
