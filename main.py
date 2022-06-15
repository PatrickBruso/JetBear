"""
JetBear! The Game!
v1.0
Copyright 2021 Patrick Bruso
"""

import pygame as pg
from pygame import mixer
import os

# Load and name assets
BACKGROUND_IMAGE = pg.image.load(os.path.join('assets/images', 'bgtop.png'))
SPLASH_IMAGE = pg.image.load(os.path.join('assets/images', 'Splash.png'))
START_BUTTON = pg.image.load(os.path.join('assets/images', 'start.png'))
BEAR_JETPACK_ON = pg.image.load(os.path.join('assets/images', 'bear.png'))
BEAR_JETPACK_OFF = pg.image.load(os.path.join('assets/images', 'idle.png'))
FOREGROUND_IMAGE = pg.image.load(os.path.join('assets/images', 'bgbottom.png'))

# Prepare music assets for loading in main function
SPLASH_MUSIC = os.path.join('assets/audio', 'intro.mp3')
GAME_MUSIC = os.path.join('assets/audio', 'game.mp3')

# Constants
WIDTH = BACKGROUND_IMAGE.get_width()
HEIGHT = BACKGROUND_IMAGE.get_height()
FPS = 60 # Test gravity with different FPS

# Set game window caption
pg.display.set_caption("JetBear! The Game!")

# Set display call
win = pg.display.set_mode((WIDTH, HEIGHT))


class Bear:
    def __init__(self):
        self.image = BEAR_JETPACK_ON
        self.x = WIDTH / 4
        self.y = HEIGHT / 2
        self.y_change = 0
        self.start_gravity()
    
    def check_border(self):
        # Logic to prevent bear from moving outside game window
        if self.x < 0:
            self.x = 0
        elif self.x > 900:
            self.x = 900
        
        if self.y < 0:
            self.y = 0
        elif self.y > 300:
            self.y = 300

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
        
        self.check_border()
    
    def move(self):
        self.y += self.y_change
        self.check_border()
    
    def start_jetpack(self):
        self.image = BEAR_JETPACK_ON
        self.y_change = -6
    
    def start_gravity(self):
        self.image = BEAR_JETPACK_OFF
        self.y_change = 8

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Foreground:
    """
    A class used to draw and move the game's foreground.

    ...

    Attributes
    ----------
    y : int
        The y-axis value of the foreground image
    x1 : int
        The beginning x-axis value of the foreground image
    x2 : int
        The ending x-axis value of the foreground image
    vel : int
        The velocity of the foreground image moving right to left
    
    Methods
    --------
    move(vel=VEL)
        Moves the foreground image from right side to left side for parallax effect
    
    draf(win)
        Draws the foreground image on the game canvas
    """

    # Class constants
    VEL = 0.5 # Foreground velocity movement
    WIDTH = FOREGROUND_IMAGE.get_width()
    IMG = FOREGROUND_IMAGE

    def __init__(self) -> None:
        """
        There are no parameters because the values do not change and are hard-coded below
        """

        self.y = 0
        self.x1 = 0
        self.x2 = self.WIDTH
        self.vel = 0 # Not sure this is needed?
    
    def move(self, vel=VEL):
        """
        Moves the foreground image on the game canvas from right to left,
        giving the canvas a parallax effect.

        Parameters
        -----------
        vel: int, optional
            The value of the foreground movement velocity
        """

        self.x1 -= vel
        self.x2 -= vel

        if (self.x1 + self.WIDTH < 0):
            self.x1 = self.x2 + self.WIDTH
        
        if (self.x2 + self.WIDTH < 0):
            self.x2 = self.x1 + self.WIDTH
    
    def draw(self, win):
        """
        Draws the foreground on to the game canvas.

        Parameters
        ----------
        win : Any
            pygame window display call 
        """

        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))


class Background:
    """
    A class used to draw and move the game's background.

    ...

    Attributes
    ----------
    y : int
        The y-axis value of the background image
    x1 : int
        The beginning x-axis value of the background image
    x2 : int
        The ending x-axis value of the background image
    
    Methods
    --------
    move(vel=VEL)
        Moves the background image from right side to left side for parallax effect
    
    draf(win)
        Draws the background image on the game canvas
    """

    # Class constants
    VEL = 2
    WIDTH = BACKGROUND_IMAGE.get_width()
    IMG = BACKGROUND_IMAGE

    def __init__(self) -> None:
        """
        There are no parameters because the values do not change and are hard-coded below
        """

        self.y = 0
        self.x1 = 0
        self.x2 = self.WIDTH
    
    def move(self, vel=VEL):
        """
        Moves the background image on the game canvas from right to left,
        giving the canvas a parallax effect.

        Parameters
        -----------
        vel: int, optional
            The value of the background movement velocity
        """

        self.x1 -= vel
        self.x2 -= vel

        if (self.x1 + self.WIDTH < 0):
            self.x1 = self.x2 + self.WIDTH
        
        if (self.x2 + self.WIDTH < 0):
            self.x2 = self.x1 + self.WIDTH
    
    def draw(self, win):
        """
        Draws the background on to the game canvas.

        Parameters
        ----------
        win : Any
            pygame window display call 
        """

        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))


def main():
    """
    Main game loop that implements splash screen and calls game function upon button click
    """
    win.blit(SPLASH_IMAGE, (0, 0)) # Move to splash logic section to have moving background?

    # Initialize, load, and play splash screen music (fix needed - stop when start button pressed)
    mixer.init()
    mixer.music.load(SPLASH_MUSIC)
    mixer.music.play()

    button = win.blit(START_BUTTON, (WIDTH / 2.60, HEIGHT / 1.75)) # Move to splash logic section for moving background?

    # Start clock
    clock = pg.time.Clock()

    # Load class instances
    bear = Bear()
    foreground = Foreground()
    background = Background()

    # Set variables for game run and start button pressed
    run = True
    start_pressed = False

    # Main game loop
    while run:
        clock.tick(FPS) # Change to see effect?

        # Event handler
        for event in pg.event.get():
            # Quit event
            if event.type == pg.QUIT:
                run = False
            
            # Check if start button pressed and set to True if pressed
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()
                if button.collidepoint(pos):
                    start_pressed = True
            
            # Jetpack logic (move to Bear class?)
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                bear.start_jetpack()
            elif event.type == pg.KEYUP and event.key == pg.K_SPACE:
                bear.start_gravity()

        # Logic for main game when start button pressed
        if start_pressed == True:
            win.blit(BACKGROUND_IMAGE, (0, 0))
            background.move()
            background.draw(win)
            foreground.move()
            foreground.draw(win)
            bear.move()
            bear.key_handle()
            bear.draw(win)
            mixer.music.load(GAME_MUSIC) # Not working
            mixer.music.play() # Not working

        # Logic for Splash screen
        else:
            foreground.move()
            foreground.draw(win)

        # Display update to refresh screen
        pg.display.update()

    pg.quit()


if __name__ == '__main__':
    main()
