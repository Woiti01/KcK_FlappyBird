from Screen import *
from Level import *
from Menu import *


def f2():
    pass
def f3():
    pass


pygame.init()
clock = pygame.time.Clock()

x = 20
y = 82

screen = Screen()


class Game(object):

    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)
        bird= Bird(x)
        graphics_items = [["Zmiana Ptaka", "bird", screen, bird]]
        graphics = Menu(graphics_items, self.screen)
        options_items = [["Zmiana poziomu trudności: ", "difficulty", screen, bird]]
        options = Menu(options_items, self.screen)

        main_menu_items = [
            ["Graj", "play", Level(x,y,bird), screen],
            ["Wybory graficzne", graphics.display],
            ["Opcje", options.display],
        ]
        main_menu = Menu(main_menu_items, self.screen)
        main_menu.display()

if __name__ == "__main__":
    screen.showPreGameScreen()
    screen.getch()
    screen.clear()
    curses.wrapper(Game)



