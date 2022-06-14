"""
JetBear! The Game!
v1.0
Copyright 2021 Patrick Bruso
"""

import pygame as pg
import os

# Load and name assets
BACKGROUND_IMAGE = pg.image.load(os.path.join('assets/images', 'bgtop.png'))
SPLASH_IMAGE = pg.image.load(os.path.join('assets/images', 'Splash.png'))
START_BUTTON = pg.image.load(os.path.join('assets/images', 'start.png'))
BEAR_JETPACK_ON = pg.image.load(os.path.join('assets/images', 'bear.png'))
BEAR_JETPACK_OFF = pg.image.load(os.path.join('assets/images', 'idle.png'))
FOREGROUND_IMAGE = pg.image.load(os.path.join('assets/images', 'bgbottom.png'))

# Constants
WIDTH = BACKGROUND_IMAGE.get_width()
HEIGHT = BACKGROUND_IMAGE.get_height()
FPS = 60 # Test gravity with different FPS

# Set game window caption
pg.display.set_caption("JetBear! The Game!")

# Set display call
win = pg.display.set_mode((WIDTH, HEIGHT))


class Bear(object):
    def __init__(self):
        self.image = BEAR_IMAGE
        self.x = WIDTH / 4
        self.y = HEIGHT / 2

    def key_handle(self):
        key = pg.key.get_pressed()
        dist = 4  # change if movement too slow
        if key[pg.K_DOWN]:
            self.y += dist
        elif key[pg.K_UP]:
            self.y -= dist
        elif key[pg.K_RIGHT]:
            self.x += dist
        elif key[pg.K_LEFT]:
            self.x -= dist

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        pg.display.update()  # testing update within Bear class


class Foreground:
    VEL = 0.5 # Base velocity movement
    WIDTH = FOREGROUND_IMAGE.get_width()
    IMG = FOREGROUND_IMAGE

    def __init__(self) -> None:
        self.y = 0
        self.x1 = 0
        self.x2 = self.WIDTH
        self.vel = 0
    
    def move(self, vel = VEL):
        self.x1 -= vel
        self.x2 -= vel

        if (self.x1 + self.WIDTH < 0):
            self.x1 = self.x2 + self.WIDTH
        
        if (self.x2 + self.WIDTH < 0):
            self.x2 = self.x1 + self.WIDTH
    
    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))


def main():
    """
    Main game loop that implements splash screen and calls game function upon button click
    """
    win.blit(SPLASH_IMAGE, (0, 0))
    # Move below
    button = win.blit(START_BUTTON, (WIDTH / 2.60, HEIGHT / 1.75))
    clock = pg.time.Clock()
    bear = Bear()

    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()
                if button.collidepoint(pos):
                    win.blit(BACKGROUND_IMAGE, (0, 0))

        bear.draw(win)
        bear.key_handle()
        pg.display.update()

    pg.quit()


if __name__ == '__main__':
    main()
