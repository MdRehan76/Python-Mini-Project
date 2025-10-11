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
Player = 'Gallery/Photos/Bird.jpg'
Background = 'Gallery/Photos/Background.jpg'
Pipe = 'Gallery/Photos/pipe.png'

if __name__ == "__main__":
    #This will be main point from where our game will start
    pygame.init() #initialize all pygame modules 
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by Rehan')
    Game_Photos['numbers'] = (
        pygame.image.load('Gallery/Photos/0.png').convert_alpha(), #To optimize the image for game
        pygame.image.load('Gallery/Photos/1.jpg').convert_alpha(),
        pygame.image.load('Gallery/Photos/2.png').convert_alpha(),
        pygame.image.load('Gallery/Photos/3.jpg').convert_alpha(),
        pygame.image.load('Gallery/Photos/4.jpg').convert_alpha(),
        pygame.image.load('Gallery/Photos/5.jpg').convert_alpha(),
        pygame.image.load('Gallery/Photos/6.png').convert_alpha(),
        pygame.image.load('Gallery/Photos/7.png').convert_alpha(),
        pygame.image.load('Gallery/Photos/8.png').convert_alpha(),
        pygame.image.load('Gallery/Photos/9.jpg').convert_alpha(),
    )

    Game_Photos['message'] = pygame.image.load('Gallery/Photos/message.png').convert_alpha()
    Game_Photos['Base'] = pygame.image.load('Gallery/Photos/Base.jpg').convert_alpha()
    Game_Photos['Pipe'] = (
        pygame.transform.rotate(pygame.image.load( Pipe).convert_alpha(), 180),
        pygame.image.load( Pipe).convert_alpha()
        )
    Game_Sound['Die'] = pygame.mixer.sound('Gallery/Sound/Die.mp3')
    Game_Sound['Hit'] = pygame.mixer.sound('Gallery/Sound/Hit.mp3')
    Game_Sound['Point'] = pygame.mixer.sound('Gallery/Sound/Point.mp3')
    Game_Sound['Swoosh'] = pygame.mixer.sound('Gallery/Sound/Swoosh.mp3')
    Game_Sound['Wing'] = pygame.mixer.sound('Gallery/Sound/Wing.mp3')
