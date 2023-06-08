import pygame as py  # import pygame library
import os  # import os library
import numpy as np

# global value
s_width = 300  # screen width
s_height = 200  # screen height


# Initialisation des formes
S = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0]]

Z = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]]

I = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]]

O = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]]

J = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0]]

L = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0]]

T = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0]]


class Formes:
    def __init__(self, forme):
        self.forme = forme
        self.x = 0
        self.y = 0

    def rotation(self, pas=1):
        for i in range(pas):
            self.forme = np.rot90(self.forme)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __str__(self) -> str:
        return (
            "Forme : "
            + str(self.forme)
            + "\nPosition : "
            + str(self.x)
            + " "
            + str(self.y)
            + "\n"
        )


def main(window):
    run = True
    while run:
        for event in py.event.get():
            if event.type == py.QUIT:
                print("Quit")
                run = False


if __name__ == "__main__":
    """win = py.display.set_mode((s_width, s_height))
    main(win)"""

    test = Formes(S)

    test.rotation()

    test.move(1, 1)
