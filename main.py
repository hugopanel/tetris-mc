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


class Tetromino:
    def __init__(self, name: str, color: int, roration: int, x: int, y: int, data=None):
        """Initialise la shape
        :param shape: shape à initialiser tableau 2D"""
        if isinstance(data, dict):
            self.name = data["name"]
            self.rotation = data["rotation"]
            self.color = data["color"]
            self.x = data["x"]
            self.y = data["y"]
        else:
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

    def save(self, file) -> bool:
        """Sauvegarde de les donnée data dans un fichier Json
        :param file: nom du fichier Json"""
        f = open(file, "w")
        f.write(json.dumps(self.__dict__(), indent=4))
        f.close()
        return True


def empty(file: str):
    """Vide le fichier Json
    :param file: nom du fichier"""
    f = open(file, "w")
    f.write("")
    f.close()


def load(file: str) -> dict:
    """renvoie les donnée d'un fichier JSON sour forme de dictionaire
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
    def __init__(self, data=None):
        self.min_speed = 2
        if isinstance(data, dict):
            self.score = data["score"]
            self.mutiplier = data["multiplier"]
            self.grid = np.array(data["grid"])
            self.frame_counter = data["frame_counter"]
            self.current_speed = data["current_speed"]
            self.current_tetrimino = Tetromino(
                rd.choice(list(shapes.items()))[0],
                0,
                0,
                0,
                0,
                data["current_tetrimino"],
            )
            self.next_tetrimino = Tetromino(
                rd.choice(list(shapes.items()))[0], 0, 0, 0, 0, data["next_tetrimino"]
            )
        else:
            self.score = 0
            self.mutiplier = 1
            self.grid = np.zeros((20, 10), int)
            self.next_tetrimino = Tetromino(
                rd.choice(list(shapes.items()))[0], 0, 0, 0, 0
            )
            self.current_tetrimino = Tetromino(
                rd.choice(list(shapes.items()))[0], 0, 0, 0, 0
            )

            self.frame_counter = 0
            self.current_speed = self.min_speed

            self.mutiplier = 1

    def __dict__(self) -> dict:
        """Affiche les donnée de l'object sous forme de dictionaire"""
        return {
            "score": self.score,
            "current_tetrimino": self.current_tetrimino.__dict__(),
            "next_tetrimino": self.next_tetrimino.__dict__(),
            "grid": self.grid.tolist(),
            "frame_counter": self.frame_counter,
            "current_speed": self.current_speed,
            "multiplier": self.mutiplier,
        }

    def save(self, file: str) -> bool:
        """Sauvegarde de les donnée de l'object dans un fichier Json"""
        f = open(file, "w")
        f.write(
            json.dumps(
                self.__dict__(),
                indent=4,
            )
        )
        f.close()
        return True

    def __str__(self):
        """print values of the object"""
        return str(self.__dict__())


if __name__ == "__main__":
    Jeu = mainGameState(load("save.json"))

    Jeu.current_tetrimino.color = rd.randint(1, 7)

    Jeu.save("save.json")
