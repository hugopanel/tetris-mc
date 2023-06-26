from Tetris.State import *

import os
import json


class PostGame(State):
    def __init__(self, game, score, gamemode='classic'):
        super().__init__(game)
        self.score = score
        self.gamemode = gamemode

        self.text_input = ""

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.dict['unicode'] == '\x08':  # Touche retour (effacer)
                    self.text_input = self.text_input[:-1]
                elif event.dict['unicode'] == '\r':  # Touche entrer
                    # On sauvegarde le score

                    # On lit les scores précédents
                    if not os.path.isfile("scores.json"):
                        f = open("scores.json", 'x')
                        scores = []
                    else:
                        f = open("scores.json", "r")
                        scores = json.loads(f.read())
                    f.close()

                    scores.append({'nom': self.text_input, 'score': self.score, 'gamemode': self.gamemode})

                    f = open("scores.json", "w")
                    f.write(json.dumps(scores, indent=4))
                    f.close()

                    self.states_stack.pop()
                    self.states_stack.pop()
                else:
                    if len(self.text_input) < 10:
                        self.text_input += event.dict['unicode']

    def render(self):
        self.draw_interface(np.full((32, 30), 12, dtype=int))
        self.screen.blit(self.font.render("Saisissez votre nom", (255, 255, 255))[0], (10, 10))
        self.screen.blit(self.font.render(self.text_input, (255, 255, 255))[0], (10, 30))