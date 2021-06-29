"""
JetBear! The Game!
v0.1
Copyright 2021 Bocifious Development
"""

import pygame
import os

pygame.display.set_caption("JetBear! The Game!")
BG_IMAGE = pygame.image.load(os.path.join('assets/images', 'background_wide.png'))
SPLASH = pygame.image.load(os.path.join('assets/images', 'Splash.png'))
START = pygame.image.load(os.path.join('assets/images', 'start.png'))
WIDTH = BG_IMAGE.get_width()
HEIGHT = BG_IMAGE.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BEAR_IMAGE = pygame.image.load(os.path.join('assets/images', 'bear.png'))


def splash():
    WIN.blit(SPLASH, (0, 0))
    button = WIN.blit(START, (WIDTH / 2.60, HEIGHT / 1.75))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if button.collidepoint(pos):
                    draw_window()
        pygame.display.update()
    pygame.quit()


def draw_window():  # function to draw on window
    WIN.fill((0, 0, 0))
    WIN.blit(BG_IMAGE, (0, 0))  # load background image
    WIN.blit(BEAR_IMAGE, (WIDTH // 4, HEIGHT // 2))  # should be sprite


def main():

    run = True
    while run:  # loop to run window until user quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        splash()

    pygame.quit()


if __name__ == '__main__':
    splash()
