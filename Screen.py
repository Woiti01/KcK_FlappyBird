import curses


class Screen:

    screen = None

    def __init__(self):
        self.screen = curses.initscr()
        self.screen.keypad(True)
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)

    def showLevel(self, x):
        for i in range(len(x)):
            for j in range(len(x[i])):
                self.screen.addstr(i, j, x[i][j])
        self.screen.refresh()


