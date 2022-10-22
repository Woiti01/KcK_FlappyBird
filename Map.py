from pprint import pprint
from sys import displayhook
from random import *


map =[]
M = 0
N = 0

#    M - ilość kolumn, N - ilość wierszy
def __create__(N, M):
    for i in range(N):
        x=[]
    for j in range (M):
        x.append('-')
    map.append(x)

def addPipe(size):
    x = randint(1, (N-1))
    for i in range(x):
        map[M][i]='|'
    map[M][x]='v'
    for i in range(x+1, N-size-1):
        map[M][i] = '-'
    map[M][N-size] = '^'
    for i in range(N-size+1,N):
        map[M][i] = '|'

def addPipe():
    pass

def move(): #??????????????????????????????
    for i in range(N):
        for j in range(1,M):
            map[i][j-1]=map[i][j]
        map[i][j]='-'

def moveAndAdd():
    for i in range(N):
        for j in range(1,M):
            map[i][j-1]=map[i][j]
    addPipe()
    

    