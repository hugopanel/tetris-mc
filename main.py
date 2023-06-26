import pygame.freetype

from Tetris.Tileset import Tileset
from Tetris.StateMenuMain import StateMenuMain


states_stack = []

if __name__ == "__main__":
    window = pygame.display.set_mode((720, 480))
    screen = pygame.Surface((256, 240))

    pygame.init()

    tileset_file = 'tileset.png'
    tileset = Tileset(tileset_file)

    clock = pygame.time.Clock()

    pygame.font.init()
    game_font = pygame.freetype.Font("arcade-legacy.ttf", 8)

    game = {
        'window': window,
        'screen': screen,
        'tileset': tileset,
        'states_stack': states_stack,
        'clock': clock,
        'font': game_font}

    states_stack.append(StateMenuMain(game))

    while True:
        clock.tick(60)

        # Update
        states_stack[-1].update()

        # Render
        states_stack[-1].render()

        window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
        pygame.display.update()
