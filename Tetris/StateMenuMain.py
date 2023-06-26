from Tetris.State import *
from Tetris.StateGameMain import MainGame

import os
import json


class MainMenu(State):
    def __init__(self, game):
        super().__init__(game)
        self.selection = 0
        self.items = ["Nouvelle partie", "Charger partie"]

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.selection += 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.selection -= 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if self.selection == 0:
                    self.states_stack.append(MainGame(self.game))
                elif self.selection == 1:
                    # Chargement de la derniere partie
                    if os.path.isfile("save.json"):
                        if os.stat("save.json").st_size != 0:
                            f = open("save.json", "r")
                            data_json = json.loads(f.read())
                            f.close()
                            self.states_stack.append(MainGame(self.game, data_json['score'], data_json['multiplier'],
                                                              data_json['grid'], data_json['current_speed'],
                                                              data_json['current_tetromino'],
                                                              data_json['next_tetromino'],
                                                              data_json['frame_counter']))
        self.selection %= len(self.items)

    def render(self):
        self.draw_interface(interface=np.full((32, 30), 12, dtype=int))
        self.screen.blit(self.font.render(self.items[self.selection], (255, 255, 255))[0], (10, 10))