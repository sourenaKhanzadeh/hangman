import pygame
from pygame.locals import *
from pygame.color import Color


class Game:
    FPS = 60
    W = 600
    H = 600

    def __init__(self):
        self.scene = []
        self.screen = pygame.display.set_mode((Game.W, Game.H))

    def awake(self):
        pass

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(Game.FPS)
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    run = False
            self.update()

    def update(self):
        pygame.display.update()
        for gameObj in self.scene:
            gameObj.update()
        self.screen.fill(Color('white'))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pygame.quit()
        quit()


if __name__ == "__main__":
    with Game() as game:
        game.run()

