from Tetris.Tetromino import *
from Tetris.GameState import GameState
from Tetris.StateMenuPause import StateMenuPause
from Tetris.StateMenuPost import StateMenuPost

import random
import pygame


class StateGameChallenges(GameState):
    def __init__(self, game, score: int = 0, multiplier: int = 1, grid: np.array = None, current_speed: int = None,
                 current_tetromino: dict = None, next_tetromino: dict = None, frame_counter: int = 0):
        super().__init__(game)
        if current_tetromino:
            self.current_tetromino = Tetromino(current_tetromino['name'], current_tetromino['color'],
                                               current_tetromino['rotation'], current_tetromino['x'],
                                               current_tetromino['y'])
        else:
            self.current_tetromino = Tetromino(random.choice(list(shapes.items()))[0], random.choice(colors))

        if next_tetromino:
            self.next_tetromino = Tetromino(next_tetromino['name'], next_tetromino['color'], next_tetromino['rotation'],
                                            next_tetromino['x'], next_tetromino['y'])
        else:
            self.next_tetromino = Tetromino(random.choice(list(shapes.items()))[0], random.choice(colors))

        self.frame_counter = frame_counter
        self.score = score
        self.multiplier = multiplier

        self.score_for_new_shape_placed = 100  # Le score à ajouter pour chaque nouvelle forme placée
        self.multiplier_for_new_shape_placed = 0.01  # Le multiplieur à multiplier pour chaque nouvelle forme placée.
        self.score_for_line_removed = 1000  # Le score à ajouter pour chaque ligne supprimée
        self.multiplier_for_line_removed = 0.1  # Le multiplieur à multiplier pour chaque ligne supprimée.
        self.score_challenge_completed = 5000  # Le score à ajouter à chaque défi terminé

        self.max_speed = 7
        self.min_speed = 40
        self.current_speed = current_speed if current_speed else self.min_speed

        self.grid = grid if grid else np.full((10, 20), 12, dtype=int)

        self.lock_movements = False

        self.challenges = ['score 300 one-shot', '4 lines one-shot',
                           '3 lines in a row']
        self.current_challenge = 0
        self.lines_removed_streak = 0  # Nombre de lignes supprimées d'affilée

    def update(self):
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if not self.lock_movements:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    if not self.current_tetromino.try_rotate(self.grid, 1):
                        if self.current_tetromino.x < 5:
                            self.current_tetromino.try_move(1, 0, self.grid)
                        else:
                            self.current_tetromino.try_move(-1, 0, self.grid)
                        self.current_tetromino.try_rotate(self.grid, 1)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.current_tetromino.try_move(-1, 0, self.grid)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.current_tetromino.try_move(1, 0, self.grid)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    while self.current_tetromino.try_move(0, 1, self.grid):
                        pass
                    self.lock_movements = True  # On bloque les mouvements latéraux.
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.states_stack.append(StateMenuPause(self.game))

        self.frame_counter += 1
        if self.frame_counter >= self.current_speed:
            self.lock_movements = False  # On débloque les mouvements (si on a appuyé sur la flèche du bas)

            if not self.current_tetromino.try_move(0, 1, self.grid):
                # On ne peut pas bouger la forme vers le bas.
                # On vérifie si la forme est par-dessus des blocs, auquel cas le joueur a perdu
                if not self.current_tetromino.try_move(0, 0, self.grid) and self.current_tetromino.y == 0:
                    # Game over
                    print("Game Over!")
                    self.states_stack.append(StateMenuPost(self.game, self.score, 'challenges'))
                    return

                score_to_add = self.score_for_new_shape_placed * self.multiplier
                self.multiplier += self.multiplier * self.multiplier_for_new_shape_placed

                # On ajoute la forme à la grille et on la supprime.
                # Pour ça, on parcourt la forme pour voir où il y a des blocs
                for y in range(len(self.current_tetromino.shape_grid)):
                    for x in range(len(self.current_tetromino.shape_grid[y])):
                        if self.current_tetromino.shape_grid[x][y]:
                            # Il y a un bloc, on l'ajoute
                            self.grid[self.current_tetromino.x + x][
                                self.current_tetromino.y + y] = self.current_tetromino.color
                self.grid, lines_removed = self.delete_line_lower_bloc(self.grid)
                n_lines_removed = len(lines_removed)
                if self.current_challenge == 2:
                    if n_lines_removed == 0:
                        self.lines_removed_streak = 0
                    else:
                        self.lines_removed_streak += 1
                    if self.lines_removed_streak >= 3:
                        self.score += self.score_challenge_completed
                        self.current_challenge += 1
                        print("NEXT CHALLENGE")
                        print("Current challenge", self.current_challenge)

                if self.current_challenge == 1 and n_lines_removed >= 4:
                    self.current_challenge += 1
                    self.score += self.score_challenge_completed

                score_to_add += self.score_for_line_removed * self.multiplier * n_lines_removed * 1.5
                self.score += score_to_add
                self.multiplier += self.multiplier * self.multiplier_for_line_removed * n_lines_removed

                print(score_to_add)
                # Challenge 0 (300 points d'un coup)
                if self.current_challenge == 0 and score_to_add >= 300:
                    self.current_challenge += 1
                    self.score += self.score_challenge_completed

                # On supprime la forme et on en ajoute une nouvelle
                del self.current_tetromino
                self.current_tetromino = self.next_tetromino
                self.next_tetromino = Tetromino(random.choice(list(shapes.items()))[0], random.choice(colors))

                print("Score", self.score, "Multiplier", self.multiplier)

                if self.current_speed > self.max_speed:
                    self.current_speed -= self.current_speed * 0.01
                print("Speed", self.current_speed)

            self.frame_counter = 0
            self.current_challenge %= len(self.challenges)
            print("Streak", self.lines_removed_streak)
            print("Current challenge", self.current_challenge)

    def render(self):
        self.draw_interface()  # Affichage de l'interface
        self.draw_grid(self.grid)  # Affichage de la grille
        self.draw_shape_object(self.current_tetromino)  # Affichage de la forme actuelle
        self.draw_shape(self.next_tetromino.shape_grid, self.next_tetromino.color, 19,
                        7)  # Affichage de la prochaine forme

        # Affichage du défi actuel
        self.screen.blit(self.font.render("Challenge: " + self.challenges[self.current_challenge], (255, 255, 255))[0], (10, 10))

    def draw_interface(self, **interface):
        super().draw_interface(**interface)
        self.screen.blit(self.font.render("Score: " + str(round(self.score)), (255, 255, 255))[0], (130, 100))

    def __dict__(self) -> dict:
        return {
            'gamemode': 'challenges',
            'score': self.score,
            'multiplier': self.multiplier,
            'grid': self.grid.tolist(),
            'current_speed': self.current_speed,
            'current_tetromino': self.current_tetromino.__dict__(),
            'next_tetromino': self.next_tetromino.__dict__(),
            'frame_counter': self.frame_counter
        }
