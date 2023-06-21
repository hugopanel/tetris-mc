import numpy as np
import pygame as py
import json
import os
import random as rd


# Initialisation des formes
shapes = {
    "S": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0]],
    "Z": [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]],
    "I": [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
    "O": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]],
    "J": [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0]],
    "L": [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0]],
    "T": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0]],
}


shapes = {
    "S": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0]],
    "Z": [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]],
    "I": [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
    "O": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]],
    "J": [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0]],
    "L": [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0]],
    "T": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0]],
}


class Tetromino:
    def __init__(self, name: str, color: int, roration: int, x: int, y: int):
        """Initialise la shape
        :param shape: shape à initialiser tableau 2D"""
        self.name = name
        self.rotation = 0
        self.color = 0
        self.x = 0
        self.y = 0
        self.grid = np.array(shapes[name])

    def rotate(self, pas=1):
        """Effectue une rotation de la shape
        :param pas: nombre de rotation à effectuer"""
        self.shape = np.rot90(self.shape, pas)
        self.rotation += pas

    def move(self, x: int, y: int):
        """Déplace la shape
        :param x: déplacement en x
        :param y: déplacement en y"""
        self.x += x
        self.y += y

    def __str__(self) -> str:
        """Affiche la shape"""
        return str(self.__dict__())

    def __dict__(self) -> dict:
        return {
            "name": self.name,
            "rotation": self.rotation,
            "color": self.color,
            "x": self.x,
            "y": self.y,
        }

    def save(selft, file) -> bool:
        """Sauvegarde de les donnée data dans un fichier Json
        :param file: nom du fichier Json"""
        f = open(file, "w")
        f.write(json.dumps(__dict__(), indent=4))
        f.close()
        return True


def empty(file):
    """Vide le fichier Json
    :param file: nom du fichier"""
    f = open(file, "w")
    f.write("")
    f.close()


def load(file):
    """renvoie les donnée contenue de le fichier Json
    :param file: nom du fichier"""
    if not os.path.isfile(file):
        return False
    if os.stat(file).st_size == 0:
        return False
    f = open(file, "r")
    data_json = json.loads(f.read())
    f.close()
    return data_json


class mainGameState:
    def __init__(self):
        self.current_tetrimino = Tetromino(
            rd.choice(list(shapes.items()))[0], 0, 0, 0, 0
        )
        self.next_tetrimino = Tetromino(rd.choice(list(shapes.items()))[0], 0, 0, 0, 0)
        self.score = 0
        self.mutiplier = 1
        self.grid = np.zeros((20, 10), int)

        self.frame_counter = 0

        self.min_speed = 2
        self.current_speed = self.min_speed

    def save(self, file: str):
        """Renvoie le score et le nom du joueur"""
        f = open(file, "w")
        f.write(
            json.dumps(
                {
                    "score": self.score,
                    "curent_tetrimino": self.current_tetrimino.__dict__(),
                    "next_tetrimino": self.next_tetrimino.__dict__(),
                    "grid": self.grid.tolist(),
                    "frame_counter": self.frame_counter,
                    "current_speed": self.current_speed,
                },
                indent=4,
            )
        )
        f.close()
        return True


if __name__ == "__main__":
    Jeu = mainGameState()

    Jeu.save("save.json")

    print(Jeu)

    Jeu2 = load("save.json")

    # todo : ceer une instance qui prend en parametre le dictionaire

    print(Jeu2)
