"""
JetBear! The Game!
v0.1
Copyright 2021 Patrick Bruso
"""

import pygame as pg
import os

pg.display.set_caption("JetBear! The Game!")

# load assets
bg_image = pg.image.load(os.path.join('assets/images', 'background_wide.png'))
splash_image = pg.image.load(os.path.join('assets/images', 'Splash.png'))
start = pg.image.load(os.path.join('assets/images', 'start.png'))
bear_image = pg.image.load(os.path.join('assets/images', 'bear.png'))

# constants
width = bg_image.get_width()
height = bg_image.get_height()
FPS = 60

# set display call
win = pg.display.set_mode((width, height))


# Thoughts: How about adding a move() function
# With only one movement key (Spacebar)
# if KeyPressed is Spacebar Move Up
# else move down?
# This is similar to a game called Jetpack Joyride

class Bear(object):
    def __init__(self):
        self.image = bear_image
        self.x = width / 4
        self.y = height / 2

    def key_handle(self):
        key = pg.key.get_pressed()
        dist = 1  # change if movement too slow
        if key[pg.K_DOWN]:
            self.y += dist
        elif key[pg.K_UP]:
            self.y -= dist
        elif key[pg.K_RIGHT]:
            self.x += dist
        elif key[pg.K_LEFT]:
            self.x -= dist

        # add logic to not increase distance if hit ground or border 
        # (This should probably be another function called checkBorders)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


def main():
    """
    Main game loop that implements splash screen and calls game function upon button click
    """
    win.blit(splash_image, (0, 0))
    button = win.blit(start, (width / 2.60, height / 1.75))
    clock = pg.time.Clock()
    bear = Bear()

    isRunning = True
    isStartPressed = False
    while isRunning:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                isRunning = False

            #This checks if startbutton is pressed
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()
                if button.collidepoint(pos):  
                    isStartPressed = True;

        if isStartPressed == True:
            win.blit(bg_image, (0, 0))
            bear.key_handle()
            bear.draw(win)
        else:
            #insert splash screen animation logic
        
        pg.display.update()


    pg.quit()


if __name__ == '__main__':
    main()
