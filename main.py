import pygame
from pygame.locals import *
from pygame.color import Color


class Hangman:
    WIDTH = 10
    MISTAKES = 7
    CHANCE = 0

    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen

    def update(self):
        self.draw()

    def draw(self):
        self.draw_gallows()
        if Hangman.CHANCE >= 1:
            self.draw_head()
        if Hangman.CHANCE >= 2:
            self.draw_body()
        if Hangman.CHANCE >= 3:
            self.draw_arm_one()
        if Hangman.CHANCE >= 4:
            self.draw_arm_two()
        if Hangman.CHANCE >= 5:
            self.draw_leg_one()
        if Hangman.CHANCE >= 6:
            self.draw_leg_two()

    def draw_leg_one(self):
        pygame.draw.line(self.screen, Color('red'), (200, 300), (150, 350), Hangman.WIDTH)

    def draw_leg_two(self):
        pygame.draw.line(self.screen, Color('red'), (200, 300), (250, 350), Hangman.WIDTH)

    def draw_arm_one(self):
        pygame.draw.line(self.screen, Color('red'), (150, 250), (200, 250), Hangman.WIDTH)

    def draw_arm_two(self):
        pygame.draw.line(self.screen, Color('red'), (200, 250), (250, 250), Hangman.WIDTH)

    def draw_body(self):
        pygame.draw.line(self.screen, Color('red'), (200, 200), (200, 300), Hangman.WIDTH)

    def draw_head(self):
        pygame.draw.circle(self.screen, Color('red'), (200, 200), 10, Hangman.WIDTH)

    def draw_gallows(self):
        pygame.draw.line(self.screen, Color('black'), (0, 400), (200, 400), Hangman.WIDTH)
        pygame.draw.line(self.screen, Color('black'), (100, 100), (100, 400), Hangman.WIDTH)
        pygame.draw.line(self.screen, Color('black'), (100 - Hangman.WIDTH, 100), (200 + Hangman.WIDTH, 100),
                         Hangman.WIDTH)
        pygame.draw.line(self.screen, Color('black'), (200, 100), (200, 200), Hangman.WIDTH)


class Game:
    FPS = 60
    W = 600
    H = 600

    def __init__(self):
        self.scene = []
        self.screen = pygame.display.set_mode((Game.W, Game.H))

    def awake(self):
        self.scene.append(Hangman(self))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        self.awake()
        while run:
            clock.tick(Game.FPS)
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    run = False
            self.update()

    def update(self):
        pygame.display.update()
        self.screen.fill(Color('white'))
        for gameObj in self.scene:
            gameObj.update()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pygame.quit()
        quit()


if __name__ == "__main__":
    with Game() as game:
        game.run()
