import curses
from curses import panel
from Bird import *

class Screen:
    screen = None
    art = ["              _..",
" ___..-\"\"\"-.  `)^|   .-\"\"\"-..___",
"`-...___ \'=.\'-.\'  \-\'.=\' ___...-\'",
"        `\\  \' ##### \'  /`",
"          \'--;|||||;--\'",
"             /\\|||/\\",
"            ( /;-;\\ )",
"             \'-...-\'",
]


    def __init__(self):
        self.screen = curses.initscr()
        self.screen.keypad(True)
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)

    def showLevel(self, x, score, fps):
        for i in range(len(x)):
            self.screen.addstr(i + 1, 0, "¦")
            self.screen.addstr(i + 1, len(x[i]) + 1, "¦")
            for j in range(len(x[i])):
                self.screen.addstr(i + 1, j + 1, x[i][j])
                self.screen.addstr(0, j + 1, "-")
                self.screen.addstr(len(x) + 1, j + 1, "-")
        self.screen.addstr(0, 0, "+")
        self.screen.addstr(len(x) + 1, 0, "+")
        self.screen.addstr(0, len(x[0]) + 1, "+")
        self.screen.addstr(len(x) + 1, len(x[0]) + 1, "+")
        self.screen.addstr(len(x) + 2, 2, "Wcisnij q aby wyjsc z gry")
        self.screen.addstr(len(x) + 3, 2, "Za pomoca spacji lec do gory")
        self.screen.addstr(len(x) + 4, 2, "Wynik --> " + str((score // 10) * 100))
        self.screen.addstr(len(x) + 5, 2, "Fps --> " + str(fps))
        self.screen.refresh()

    def showPreGameScreen(self):
        self.clear()
        for i in range(len(self.art)):
            self.screen.addstr(i+1,32,self.art[i])
        self.screen.addstr(10,40,"STRAIGHT BIRD")
        self.screen.addstr(14,40, "Wcisnij przycisk by zagrac")
        self.screen.refresh()

    def showPostGameScreen(self, score):
        self.clear()
        self.screen.addstr(10,40,"Koniec gry!")
        self.screen.addstr(11,40,"Twoj wynik to:")
        self.screen.addstr(12,40,str((score // 10) * 100))
        self.screen.addstr(13,40,"Wcisnij q aby wrocic do menu")
        self.screen.refresh()

    def refresh(self):
        self.screen.refresh()

    def clear(self):
        self.screen.clear()
        self.screen.refresh()
    def birdChange(self):
        id = 0
        while True:
            self.clear()
            id = id%len(Bird.bodies)
            bird = ""
            for i in range(len(Bird.bodies[id])):
                bird = bird + str(Bird.bodies[id][i])
            self.screen.addstr(10, 40, "Wybierz ptaka")
            self.screen.addstr(12, 45, bird)
            self.screen.refresh()
            x = self.screen.getkey()
            if x == "KEY_LEFT": id = id-1
            elif x == "KEY_RIGHT": id = id+1
            elif x == "\n" or "q":
                self.clear()
                return id
    def difficultyChange(self):
        id = 1
        while True:
            id = id%3
            self.clear()
            self.screen.addstr(10, 40, "Wybierz poziom trudnosci")
            if id == 1: self.screen.addstr(12, 47, "Sredni")
            elif id == 2: self.screen.addstr(12, 47, "Trudny")
            elif id == 0: self.screen.addstr(12, 47, "Latwy")
            self.screen.refresh()
            x = self.screen.getkey()
            if x == "KEY_LEFT":
                id = id - 1
            elif x == "KEY_RIGHT":
                id = id + 1
            elif x == "\n" or "q":
                self.clear()
                return id

    def getch(self):
        return self.screen.getch()
