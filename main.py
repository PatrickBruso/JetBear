"""
JetBear! The Game!
v0.1
Copyright 2021 Bocifious Development
"""

import pygame
import os

pygame.display.set_caption("JetBear! The Game!")
BG_IMAGE = pygame.image.load(os.path.join('assets/images', 'background_wide.png'))
WIDTH = BG_IMAGE.get_width()
HEIGHT = BG_IMAGE.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BEAR_IMAGE = pygame.image.load(os.path.join('assets/images', 'bear.png'))


def draw_window():  # function to draw on window
    WIN.blit(BG_IMAGE, (0, 0))  # load background image
    WIN.blit(BEAR_IMAGE, (WIDTH // 4, HEIGHT // 2))  # should be sprite
    pygame.display.update()  # update the window


def main():

    run = True
    while run:  # loop to run window until user quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
