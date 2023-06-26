import pygame
import numpy as np


class State:
    def __init__(self, game):
        self.window: pygame.Surface
        self.screen: pygame.Surface
        self.font: pygame.font.Font

        self.game = game
        self.window = game['window']
        self.screen = game['screen']
        self.tileset = game['tileset']
        self.states_stack = game['states_stack']
        self.clock = game['clock']
        self.font = game['font']

    def update(self):
        pass

    def render(self):
        pass

    def draw_interface(self, interface):
        # On parcourt la grille d'interface pour afficher les tiles une par une
        for row in range(0, len(interface)):
            for col in range(0, len(interface[row])):
                self.screen.blit(self.tileset.tiles[interface[row][col]], (row * 8, col * 8),
                                 self.tileset.tiles[interface[row][col]].get_rect())
