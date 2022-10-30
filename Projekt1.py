from Screen import *
from Level import *
from Menu import *

def f1():
    pass
def f2():
    pass
def f3():
    pass


pygame.init()
clock = pygame.time.Clock()

x = 20
y = 82

screen = Screen()
fps = 12
class Game(object):
    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)
        bird = Bird(x, 0)

        graphics_items = [("Zmiana Ptaka", "bird", bird), ("Zmiana Kolorow", f2)]
        graphics = Menu(graphics_items, self.screen)

        options_items = [("Zmiana poziomu trudności: ", f3)]
        options = Menu(options_items, self.screen)

        main_menu_items = [
            ("Graj", "play", Level(x,y,bird), screen, fps),
            ("Wybory graficzne", graphics.display),
            ("Opcje", options.display),
        ]
        main_menu = Menu(main_menu_items, self.screen)
        main_menu.display()

if __name__ == "__main__":
    curses.wrapper(Game)



