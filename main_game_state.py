import random

import numpy as np
import pygame


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

    def try_rotate(self, grid, pas=1):
        """
        Essaye d'effectuer une rotation avec rotate().
        :param grid: Grille de jeu
        :param pas: Nombre de rotations de 90° à effectuer
        :return: Vrai si la rotation est possible, Faux sinon.
        """
        new_forme = np.rot90(self.forme, pas)
        if self.check_collisions(new_forme, (self.x, self.y), grid):
            self.forme = new_forme
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
        return self.check_collisions(self.forme, (newX, newY), grid)

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


class State:
    def __init__(self, game):
        self.game = game
        self.window: pygame.Surface
        self.screen: pygame.Surface
        self.font: pygame.font.Font
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
        self.draw_shape(shape_object.forme, shape_object.color, 4 + shape_object.x, 7 + shape_object.y)

    def delete_line_lower_bloc(self, grid):
        grid = np.array(grid)
        lines_to_delete = 1 * np.all(grid != 12, axis=0)
        lines_to_delete = np.where(lines_to_delete == 1)[0]
        grid = np.delete(grid, lines_to_delete, axis=1)
        for _ in lines_to_delete:
            grid = np.hstack((np.array([12 for _ in range(10)])[:, np.newaxis], grid))
        return grid, len(lines_to_delete)


class MainMenu(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.states_stack.append(MainGame(self.game))

    def render(self):
        self.draw_interface(interface=np.full((32, 30), 12, dtype=int))
        self.screen.blit(self.font.render("Bienvenue sur Tetris", (255, 255, 255))[0], (10, 10))


class MainGame(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.current_shape = Formes(random.choice(list(shapes.values())), random.choice(colors))
        self.next_shape = Formes(random.choice(list(shapes.values())), random.choice(colors))

        self.frame_counter = 0
        self.score = 0
        self.multiplier = 1

        self.score_for_new_shape_placed = 100  # Le score à ajouter pour chaque nouvelle forme placée
        self.multiplier_for_new_shape_placed = 0.01  # Le multiplieur à multiplier pour chaque nouvelle forme placée.
        self.score_for_line_removed = 1000  # Le score à ajouter pour chaque ligne supprimée
        self.multiplier_for_line_removed = 0.1  # Le multiplieur à multiplier pour chaque ligne supprimée.

        self.max_speed = 7
        self.min_speed = 40
        self.current_speed = self.min_speed

        self.grid = np.full((10, 20), 12, dtype=int)

        self.lock_movements = False

    def update(self):
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if not self.lock_movements:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    if not self.current_shape.try_rotate(self.grid, 1):
                        if self.current_shape.x < 5:
                            self.current_shape.try_move(1, 0, self.grid)
                        else:
                            self.current_shape.try_move(-1, 0, self.grid)
                        self.current_shape.try_rotate(self.grid, 1)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.current_shape.try_move(-1, 0, self.grid)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.current_shape.try_move(1, 0, self.grid)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    while self.current_shape.try_move(0, 1, self.grid):
                        pass
                    self.lock_movements = True  # On bloque les mouvements latéraux.

        self.frame_counter += 1
        if self.frame_counter >= self.current_speed:
            self.lock_movements = False  # On débloque les mouvements (si on a appuyé sur la flèche du bas)

            if not self.current_shape.try_move(0, 1, self.grid):
                # On ne peut pas bouger la forme vers le bas.
                # On vérifie si la forme est par-dessus des blocs, auquel cas le joueur a perdu
                if not self.current_shape.try_move(0, 0, self.grid) and self.current_shape.y == 0:
                    # Game over
                    print("Game Over!")
                    self.states_stack.pop()
                    return

                self.score += self.score_for_new_shape_placed * self.multiplier
                self.multiplier += self.multiplier * self.multiplier_for_new_shape_placed

                # On ajoute la forme à la grille et on la supprime.
                # Pour ça, on parcourt la forme pour voir où il y a des blocs
                for y in range(len(self.current_shape.forme)):
                    for x in range(len(self.current_shape.forme[y])):
                        if self.current_shape.forme[x][y]:
                            # Il y a un bloc, on l'ajoute
                            self.grid[self.current_shape.x + x][self.current_shape.y + y] = self.current_shape.color
                self.grid, n_lines_removed = self.delete_line_lower_bloc(self.grid)

                self.score += self.score_for_line_removed * self.multiplier * n_lines_removed * 1.5
                self.multiplier += self.multiplier * self.multiplier_for_line_removed * n_lines_removed

                # On supprime la forme et on en ajoute une nouvelle
                del self.current_shape
                self.current_shape = self.next_shape
                self.next_shape = Formes(random.choice(list(shapes.values())), random.choice(colors))

                print("Score", self.score, "Multiplier", self.multiplier)

                if self.current_speed > self.max_speed:
                    self.current_speed -= self.current_speed * 0.1
                print("Speed", self.current_speed)

            self.frame_counter = 0

    def render(self):
        self.draw_interface()  # Affichage de l'interface
        self.draw_grid(self.grid)  # Affichage de la grille
        self.draw_shape_object(self.current_shape)  # Affichage de la forme actuelle
        self.draw_shape(self.next_shape.forme, self.next_shape.color, 19, 7)  # Affichage de la prochaine forme

