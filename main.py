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
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
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
    
    #Create new pipe 2 pipes on screen ( up and down )
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()
    
    #My list of upper pipes
    upperPipes = [
        {'x' : ScreenWidth + 200, 'y' : newPipe1[0]['y']},
        {'x' : ScreenWidth + 200+ (ScreenWidth/2), 'y' : newPipe2[0]['y']}
    ]
    #My list of lower pipes
    lowerPipes = [
        {'x' : ScreenWidth + 200, 'y' : newPipe1[1]['y']},
        {'x' : ScreenWidth + 200+ (ScreenWidth/2), 'y' : newPipe2[1]['y']}
    ]
    
    pipeVelocityX = -4
    playerVelocity_Y = -9
    playerMaxVel_Y = 10
    playerAcceleration_Y = 1
    
    playerFlapAccVel = -8 #Velocity while flapping
    playerFlapped = False #True --> When bird flying

    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelocity_Y = playerFlapAccVel
                    playerFlapped = True
                    Game_Sound['Wing'].play()
                    
        crashTest = isCollide(playerx, playery,upperPipes, lowerPipes)
        #Above function will return true, if we may have been crashed.
        if crashTest:
            return
        
        #checks the score 
        playerMidPosition = playerx + Game_Photos['Player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPosition = pipe['x'] + Game_Photos['Pipe'][0].get_width()/2
            if pipeMidPosition <= playerMidPosition < pipeMidPosition + 4:
                score += 1
                print(f"Your score is : {score}")
                Game_Sound['Point'].play()
        
        #Gravity bird slowing during fall
        if playerVelocity_Y < playerMaxVel_Y and not playerFlapped:
            playerVelocity_Y += playerAcceleration_Y
    
            
        if playerFlapped:
            playerFlapped = False
        playerHeight = Game_Photos['Player'].get_height()
        playery = playery + min(playerVelocity_Y, GroundY - playery - playerHeight)

        #move pipes to the left 
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelocityX
            lowerPipe['x'] += pipeVelocityX
            
        #if the pipe is out of screen , we need to remove it
        if upperPipes[0]['x'] < -Game_Photos['Pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
            
        #Add a new pipe when the first pipe is about to cross the leftmost part of the screen
        if 0 < upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])
        
        #Blitting the sprites
        Screen.blit(Game_Photos['Background'], (0,0))
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            Screen.blit(Game_Photos['Pipe'][0],(upperPipe['x'],upperPipe['y']))
            Screen.blit(Game_Photos['Pipe'][1],(lowerPipe['x'],lowerPipe['y']))
            
            
        Screen.blit(Game_Photos['Base'], (basex, GroundY))
        Screen.blit(Game_Photos['Player'], (playerx, playery))
        #Score digits
        myDigits = [int(x) for x in list(str(score))]
        width = 0 
        
        for digit in myDigits:
            width += Game_Photos['numbers'][digit].get_width()
        Xoffset = (ScreenWidth - width)/2
        
        for digit in myDigits:
            Screen.blit(Game_Photos['numbers'][digit], (Xoffset, ScreenHeight*0.12))
            Xoffset += Game_Photos['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def isCollide(playerx, playery,upperPipes, lowerPipes):
    if playery> GroundY - 25  or playery<0:
        Game_Sound['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = Game_Photos['Pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < Game_Photos['Pipe'][0].get_width()):
            Game_Sound['hit'].play()
            return True
        
    for pipe in lowerPipes:
        if (playery + Game_Photos['Player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < Game_Photos['Pipe'][0].get_width():
            Game_Sound['hit'].play()
            return True
        
    return False
            
def getRandomPipe():
    
    #Generate positions of two pipes (1st: Bottom, 2nd: Rotated)
    
    pipeHeight = Game_Photos['Pipe'][0].get_height()
    offset = ScreenHeight/3
    y2 = offset + random.randrange(0, int(ScreenHeight - Game_Photos['Base'].get_height() -  1.2 * offset))
    pipeX = ScreenWidth + 10
    y1 = pipeHeight - y2 + offset
    pipe  = [
        {'x': pipeX , 'y': -y1},  #Upper pipe
        {'x': pipeX , 'y': y2}   #Lower pipe
    ]
    
    return pipe

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