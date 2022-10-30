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
            self.screen.addstr(i + 1, 0 , "¦")
            self.screen.addstr(i + 1, len(x[i])+1, "¦")
            for j in range(len(x[i])):
                self.screen.addstr(i+1, j+1, x[i][j])
                self.screen.addstr(0 , j + 1, "-")
                self.screen.addstr(len(x)+1, j+1, "-")
        self.screen.addstr(0, 0, "+")
        self.screen.addstr(len(x) + 1, 0 , "+")
        self.screen.addstr(0 , len(x[0]) + 1, "+")
        self.screen.addstr(len(x) + 1, len(x[0]) + 1, "+")

        self.screen.addstr(len(x) + 2, 1, "Wcisnij q aby wyjsc z gry")
        self.screen.addstr(len(x) + 3, 2, "Za pomoca spacji lec do gory")
        self.screen.addstr(len(x) + 4, 3, "Wynik --> " + str((score//10)*100))
        self.screen.refresh()
    def refresh(self):
        self.screen.refresh()
    def clear(self):
        self.screen.clear()
        self.screen.refresh()
class Menu(object):
    def __init__(self, items, stdscreen):
        self.window = stdscreen.subwin(0, 0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items
        self.items.append(("Wyjscie", "exit"))

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items) - 1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = "%d. %s" % (index, item[0])
                self.window.addstr(1 + index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord("\n")]:
                if self.position == len(self.items) - 1:
                    break
                else:
                    if(self.items[self.position][1]=="play"):
                        self.items[self.position][2].play(self.items[self.position][3],self.items[self.position][4])
                    # if(self.items[self.position][1]=="exit"):
                    #     goToLastMenu()
                    else:
                        self.items[self.position][1]()

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

        # self.window.clear()
        self.panel.hide()
        # panel.update_panels()
        curses.doupdate()
