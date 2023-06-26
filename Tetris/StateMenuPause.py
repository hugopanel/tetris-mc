from Tetris.State import *

import json


class PauseMenu(State):
    def __init__(self, game):
        super().__init__(game)
        self.selection = 0
        self.items = ["Continue", "Save and quit", "Quit without saving"]

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.selection += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.selection -= 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.continue_game()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Handle key presses
                if self.selection == 0:
                    self.continue_game()
                elif self.selection == 1:
                    self.save_and_quit()
                else:
                    self.quit_without_saving()

        self.selection %= len(self.items)

    def render(self):
        self.draw_interface(np.full((32, 30), 12, dtype=int))
        self.screen.blit(self.font.render(self.items[self.selection], (255, 255, 255))[0], (10, 10))

    def continue_game(self):
        self.states_stack.pop()

    def quit_without_saving(self):
        self.states_stack.pop()
        self.states_stack.pop()

    def save_and_quit(self):
        # Sauvegarder
        f = open("save.json", "w")
        f.write(json.dumps(self.states_stack[-2].__dict__(), indent=4))
        f.close()

        # Quitter
        self.quit_without_saving()