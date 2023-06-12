import numpy as np
import pygame as py
import os

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
        """Effectue une rotation de la forme
        :param pas: nombre de rotation à effectuer"""
        self.forme = np.rot90(self.forme, pas)

    def move(self, x, y):
        """Déplace la forme
        :param x: déplacement en x
        :param y: déplacement en y"""
        self.x += x
        self.y += y

    def __str__(self) -> str:
        """
        Affiche la forme et sa position"""
        return (
            "Forme : "
            + str(self.forme)
            + "\nPosition : "
            + str(self.x)
            + " "
            + str(self.y)
            + "\n"
        )


def save(file, data):
    """Sauvegarde la partie
    :param file: nom du fichier"""
    f = open(file, "a")
    f.write(str(data))
    f.close()


def load(file):
    """Charge la partie
    :param file: nom du fichier"""
    if not os.path.isfile(file):
        return None
    if os.stat(file).st_size == 0:
        return None
    f = open(file, "r")
    data = f.read()
    f.close()
    return data


if __name__ == "__main__":
    py.init()
    screen = py.display.set_mode((s_width, s_height))
    curent = load("save.json")
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                save("save.json", curent)
                py.quit()
                exit()
            if event.type == py.KEYDOWN and event.key == py.K_UP:
                curent.move(0, 1)
                print(curent)
            if event.type == py.KEYDOWN and event.key == py.K_DOWN:
                curent.move(0, -1)
                print(curent)
            if event.type == py.KEYDOWN and event.key == py.K_LEFT:
                curent.rotation(1)
            if event.type == py.KEYDOWN and event.key == py.K_RIGHT:
                curent.rotation(-1)
        py.display.update()
