import numpy as np


# Initialisation des formes
shapes = {"S": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0]],
          "Z": [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]],
          "I": [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
          "O": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]],
          "J": [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0]],
          "L": [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0]],
          "T": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0]]}
colors = [color for color in range(7)]


class Tetromino:
    def __init__(self, name: str, color: int, rotation: int = 0, x: int = 0, y: int = 0):
        self.name = name
        self.color = color
        self.rotation = 0
        self.x = x
        self.y = y

        self.shape_grid = shapes[name]

        self.rotate(pas=rotation)

    def rotate(self, pas=1):
        """
        Tourne la forme dans le sens horaire
        :param pas: Nombre de rotations de 90° à effectuer
        """
        self.shape_grid = np.rot90(self.shape_grid, pas)
        self.rotation += pas
        self.rotation %= 4

    def try_rotate(self, grid, pas=1):
        """
        Essaye d'effectuer une rotation avec rotate().
        :param grid: Grille de jeu
        :param pas: Nombre de rotations de 90° à effectuer
        :return: Vrai si la rotation est possible, Faux sinon.
        """
        new_forme = np.rot90(self.shape_grid, pas)
        if self.check_collisions(new_forme, (self.x, self.y), grid):
            self.shape_grid = new_forme
            return True
        return False

    def move(self, x, y):
        """
        Force le mouvement de la forme.
        :param x: Décalage vers la droite
        :param y: Décalage vers le bas
        """
        self.x += x
        self.y += y

    def try_move(self, x, y, grid):
        """
        Comme move(), mais ne bouge pas à la nouvelle position si c'est impossible.

        :param x: Décalage vers la droite
        :param y: Décalage vers le bas
        :param grid: Grille de jeu
        :return: Vrai si le mouvement a été effectué, Faux sinon.
        """
        if self.can_move(x, y, grid):
            self.move(x, y)
            return True
        return False

    def can_move(self, tryX, tryY, grid):
        """
        Vérifie si la forme peut bouger à sa nouvelle position.

        :param tryX: Décalage vers la droite
        :param tryY: Décalage vers le bas
        :param grid: Grille de jeu
        :return: Vrai si c'est possible, Faux sinon.
        """
        newX = self.x + tryX
        newY = self.y + tryY
        return self.check_collisions(self.shape_grid, (newX, newY), grid)

    def check_collisions(self, shape, pos, grid):
        """
        Vérifie si la forme se trouve par-dessus un bloc ou en dehors des limites de la grille de jeu.

        :param shape: La forme à vérifier
        :param pos: La position de la forme dans la grille
        :param grid: La grille de jeu
        :return: Vrai si aucune collision n'existe, Faux sinon.
        """
        # On parcourt la forme
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                if shape[x][y]:
                    # Limites de la grille
                    if pos[0] + x < 0 or pos[0] + x >= 10 or pos[1] + y < 0 or pos[1] + y >= 20:
                        return False
                # Test de collision
                if self.shape_grid[x][y] and grid[pos[0] + x][pos[1] + y] != 12:
                    return False
        return True

    def __str__(self) -> str:
        return str(self.__dict__())

    def __dict__(self) -> dict:
        return {
            'name': self.name,
            'color': self.color,
            'x': self.x,
            'y': self.y,
            'rotation': self.rotation
        }
