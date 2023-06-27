from Tetris.State import *
from Tetris.StateGameMain import StateGameMain
from Tetris.StateGameTimeTrial import StateGameTimeTrial
from Tetris.StateGameChallenges import StateGameChallenges

import os
import json


class StateMenuMain(State):
    def __init__(self, game):
        super().__init__(game)
        self.selection = 0
        self.items = ["Mode classique", "Temps contre la montre", "Défis", "Charger partie"]

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
                    self.states_stack.append(StateGameMain(self.game))
                elif self.selection == 1:
                    self.states_stack.append(StateGameTimeTrial(self.game))
                elif self.selection == 2:
                    self.states_stack.append(StateGameChallenges(self.game))
                else:
                    # Chargement de la dernière partie
                    if os.path.isfile("save.json"):
                        if os.stat("save.json").st_size != 0:
                            f = open("save.json", "r")
                            data_json = json.loads(f.read())
                            f.close()
                            if data_json['gamemode'] == 'classic':
                                class_to_load = StateGameMain
                            elif data_json['gamemode'] == 'timetrials':
                                class_to_load = StateGameTimeTrial
                            elif data_json['gamemode'] == 'challenges':
                                class_to_load = StateGameChallenges
                            else:
                                class_to_load = StateGameMain
                            self.states_stack.append(class_to_load(self.game, data_json['score'],
                                                                   data_json['multiplier'], data_json['grid'],
                                                                   data_json['current_speed'],
                                                                   data_json['current_tetromino'],
                                                                   data_json['next_tetromino'],
                                                                   data_json['frame_counter']))
        self.selection %= len(self.items)

    def render(self):
        self.draw_interface(interface=np.full((32, 30), 12, dtype=int))
        self.screen.blit(self.font.render(self.items[self.selection], (255, 255, 255))[0], (10, 10))