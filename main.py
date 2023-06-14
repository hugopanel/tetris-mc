import pygame
import numpy as np


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
S = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0]]

Z = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]]

I = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]]

O = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]]

J = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0]]

L = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0]]

T = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0]]


class Formes:
    def __init__(self, forme, color):
        self.forme = forme
        self.x = 0
        self.y = 0
        self.color = color

    def rotation(self, pas=1):
        """Effectue une rotation de la forme
        :param pas: nombre de rotations de 90° à effectuer"""
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


def drawInterface(screen, tileset):
    interface = np.full((32, 30), 12, dtype=int)
    # interface = np.full((32, 30), 0, dtype=int)

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

    for row in range(0, len(interface)):
        for col in range(0, len(interface[row])):
            screen.blit(tileset.tiles[interface[row][col]], (row * 8, col * 8),
                        tileset.tiles[interface[row][col]].get_rect())


def drawShape(screen, tileset, current):
    # Display shape
    for y in range(len(current.forme)):
        for x in range(len(current.forme[y])):
            if current.forme[x][y]:
                tile = tileset.tiles[current.color]

                screen.blit(tile, ((4 + current.x + x) * 8, (7 + current.y + y) * 8),
                            tile.get_rect())
            else:
                tile = tileset.tiles[2]

                screen.blit(tile, ((4 + current.x + x) * 8, (7 + current.y + y) * 8),
                            tile.get_rect())


if __name__ == "__main__":
    tileset_file = 'tileset.png'

    screen = pygame.Surface((256, 240))

    pygame.init()
    window = pygame.display.set_mode((720, 480))

    tileset = Tileset(tileset_file)
    screen.blit(tileset.tiles[4], tileset.tiles[4].get_rect())



    window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
    pygame.display.update()

    current = Formes(L, 0)

    clock = pygame.time.Clock()
    frameCounter = 0

    grid = np.zeros((10, 20))

    while True:
        # clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # save("save.json", curent)
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                current.rotation(1)

            # if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            #     current.move(0, 1)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                current.move(-1, 0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                current.move(1, 0)

        drawInterface(screen, tileset)
        drawShape(screen, tileset, current)

        window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
        pygame.display.update()

        clock.tick(60)
        frameCounter += 1
        if frameCounter == 60:
            current.move(0, 1)
            frameCounter = 0
