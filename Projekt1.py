from pprint import pprint
from sys import displayhook
import Map

DASHES = 100
LINES = 10




def init():
    
    dashBoard = []
    for i in range(DASHES):
        dashBoard.append('-')
    for i in range(LINES):
        for j in range(len(dashBoard)):
            print(dashBoard[j],end='')
        print()
