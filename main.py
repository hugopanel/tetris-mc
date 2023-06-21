import pygame
import numpy as np
import random


class Tileset:
    def __init__(self, file, size=(8, 8)):
        self.file = file
        self.size = size
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()

    def load(self):
        self.tiles = []
        w, h = self.rect.size

        nTilesX = int(w/self.size[0])
        nTilesY = int(h/self.size[1])

        for y in range(0, nTilesY):
            for x in range(0, nTilesX):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x*self.size[0], y*self.size[1], *self.size))
                self.tiles.append(tile)


# Initialisation des formes
shapes = {"S": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0]],
          "Z": [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]],
          "I": [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
          "O": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]],
          "J": [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0]],
          "L": [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0]],
          "T": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0]]}
colors = [color for color in range(7)]


class Formes:
    def __init__(self, forme, color):
        self.forme = forme
        self.x = 0
        self.y = 0
        self.color = color

    def rotate(self, pas=1):
        """
        Tourne la forme dans le sens horaire
        :param pas: Nombre de rotations de 90° à effectuer
        """
        self.forme = np.rot90(self.forme, pas)

    def tryRotate(self, grid, pas=1):
        """
        Essaye d'effectuer une rotation avec rotate().
        :param grid: Grille de jeu
        :param pas: Nombre de rotations de 90° à effectuer
        :return: Vrai si la rotation est possible, Faux sinon.
        """
        newForme = np.rot90(self.forme, pas)
        if self.checkCollisions(newForme, (self.x, self.y), grid):
            self.forme = newForme
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

    def tryMove(self, x, y, grid):
        """
        Comme move(), mais ne bouge pas à la nouvelle position si c'est impossible.

        :param x: Décalage vers la droite
        :param y: Décalage vers le bas
        :param grid: Grille de jeu
        :return: Vrai si le mouvement a été effectué, Faux sinon.
        """
        if self.canMove(x, y, grid):
            self.move(x, y)
            return True
        return False

    def canMove(self, tryX, tryY, grid):
        """
        Vérifie si la forme peut bouger à sa nouvelle position.

        :param tryX: Décalage vers la droite
        :param tryY: Décalage vers le bas
        :param grid: Grille de jeu
        :return: Vrai si c'est possible, Faux sinon.
        """
        newX = self.x + tryX
        newY = self.y + tryY
        return self.checkCollisions(self.forme, (newX, newY), grid)

    def checkCollisions(self, shape, pos, grid):
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
                if self.forme[x][y] and grid[pos[0] + x][pos[1] + y] != 12:
                    return False
        return True

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


def drawInterface(screen, tileset):
    """
    Dessine l'interface du jeu
    :param screen: L'écran sur lequel afficher l'interface
    :param tileset: Le tileset
    :return:
    """
    interface = np.full((32, 30), 12, dtype=int)
    # interface = np.full((32, 30), 25, dtype=int)

    # Carré grille de jeu
    # Coin haut gauche
    interface[3][6] = 17
    # Ligne dessus
    interface[4][6] = 9
    interface[5][6] = 9
    interface[6][6] = 9
    interface[7][6] = 9
    interface[8][6] = 9
    interface[9][6] = 9
    interface[10][6] = 9
    interface[11][6] = 9
    interface[12][6] = 9
    interface[13][6] = 9
    # Coin haut droite
    interface[14][6] = 16
    # Ligne gauche
    interface[3][7] = 10
    interface[3][8] = 10
    interface[3][9] = 10
    interface[3][10] = 10
    interface[3][11] = 10
    interface[3][12] = 10
    interface[3][13] = 10
    interface[3][14] = 10
    interface[3][15] = 10
    interface[3][16] = 10
    interface[3][17] = 10
    interface[3][18] = 10
    interface[3][19] = 10
    interface[3][20] = 10
    interface[3][21] = 10
    interface[3][22] = 10
    interface[3][23] = 10
    interface[3][24] = 10
    interface[3][25] = 10
    interface[3][26] = 10
    # Ligne droite
    interface[14][7] = 8
    interface[14][8] = 8
    interface[14][9] = 8
    interface[14][10] = 8
    interface[14][11] = 8
    interface[14][12] = 8
    interface[14][13] = 8
    interface[14][14] = 8
    interface[14][15] = 8
    interface[14][16] = 8
    interface[14][17] = 8
    interface[14][18] = 8
    interface[14][19] = 8
    interface[14][20] = 8
    interface[14][21] = 8
    interface[14][22] = 8
    interface[14][23] = 8
    interface[14][24] = 8
    interface[14][25] = 8
    interface[14][26] = 8
    # Coin bas gauche
    interface[3][27] = 15
    # Ligne bas
    interface[4][27] = 7
    interface[5][27] = 7
    interface[6][27] = 7
    interface[7][27] = 7
    interface[8][27] = 7
    interface[9][27] = 7
    interface[10][27] = 7
    interface[11][27] = 7
    interface[12][27] = 7
    interface[13][27] = 7
    # Coin bas droit
    interface[14][27] = 14

    # Carré forme suivante
    # Coin haut gauche
    interface[18][6] = 17
    # Ligne haut
    interface[19][6] = 9
    interface[20][6] = 9
    interface[21][6] = 9
    interface[22][6] = 9
    # Coin haut droit
    interface[23][6] = 16
    # Ligne gauche
    interface[18][7] = 10
    interface[18][8] = 10
    interface[18][9] = 10
    interface[18][10] = 10
    # Ligne droite
    interface[23][7] = 8
    interface[23][8] = 8
    interface[23][9] = 8
    interface[23][10] = 8
    # Coin bas gauche
    interface[18][11] = 15
    # Ligne bas
    interface[19][11] = 7
    interface[20][11] = 7
    interface[21][11] = 7
    interface[22][11] = 7
    # Coin bas droit
    interface[23][11] = 14

    # On parcourt la grille d'interface pour afficher les tiles une par une
    for row in range(0, len(interface)):
        for col in range(0, len(interface[row])):
            screen.blit(tileset.tiles[interface[row][col]], (row * 8, col * 8),
                        tileset.tiles[interface[row][col]].get_rect())


def draw_shape_object(screen, tileset, obj):
    """
    Affiche une forme à l'écran.

    :param screen: L'écran sur lequel afficher la forme (le même que pour l'interface)
    :param tileset: Le tileset
    :param obj: La forme à afficher
    :return:
    """
    draw_shape(screen, tileset, obj.forme, obj.color, 4+obj.x, 7+obj.y)


def draw_shape(screen, tileset, shape, color, objX, objY):
    # Display shape
    for y in range(len(shape)):
        for x in range(len(shape[y])):
            if shape[x][y]:
                tile = tileset.tiles[color]

                screen.blit(tile, ((objX + x)*8, (objY + y)*8), tile.get_rect())


def drawGrid(screen, tileset, grid):
    """
    Affiche la grille de jeu sur l'écran.

    :param screen: La surface sur laquelle afficher la grille
    :param tileset: Le tileset
    :param grid: La grille de jeu
    """
    for y in range(20):
        for x in range(10):
            tile = tileset.tiles[grid[x][y]]
            screen.blit(tile, ((4 + x)*8, (7 + y)*8), tile.get_rect())


def DeleteLineLowerBloc(grid):
    """
    Supprime les lignes complètes et ajoute des lignes vides en haut de la grille.

    :param grid: La grille de jeu
    :return: La nouvelle grille de jeu
    """
    grid = np.array(grid)
    lines_to_delete = 1*np.all(grid != 12, axis=0)
    lines_to_delete = np.where(lines_to_delete == 1)[0]
    grid = np.delete(grid, lines_to_delete, axis=1)
    for _ in lines_to_delete:
        grid = np.hstack((np.array([12 for _ in range(10)])[:, np.newaxis], grid))
    return grid


def main(window):
    """boucle du jeu principale
    Args:
        window (pygame window): fenêtre du jeu.
    """
    run = True
    tileset_file = 'tileset.png'

    screen = pygame.Surface((256, 240))

    pygame.init()

    tileset = Tileset(tileset_file)

    current_shape = Formes(random.choice(list(shapes.values())), random.choice(colors))
    next_shape = Formes(random.choice(list(shapes.values())), random.choice(colors))

    clock = pygame.time.Clock()
    frameCounter = 0

    grid = np.full((10, 20), 12, dtype=int)

    while run:
        # clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # save("save.json", curent)
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                current_shape.tryRotate(grid, 1)

            # if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            #     current.move(0, 1)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                current_shape.tryMove(-1, 0, grid)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                current_shape.tryMove(1, 0, grid)

        drawInterface(screen, tileset)  # Affichage de l'interface
        drawGrid(screen, tileset, grid)  # Affichage de la grille
        draw_shape_object(screen, tileset, current_shape)  # Affichage de la forme actuelle
        draw_shape(screen, tileset, next_shape.forme, next_shape.color, 19, 7)  # Affichage de la prochaine forme

        window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
        pygame.display.update()

        clock.tick(60)
        frameCounter += 1
        if frameCounter == 10:
            if not current_shape.tryMove(0, 1, grid):
                # On ne peut pas bouger la forme vers le bas.
                # On vérifie si la forme est par-dessus des blocs, auquel cas le joueur a perdu
                if not current_shape.tryMove(0, 0, grid) and current_shape.y == 0:
                    # Game over
                    print("Game Over!")
                    return

                # On ajoute la forme à la grille et on la supprime.
                # Pour ça, on parcourt la forme pour voir où il y a des blocs
                for y in range(len(current_shape.forme)):
                    for x in range(len(current_shape.forme[y])):
                        if current_shape.forme[x][y]:
                            # Il y a un bloc, on l'ajoute
                            grid[current_shape.x + x][current_shape.y + y] = current_shape.color
                grid = DeleteLineLowerBloc(grid)
                # On supprime la forme et on en ajoute une nouvelle
                del current_shape
                current_shape = next_shape
                next_shape = Formes(random.choice(list(shapes.values())), random.choice(colors))
            frameCounter = 0


if __name__ == "__main__":
    window = pygame.display.set_mode((720, 480))
    main(window)
