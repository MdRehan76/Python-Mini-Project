import random #For generating random numbers
import sys # we will use sys.exit to exit the program
import pygame
#import pygame.locals import * # Basic pygame imports
from pygame.locals import * # Basic pygame imports

# Globals Variables for the game
FPS = 32
ScreenWidth = 409
ScreenHeight = 593
Screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
GroundY = ScreenHeight * 0.8 #For Base
Game_Photos = {}
Game_Sound = {}
Player = 'Gallery/Photos/Bird.png'
Background = 'Gallery/Photos/Background.jpg'
Pipe = 'Gallery/Photos/pipe.png'

def welcomeScreen():
    """
    Shows Welcome Images on the screen 
    """ 
    messagex = int((ScreenHeight - Game_Photos['message'].get_width())/13)
    messagey = int(ScreenHeight*0.1)
    PlayerX = int(ScreenWidth/7)
    PlayerY = int((ScreenHeight - Game_Photos['Player'].get_height())/2)
    basex = 0

    while True:
        for event in pygame.event.get():
            #if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return 
            else:
                Screen.blit(Game_Photos['Background'],(0,0)) 
                Screen.blit(Game_Photos['Player'],(PlayerX + 125,PlayerY + 20)) 
                Screen.blit(Game_Photos['message'],(messagex,messagey)) 
                Screen.blit(Game_Photos['Base'],(basex,GroundY )) 
                pygame.display.update()
                FPSCLOCK.tick(FPS) # To Control the game FPS
def mainGame():
    score = 0
    playerx = int(ScreenWidth/5)
    playery = int(ScreenWidth/2)
    basex = 0
    


if __name__ == "__main__":
    #This will be main point from where our game will start
    pygame.init() #initialize all pygame modules 
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by Rehan')
    Game_Photos['numbers'] = (
        pygame.image.load('Gallery/Photos/0.png').convert_alpha(), #To optimize the image for game
        pygame.image.load('Gallery/Photos/1.png').convert_alpha(),
        pygame.image.load('Gallery/Photos/2.png').convert_alpha(),
        pygame.image.load('Gallery/Photos/3.png').convert_alpha(),
        pygame.image.load('Gallery/Photos/4.png').convert_alpha(),
        pygame.image.load('Gallery/Photos/5.png').convert_alpha(),
        pygame.image.load('Gallery/Photos/6.png').convert_alpha(),
        pygame.image.load('Gallery/Photos/7.png').convert_alpha(),
        pygame.image.load('Gallery/Photos/8.png').convert_alpha(),
        pygame.image.load('Gallery/Photos/9.png').convert_alpha(),
    )

    Game_Photos['message'] = pygame.image.load('Gallery/Photos/message.png').convert_alpha()
    Game_Photos['Base'] = pygame.image.load('Gallery/Photos/Base.png').convert_alpha()
    Game_Photos['Pipe'] = (
        pygame.transform.rotate(pygame.image.load( Pipe).convert_alpha(), 180),
        pygame.image.load( Pipe).convert_alpha()
        )
    Game_Sound['Die'] = pygame.mixer.Sound('Gallery/Sound/Die.mp3')
    Game_Sound['Hit'] = pygame.mixer.Sound('Gallery/Sound/Hit.mp3')
    Game_Sound['Point'] = pygame.mixer.Sound('Gallery/Sound/Point.mp3')
    Game_Sound['Swoosh'] = pygame.mixer.Sound('Gallery/Sound/Swoosh.mp3')
    Game_Sound['Wing'] = pygame.mixer.Sound('Gallery/Sound/Wing.mp3')

        
    Game_Photos['Background'] = pygame.image.load(Background).convert()
    Game_Photos['Player'] = pygame.image.load(Player).convert_alpha()

    while True: 
        welcomeScreen() #Shows welcome Screen to the user until he presses a button
        mainGame() #This is the main Game Function 
        