import pygame


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

        n_tiles_x = int(w / self.size[0])
        n_tiles_y = int(h / self.size[1])

        for y in range(0, n_tiles_y):
            for x in range(0, n_tiles_x):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x * self.size[0], y * self.size[1], *self.size))
                self.tiles.append(tile)
