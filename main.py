import pygame


class Tileset:
    def __init__(self, file, size=(8, 8)):
        self.file = file
        self.size = size
        self.image = pygame.image.load(file)
        # self.image = pygame.transform.scale(self.image, (self.image.get_size[0] * 3, self.image.get_size[1] * 3))
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


tileset_file = 'tileset.png'

screen = pygame.Surface((256, 240))

pygame.init()
window = pygame.display.set_mode((720, 480))

tileset = Tileset(tileset_file)
screen.blit(tileset.tiles[4], tileset.tiles[4].get_rect())

import numpy as np
interface = np.full((32, 30), 12, dtype=int)
# interface = np.full((32, 30), 1, dtype=int)

interface[3][1] = 17
interface[4][1] = 9
interface[5][1] = 9
interface[6][1] = 9
interface[7][1] = 16
interface[3][2] = 10
interface[3][3] = 10
interface[3][4] = 10
interface[3][5] = 10
interface[3][6] = 10
interface[3][7] = 10
interface[7][2] = 8
interface[7][3] = 8
interface[7][4] = 8
interface[7][5] = 8
interface[7][6] = 8
interface[7][7] = 8
interface[3][8] = 15
interface[4][8] = 7
interface[5][8] = 7
interface[6][8] = 7
interface[7][8] = 14

for row in range(0, len(interface)):
    print(row)
    for col in range(0, len(interface[row])):
        print(col)
        screen.blit(tileset.tiles[interface[row][col]], (row*8, col*8), tileset.tiles[interface[row][col]].get_rect())

window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
