import numpy as np
import pygame as py
import json
import os
import random as rd

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

formes = [S, Z, I, O, J, L, T]


class Formes:
    def __init__(self, forme):
        """Initialise la forme
        :param forme: forme à initialiser tableau 2D"""
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


def save(file, data) -> bool:
    """Sauvegarde de la partie en cour dans un fichier Json
    :param file: nom du fichier Json"""
    try:
        f = open(file, "a")
        data_json = json.dumps(data)
        f.write(data_json)
        f.close()
        return True
    except:
        return False


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


class Partie:
    def __init__(self):
        """Initialise la partie"""
        self.currentForme = Formes(formes[rd.randint(0, 6)])
        self.grille = np.zeros((10, 20))
        self.vitesse = 1
        self.score = 0
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
        return {"nom": self.nom, "score": self.score}

    def GameInfo(self):
        "renvoie les données de la partie"
        return {
            "currentForme": self.currentForme,
            "grille": self.grille,
            "vitesse": self.vitesse,
        }


if __name__ == "__main__":
    # Recuperation des scores
    scores = load("score.json")

    # Verification d'une partie en cour
    currentGame = load("currentGame.json")
    if currentGame == False:
        # Generation d'une nouvelle partie
        partie = Partie()

    #!Partie en cour
    # Changement des données du jeu
    partie.nom = "Jean"
    partie.score = 100
    partie.grille[0][0] = 1
    partie.currentForme.move(1, 1)

    #!le joeur a perdu
    partie.gameOver = True

    if partie.gameOver:
        #!recupere les données "nom" et score et le met dans le fichier test.json
        # ajoute les donnée dans le dic scores
        save("test.json", partie.ScoreInfo())
    else:
        # Sauvegarde de la partie en cour
        save("currentGame.json", partie)
