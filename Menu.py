import curses
from curses import panel

import keyboard
import pygame
from pygame import mixer
class Menu(object):
    def __init__(self, items, stdscreen):
        pygame.init()
        self.window = stdscreen.subwin(0, 0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items
        self.items.append(("Wstecz", "exit"))

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
        try:
            beep_Sound = mixer.Sound("Soundtrack/Beep.wav")
            beep_Sound.set_volume(0.1)
            boop_Sound = mixer.Sound("Soundtrack/Boop.wav")
        except:
            pass
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
                    try:
                        boop_Sound.play(1,1000)
                    except:
                        pass
                    break
                else:
                    if (self.items[self.position][1] == "play"):
                        self.items[self.position][2].play(self.items[self.position][3])
                    elif (self.items[self.position][1] == "bird"):
                        try:
                            beep_Sound.play(1)
                        except:
                            pass
                        self.items[self.position][3].changeSkin(self.items[self.position][2].birdChange())
                    elif (self.items[self.position][1] == "difficulty"):
                        try:
                            beep_Sound.play(1)
                        except:
                            pass
                        self.items[self.position][3].changeDiff(self.items[self.position][2].difficultyChange())
                    else:
                        try:
                            beep_Sound.play(1)
                        except:
                            pass
                        self.items[self.position][1]()
                        self.window.clear()

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

        self.panel.hide()
        curses.doupdate()