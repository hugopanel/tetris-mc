import numpy as np
import pygame as py
import json
import os
import random as rd


# Initialisation des formes
S = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0]]

Z = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]]

I = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]]

O = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]]

J = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0]]

L = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0]]

T = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0]]

shapes = {"S": S, "Z": Z, "I": I, "O": O, "J": J, "L": L, "T": T}


class Formes:
    def __init__(self, TypeForme, color):
        """Initialise la forme
        :param forme: forme à initialiser tableau 2D"""
        self.shape = shapes[TypeForme]
        self.type = TypeForme
        self.x = 0
        self.y = 0
        self.color = color

    def rotation(self, pas=1):
        """Effectue une rotation de la forme
        :param pas: nombre de rotation à effectuer"""
        self.forme = np.rot90(self.forme, pas)

    def move(self, x=1, y=1):
        """Déplace la forme
        :param x: déplacement en x
        :param y: déplacement en y"""
        self.x += x
        self.y += y

    def __str__(self) -> str:
        """
        Affiche la forme et sa position en sortie de la fonction print()"""
        return (
            "Forme : "
            + str(self.forme)
            + "\nPosition : "
            + str(self.x)
            + " "
            + str(self.y)
            + "\n"
        )

    def __repr__(self) -> dict:
        """
        Affiche la forme et sa position pour la machine"""
        return {
            "x": self.x,
            "y": self.y,
            "color": self.color,
            "type": self.type,
        }


def save(file, data) -> bool:
    """Sauvegarde de les donnée data dans un fichier Json
    :param file: nom du fichier Json"""
    f = open(file, "a")
    data_json = json.dumps(data)
    f.write(data_json)
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
        return None
    if os.stat(file).st_size == 0:
        return None
    f = open(file, "r")
    data_json = json.loads(f.read())
    f.close()
    return data_json


class Partie:
    def __init__(self, data: dict = None):
        if data == None:
            self.current_shape = Formes("S")
            self.next_shape = Formes("S")
            self.grille = np.zeros((10, 20))
            self.curent_speed = 1
            self.score = 0
        else:
            self.current_shape = Formes(data["currentForme"])
            self.grille = data["grille"]
            self.vitesse = data["vitesse"]
            self.score = data["score"]
        self.nom = ""
        self.gameOver = False

    def __str__(self) -> str:
        """Affiche les doonées de la partie"""
        return (
            "Grille : "
            + str(self.grille)
            + "\nVitesse : "
            + str(self.vitesse)
            + "\nScore : "
            + str(self.score)
            + "\n"
        )

    def ScoreInfo(self):
        """Renvoie le score et le nom du joueur"""
        return {"nom": self.name, "score": self.score}

    def GameInfo(self):
        "renvoie les données de la partie"
        test = self.grille.tolist()
        return {
            "currentForme": self.currentForme,
            "score": self.score,
            "grille": test,
            "vitesse": self.vitesse,
        }


if __name__ == "__main__":
    # Recuperation des scores
    scores = load("score.json")

    # Verification d'une partie dans le fichier save.json
    currentGame = load("save.json")
    empty("save.json")
    if currentGame == None:
        # Generation d'une nouvelle partie
        currentGame = Partie()
    else:
        # Recuperation de la partie en cour
        currentGame = Partie(currentGame)

    #!le joeur a perdu
    currentGame.gameOver = False

    if currentGame.gameOver:
        #!recupere les données "nom" et score et le met dans le fichier test.json
        # ajoute les donnée dans le dic scores
        scores["Id_game" + str(len(scores))] = currentGame.ScoreInfo()
        empty("score.json")
        save("score.json", scores)
    else:
        # Sauvegarde de la partie en cour
        save("save.json", currentGame.GameInfo())

""" 
todo: enregistrer la couleur de la tuiles dans le save
todo : enregistrer la futur tuiles dans le save
todo : enregistrer la position dans le save
"""
