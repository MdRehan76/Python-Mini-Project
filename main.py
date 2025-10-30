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
            
            elif event.type == MOUSEBUTTONDOWN:
                return
            else:
                Screen.blit(Game_Photos['Background'],(0,0)) 
                Screen.blit(Game_Photos['Player'],(PlayerX,PlayerY)) 
                Screen.blit(Game_Photos['message'],(messagex,messagey)) 
                Screen.blit(Game_Photos['Base'],(basex,GroundY )) 
                pygame.display.update()
                FPSCLOCK.tick(FPS) # To Control the game FPS
def mainGame():
    score = 0
    playerx = int(ScreenWidth/5)
    playery = int(ScreenWidth/2)
    basex = 0
    
    # Variable to track which pipe to use
    current_pipe = 'Pipe'
    
    #Create new pipe 2 pipes on screen ( up and down )
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()
    
    #My list of upper pipes - classic Flappy Bird spacing
    upperPipes = [
        {'x' : ScreenWidth + 200, 'y' : newPipe1[0]['y']},
        {'x' : ScreenWidth + 400, 'y' : newPipe2[0]['y']}  # 200px between pipes
    ]
    #My list of lower pipes
    lowerPipes = [
        {'x' : ScreenWidth + 200, 'y' : newPipe1[1]['y']},
        {'x' : ScreenWidth + 400, 'y' : newPipe2[1]['y']}  # 200px between pipes
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
            if (event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP)) or event.type == MOUSEBUTTONDOWN:
                if playery > 0:
                    playerVelocity_Y = playerFlapAccVel
                    playerFlapped = True
                    Game_Sound['Wing'].play()
                    
        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
        #Above function will return true, if we may have been crashed.
        if crashTest:
            Game_Sound['Hit'].play()
            Game_Sound['Die'].play()
            # Reset player sprite back to bird
            Game_Photos['Player'] = pygame.image.load(Player).convert_alpha()
            return
        
        #checks the score 
        playerMidPosition = playerx + Game_Photos['Player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPosition = pipe['x'] + Game_Photos['Pipe'][0].get_width()/2
            if pipeMidPosition <= playerMidPosition < pipeMidPosition + 4:
                score += 1
                print(f"Your score is : {score}")
                Game_Sound['Point'].play()
                
                # Change pipes when score reaches 3
                if score == 3:
                    current_pipe = 'Pipe1'
            
            
        if playerVelocity_Y < playerMaxVel_Y and not playerFlapped:
            playerVelocity_Y += playerAcceleration_Y

        if playerFlapped:
            playerFlapped = False
            
        playerHeight = Game_Photos['Player'].get_height()
        playery += min(playerVelocity_Y, GroundY - playery - playerHeight)

        #move pipes to the left 
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelocityX
            lowerPipe['x'] += pipeVelocityX
            
        #Add a new pipe when the first pipe is about to cross the leftmost part of the screen
        if 0 < upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])
            
        
        #if the pipe is out of screen , we need to remove it
        if len(upperPipes) > 0 and upperPipes[0]['x'] < -Game_Photos['Pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        
        #Blitting the sprites
        Screen.blit(Game_Photos['Background'], (0,0))
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            # Draw upper pipe using current pipe
            Screen.blit(Game_Photos[current_pipe][0],(upperPipe['x'],upperPipe['y']))
            
            # Draw lower pipe (scaled to reach base)
            if 'height' in lowerPipe:
                # Scale the lower pipe to extend to the base
                pipeWidth = Game_Photos[current_pipe][1].get_width()
                scaledLowerPipe = pygame.transform.scale(Game_Photos[current_pipe][1], (pipeWidth, lowerPipe['height']))
                Screen.blit(scaledLowerPipe,(lowerPipe['x'],lowerPipe['y']))
            else:
                # Fallback to normal pipe
                Screen.blit(Game_Photos[current_pipe][1],(lowerPipe['x'],lowerPipe['y']))
            
            
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


def isCollide(playerx, playery, upperPipes, lowerPipes):
    """
    Returns True if player collides with the ground or pipes.
    """
    playerHeight = Game_Photos['Player'].get_height()
    playerWidth = Game_Photos['Player'].get_width()

    # Check if bird hits the ground
    if playery + playerHeight >= GroundY:
        return True
    # Check if bird hits the top
    elif playery < 0:
        return True
    
    # Check collision with pipes
    for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
        # Get pipe dimensions
        pipeWidth = Game_Photos['Pipe'][0].get_width()
        pipeHeight = Game_Photos['Pipe'][0].get_height()
        
        # Check if bird is in the horizontal range of the pipe
        if (playerx < upperPipe['x'] + pipeWidth) and (playerx + playerWidth > upperPipe['x']):
            # Check collision with upper pipe
            if playery < upperPipe['y'] + pipeHeight:
                return True
            # Check collision with lower pipe (use custom height if available)
            lowerPipeBottom = lowerPipe['y'] + (lowerPipe.get('height', pipeHeight))
            if playery + playerHeight > lowerPipe['y']:
                return True
    
    return False
    
            
def getRandomPipe():
    """
    Generate positions of two pipes (upper and lower) with classic Flappy Bird gap
    Lower pipe ALWAYS extends to the base, upper pipe comes from top
    """
    pipeHeight = Game_Photos['Pipe'][0].get_height()
    
    # Classic Flappy Bird gap size
    gapSize = 100  # Perfect gap for bird to pass through
    
    # Calculate the range where gap can be positioned
    # The gap should be positioned so lower pipe can reach the base
    minGapY = 80  # Minimum distance from top
    maxGapY = int(GroundY - gapSize - 80)  # Ensure lower pipe has space to reach base
    
    # Random position for the gap TOP edge
    gapTopY = random.randrange(minGapY, maxGapY)
    
    pipeX = ScreenWidth + 10
    
    # Upper pipe - comes down from top, bottom edge at gap top
    upperPipeY = gapTopY - pipeHeight
    
    # Lower pipe - starts right after the gap and extends ALL THE WAY to the base
    lowerPipeY = gapTopY + gapSize
    # Make sure lower pipe extends exactly to the base with no gap
    lowerPipeHeight = int(GroundY - lowerPipeY + 5)  # Add 5 pixels to ensure it touches base
    
    # Debug: ensure we have a valid lower pipe height
    if lowerPipeHeight <= 0:
        lowerPipeHeight = 100  # Minimum height fallback
        lowerPipeY = int(GroundY - lowerPipeHeight)
    
    pipe = [
        {'x': pipeX, 'y': upperPipeY},                    #Upper pipe (normal height)
        {'x': pipeX, 'y': lowerPipeY, 'height': lowerPipeHeight}  #Lower pipe (extends to base)
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
    Game_Photos['Base1'] = pygame.image.load('Gallery/Photos/Base1.png').convert_alpha()
    # Load and scale pipes to classic Flappy Bird size
    pipeImage = pygame.image.load(Pipe).convert_alpha()
    pipe1Image = pygame.image.load('Gallery/Photos/pipe1.png').convert_alpha()
    pipeWidth = 52  # Classic Flappy Bird pipe width
    pipeHeight = 320  # Make pipes taller
    
    Game_Photos['Pipe'] = (
        pygame.transform.scale(pygame.transform.rotate(pipeImage, 180), (pipeWidth, pipeHeight)),
        pygame.transform.scale(pipeImage, (pipeWidth, pipeHeight))
        )
    Game_Photos['Pipe1'] = (
        pygame.transform.scale(pygame.transform.rotate(pipe1Image, 180), (pipeWidth, pipeHeight)),
        pygame.transform.scale(pipe1Image, (pipeWidth, pipeHeight))
        )
    Game_Sound['Die'] = pygame.mixer.Sound('Gallery/Sound/Die.mp3')
    Game_Sound['Hit'] = pygame.mixer.Sound('Gallery/Sound/Hit.mp3')
    Game_Sound['Point'] = pygame.mixer.Sound('Gallery/Sound/Point.mp3')
    Game_Sound['Swoosh'] = pygame.mixer.Sound('Gallery/Sound/Swoosh.mp3')
    Game_Sound['Wing'] = pygame.mixer.Sound('Gallery/Sound/Wing.mp3')

        
    Game_Photos['Background'] = pygame.image.load(Background).convert()
    Game_Photos['Background1'] = pygame.image.load('Gallery/Photos/Background1.png').convert()
    Game_Photos['Player'] = pygame.image.load(Player).convert_alpha()

    while True: 
        welcomeScreen() #Shows welcome Screen to the user until he presses a button
        mainGame() #This is the main Game Function 
