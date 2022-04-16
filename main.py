import pygame
from pygame.locals import *
from pygame.color import Color
from wonderwords import RandomWord
from tkinter.ttk import *
from tkinter import Tk


class Question(Tk):
    def __init__(self, hangman):
        super().__init__()
        self.e = Entry()
        self.btn = Button(self, text="Enter", command=self.click)
        self.label = Label(text="Enter one letter please...")
        self.hangman = hangman
        self.game = hangman.game
        self.screen = hangman.screen

    def run(self):
        self.mainloop()

    def update(self):
        self.label.pack()
        self.e.pack()
        self.btn.pack()
        self.run()

    def click(self):
        word = str(self.hangman.word)
        if self.e.get() in word:
            for index in [i for i, x in enumerate(word) if x == self.e.get()]:
                self.hangman.word.bits[index] = 1
        self.destroy()


class Word:
    def __init__(self, game):
        self.random_word = RandomWord().random_words()[0]
        self.screen = game.screen
        self.game = game
        self.font = pygame.font.SysFont('calibri', 20)
        self.bits = [0 for i in range(len(self))]
        # print(pygame.font.get_fonts())

    def draw(self):
        start = 250
        for i in range(len(self)):
            end = start + i * 20 + 10
            pygame.draw.line(self.screen, Color('blue'), (start + i * 20, 100), (end, 100), 5)
            if self.bits[i]:
                text = self.font.render(self.random_word[i], False, Color('black'))
                self.screen.blit(text, (start + i * 20, 75))

    def __len__(self):
        return len(self.random_word)

    def update(self):
        self.draw()

    def __str__(self):
        return self.random_word


class Hangman:
    WIDTH = 10
    MISTAKES = 7
    CHANCE = 0

    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.word = Word(game)
        print(self.word)

    def update(self):
        self.draw()
        self.word.update()

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
        pygame.font.init()

    def awake(self):
        self.scene.append(Hangman(self))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        self.awake()
        font = pygame.font.SysFont('arial', 25)
        text = font.render("Please Enter To Type The Letter", False, Color('blue'))
        while run:
            clock.tick(Game.FPS)
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    run = False
                if ev.type == KEYDOWN:
                    if ev.key == K_n:
                        self.scene[0].word = Word(self)
                        print(self.scene[0].word)
                    if ev.key == K_RETURN:
                        Question(self.scene[0]).update()
            self.screen.blit(text, (0, 500))
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
