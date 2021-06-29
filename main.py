"""
JetBear! The Game!
v0.1
Copyright 2021 Bocifious Development
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

# set display call
win = pg.display.set_mode((width, height))


def splash():
    win.blit(splash_image, (0, 0))
    button = win.blit(start, (width / 2.60, height / 1.75))

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()
                if button.collidepoint(pos):
                    draw_window()
        pg.display.update()
    pg.quit()


def draw_window():  # function to draw on window
    win.blit(bg_image, (0, 0))  # load background image
    win.blit(bear_image, (width // 4, height // 2))  # should be sprite


if __name__ == '__main__':
    splash()
