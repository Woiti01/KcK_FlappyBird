from pprint import pprint
from sys import displayhook
from random import *
from Bird import *

class Level:

    layout = []
    M = 0
    N = 0
    opening = 3

    #    M - ilość kolumn, N - ilość wierszy
    def __init__(self, a, b):
        self.N=a
        self.M=b
        for i in range(self.N):
            x=[]
            for j in range(self.M):
                x.append('-')
            self.layout.append(x)

    def addCorrectPipe(self):
        size = 3                         #Opcja pozwalająca EWENTUALNIE zmienić rozmiar otworu
        x = randint(1,self.N-(size+2))   #
        for i in range(x):
            self.layout[i][self.M - 1] = '|'
        self.layout[x][self.M - 1] = 'v'
        for i in range(x+1,x+(size+1)):
            self.layout[i][self.M - 1] = '-'
        self.layout[x+(size+1)][self.M - 1] = '^'
        for i in range(x+(size+2),self.N):
            self.layout[i][self.M - 1] = '|'

    def move(self):
        for i in range(self.N):
            for j in range(1,self.M):
                if self.layout[i][j - 1] not in Bird.body:
                    self.layout[i][j - 1]=self.layout[i][j]
            self.layout[i][j]= '-'

    def addBird(self, bird):
        for i in range(len(bird.body)):
            self.layout[int(bird.position)][i+1]=bird.body[i]

    # def moveAndAdd(self):
    #     for i in range(self.N):
    #         for j in range(1,self.M):
    #             self.layout[i][j - 1]=self.layout[i][j]
    #     self.addPipe(3)

    def jump(self, bird):
        bird.jump()
        for i in range(len(bird.body)):
            self.layout[int(bird.position-1)][i+1]='-'
        self.addBird(bird)

    def fall(self, bird):
        bird.gravity()
        for i in range(len(bird.body)):
            self.layout[int(bird.position - 1)][i + 1] = '-'
        self.addBird(bird)

    def viewMap(self):
        return self.layout
        

    