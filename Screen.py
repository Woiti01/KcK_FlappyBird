import curses
from curses import panel


class Screen:
    screen = None

    def __init__(self):
        self.screen = curses.initscr()
        self.screen.keypad(True)
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)

    def showLevel(self, x, score):
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
        self.screen.refresh()

    def showPostGameScreen(self, score):
        self.clear()
        self.screen.addstr(0,0,"Koniec gry!")
        self.screen.addstr(1,0,"Twoj wynik to:")
        self.screen.addstr(2,0,str(score*10))
        self.screen.addstr(3,0,"Wcisnij q aby wrocic do menu")
        self.screen.refresh()


    def refresh(self):
        self.screen.refresh()

    def clear(self):
        self.screen.clear()
        self.screen.refresh()



