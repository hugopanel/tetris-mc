import pygame
import random


class Particule:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(1, 5)
        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_x *= 0.99
        self.speed_y *= 0.99
        self.size -= 0.05

    def draw(self, screen):
        pygame.draw.circle(
            screen, self.color, (int(self.x), int(self.y)), int(self.size)
        )

class Particules:
    def __init__(self):
        self.particles = []

    def update(self):
        for particle in self.particles:
            particle.update()

            if particle.size <= 0:
                self.particles.remove(particle)

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)

    def add(self, x, y):
        self.particles.append(Particule(x, y))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Effet de particules")
    clock = pygame.time.Clock()

    particles = Particules()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        x, y = pygame.mouse.get_pos()
        particles.add(x,y)

        screen.fill((0, 0, 0))  # Effacer l'écran

        particles.update()
        particles.draw(screen)
        
        pygame.display.flip()
        clock.tick(120)

    pygame.quit()
