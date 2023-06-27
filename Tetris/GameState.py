from Tetris.State import State
import numpy as np


class GameState(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        pass

    def render(self):
        pass

    def draw_interface(self, **interface):
        if not interface:
            interface = np.full((32, 30), 12, dtype=int)

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

        super().draw_interface(interface)

    def draw_grid(self, grid):
        for y in range(20):
            for x in range(10):
                tile = self.tileset.tiles[grid[x][y]]
                self.screen.blit(tile, ((4 + x) * 8, (7 + y) * 8), tile.get_rect())

    def draw_shape(self, shape, color, obj_x, obj_y):
        # Display shape
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                if shape[x][y]:
                    tile = self.tileset.tiles[color]

                    self.screen.blit(tile, ((obj_x + x) * 8, (obj_y + y) * 8), tile.get_rect())

    def draw_shape_object(self, shape_object):
        self.draw_shape(shape_object.shape_grid, shape_object.color, 4 + shape_object.x, 7 + shape_object.y)

    def delete_line_lower_bloc(self, grid):
        grid = np.array(grid)
        lines_to_delete = 1 * np.all(grid != 12, axis=0)
        lines_to_delete = np.where(lines_to_delete == 1)[0]
        grid = np.delete(grid, lines_to_delete, axis=1)
        for _ in lines_to_delete:
            grid = np.hstack((np.array([12 for _ in range(10)])[:, np.newaxis], grid))
        return grid, lines_to_delete
