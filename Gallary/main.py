'''
import random #For generating random numbers
import sys # we will use sys.exit to exit the program
import pygame
#import pygame.locals import * # Basic pygame imports
from pygame.locals import * # Basic pygame imports

# Globals Variables for the game
FPS = 50
ScreenWidth = 289
ScreenHeight = 511
Screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
GroundY = ScreenHeight * 0.8
Game_Photos = {}
Game_Sound = {}
Player = '/gallery/Photos/Bird.jpg'
Background = '/gallery/Photos/Background.png'
Pipe = '/gallery/Photos/pipe.png'

if __name__ == "__main__":
    #This will be main point from where our game will start
    pygame.init() #initialize all pygame modules 
    FPSCLOCK = pygame.time.CLock()
    pygame.display.set_caption('Flappy Bird by Rehan')
    Game_Photos['numbers'] = (
        pygame.image.load('/gallery/Photos/0.png').covert_alpha(), #To optimize the image for game
        pygame.image.load('/gallery/Photos/1.jpg').covert_alpha(),
        pygame.image.load('/gallery/Photos/2.png').covert_alpha(),
        pygame.image.load('/gallery/Photos/3.jpg').covert_alpha(),
        pygame.image.load('/gallery/Photos/4.jpg').covert_alpha(),
        pygame.image.load('/gallery/Photos/5.jpg').covert_alpha(),
        pygame.image.load('/gallery/Photos/6.png').covert_alpha(),
        pygame.image.load('/gallery/Photos/7.png').covert_alpha(),
        pygame.image.load('/gallery/Photos/8.png').covert_alpha(),
        pygame.image.load('/gallery/Photos/9.jpg').covert_alpha(),
    )
'''