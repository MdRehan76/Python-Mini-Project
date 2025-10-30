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
highest_score = 0  # Global variable to track highest score
current_bird_index = 0  # Global variable to track current bird selection
game_mode = 'normal'  # Global variable to track game mode ('normal' or 'enemy')
bird_options = ['Gallery/Photos/Bird.png', 'Gallery/Photos/Blue_Bird.png', 'Gallery/Photos/Red_Bird.png']
Player = bird_options[current_bird_index]  # Use current bird selection
Background = 'Gallery/Photos/Background.jpg'
Pipe = 'Gallery/Photos/pipe.png'

def welcomeScreen():
    """
    Shows Welcome Images on the screen 
    """ 
    global current_bird_index, Player
    
    # Calculate positions for the new layout
    # 1) Flappy_Bird.png (title) - centered horizontally, positioned higher
    titleX = int((ScreenWidth - Game_Photos['title'].get_width()) / 2)
    titleY = 50  # Fixed position from top
    
    # 2) Pipe_Mode.png - centered horizontally, moved up by 150px
    pipeModeX = int((ScreenWidth - Game_Photos['pipe_mode'].get_width()) / 2)
    pipeModeY = (titleY + Game_Photos['title'].get_height() + 20) - 110  # Moved up by 150px
    
    # 3) Enemy_Mode.png - centered horizontally, moved up by 150px
    enemyModeX = int((ScreenWidth - Game_Photos['enemy_mode'].get_width()) / 2)
    enemyModeY = (pipeModeY + Game_Photos['pipe_mode'].get_height() + 15) - 170  # Moved up by 150px
    
    # 4) Change Bird button - right side with 20px margin from edge, 30px above base
    button_size = 60  # Button size
    changeBirdX = ScreenWidth - button_size - 20  # 20px margin from right edge
    changeBirdY = GroundY - 30 - button_size  # 30px above base
    
    PlayerX = int(ScreenWidth/7)
    PlayerY = int((ScreenHeight - Game_Photos['Player'].get_height())/3)
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
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_size = 60  # Same as in drawing section
                
                # Check if click is on Change Bird button
                if (changeBirdX <= mouse_x <= changeBirdX + button_size and 
                    changeBirdY <= mouse_y <= changeBirdY + button_size):
                    # Cycle to next bird
                    current_bird_index = (current_bird_index + 1) % len(bird_options)
                    Player = bird_options[current_bird_index]
                    # Reload the player image
                    Game_Photos['Player'] = pygame.image.load(Player).convert_alpha()
                
                # Check if click is on Enemy Mode button
                elif (enemyModeX <= mouse_x <= enemyModeX + Game_Photos['enemy_mode'].get_width() and
                      enemyModeY <= mouse_y <= enemyModeY + Game_Photos['enemy_mode'].get_height()):
                    global game_mode
                    game_mode = 'enemy'
                    return  # Start enemy mode
                
                # Check if click is on Pipe Mode button
                elif (pipeModeX <= mouse_x <= pipeModeX + Game_Photos['pipe_mode'].get_width() and
                      pipeModeY <= mouse_y <= pipeModeY + Game_Photos['pipe_mode'].get_height()):
                    game_mode = 'normal'
                    return  # Start normal mode
                
                else:
                    return  # Start game if clicked elsewhere
            else:
                # Draw background first
                Screen.blit(Game_Photos['Background'],(0,0)) 
                Screen.blit(Game_Photos['Base'],(basex,GroundY )) 
                Screen.blit(Game_Photos['Player'],(PlayerX,PlayerY)) 
                
                # Draw menu elements on top (in proper order)
                Screen.blit(Game_Photos['title'],(titleX,titleY)) 
                Screen.blit(Game_Photos['pipe_mode'],(pipeModeX,pipeModeY)) 
                Screen.blit(Game_Photos['enemy_mode'],(enemyModeX,enemyModeY)) 
                
                # Draw Change Bird button with circular blur background
                button_size = 60  # Button size
                center_x = changeBirdX + button_size // 2
                center_y = changeBirdY + button_size // 2
                radius = button_size // 2
                
                # Create blur effect with multiple circles of decreasing opacity
                for i in range(5):
                    blur_radius = radius + (5 - i) * 3
                    alpha = 30 - i * 5  # Decreasing opacity
                    # Create a surface for the blur circle
                    blur_surface = pygame.Surface((blur_radius * 2, blur_radius * 2), pygame.SRCALPHA)
                    pygame.draw.circle(blur_surface, (200, 200, 200, alpha), (blur_radius, blur_radius), blur_radius)
                    Screen.blit(blur_surface, (center_x - blur_radius, center_y - blur_radius))
                
                # Draw main circular background with semi-transparent effect
                circle_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(circle_surface, (255, 255, 255, 120), (radius, radius), radius)  # Semi-transparent white
                Screen.blit(circle_surface, (changeBirdX, changeBirdY))
                
                # Draw circular border
                pygame.draw.circle(Screen, (0, 0, 0), (center_x, center_y), radius, 3)  # Black border
                
                # Get current bird image and scale it to fit button
                bird_image_keys = ['Bird', 'Blue_Bird', 'Red_Bird']
                current_bird_image = Game_Photos[bird_image_keys[current_bird_index]]
                
                # Scale bird image to fit in circle (with some padding)
                scaled_bird = pygame.transform.scale(current_bird_image, (button_size - 15, button_size - 15))
                
                # Center the bird image in the circle
                bird_x = changeBirdX + 7
                bird_y = changeBirdY + 7
                Screen.blit(scaled_bird, (bird_x, bird_y))
                
                pygame.display.update()
                FPSCLOCK.tick(FPS) # To Control the game FPS
def mainGame():
    global game_mode
    score = 0
    playerx = int(ScreenWidth/5)
    playery = int(ScreenWidth/2)
    basex = 0
    
    # Variables to track game elements based on mode
    current_pipe = 'Pipe'
    current_background = 'Background1' if game_mode == 'enemy' else 'Background'
    current_base = 'Base1' if game_mode == 'enemy' else 'Base'
    
    # Powerup variables
    powerups = []  # List to store powerup positions
    last_powerup_score = 0  # Track when we last spawned a powerup
    should_spawn_powerup = False  # Flag to track if we should spawn a powerup
    
    # Start background music for enemy mode
    if game_mode == 'enemy':
        Game_Sound['Background1'].play(-1)  # -1 means loop indefinitely
    
    # Initialize enemies list for enemy mode
    enemies = []
    upperPipes = []
    lowerPipes = []
    
    if game_mode == 'normal':
        # Create pipes for normal mode
        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()
        
        upperPipes = [
            {'x' : ScreenWidth + 200, 'y' : newPipe1[0]['y']},
            {'x' : ScreenWidth + 400, 'y' : newPipe2[0]['y']}
        ]
        lowerPipes = [
            {'x' : ScreenWidth + 200, 'y' : newPipe1[1]['y']},
            {'x' : ScreenWidth + 400, 'y' : newPipe2[1]['y']}
        ]
    else:  # enemy mode
        # Create initial enemies
        enemies = [
            getRandomEnemy(),
            {'x': ScreenWidth + 300, 'y': random.randrange(50, int(GroundY - 100))}
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
                # Stop background music before quitting
                if game_mode == 'enemy':
                    Game_Sound['Background1'].stop()
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP)) or event.type == MOUSEBUTTONDOWN:
                if playery > 0:
                    playerVelocity_Y = playerFlapAccVel
                    playerFlapped = True
                    Game_Sound['Wing'].play()
                    
        if game_mode == 'normal':
            crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
        else:  # enemy mode
            crashTest = isCollideWithEnemies(playerx, playery, enemies)
            
        #Above function will return true, if we may have been crashed.
        if crashTest:
            # Stop background music if it's playing
            if game_mode == 'enemy':
                Game_Sound['Background1'].stop()
                # Enemy mode: Play swoosh sound first, then die sound after 0.5 seconds
                Game_Sound['Swoosh'].play()
                # Show the final frame for a moment
                pygame.display.update()
                pygame.time.wait(500)  # Wait half a second
                Game_Sound['Die'].play()
            else:
                # Normal mode: Play hit sound first, then die sound after 0.5 seconds
                Game_Sound['Hit'].play()
                # Show the final frame for a moment
                pygame.display.update()
                pygame.time.wait(500)  # Wait half a second
                Game_Sound['Die'].play()
            
            # Show game over screen with final score and wait for click
            gameOverScreen(score)
            # Return to let the main loop show welcome screen
            return
        
        #checks the score 
        playerMidPosition = playerx + Game_Photos['Player'].get_width()/2
        
        if game_mode == 'normal':
            for pipe in upperPipes:
                pipeMidPosition = pipe['x'] + Game_Photos['Pipe'][0].get_width()/2
                if pipeMidPosition <= playerMidPosition < pipeMidPosition + 4:
                    score += 1
                    print(f"Your score is : {score}")
                    Game_Sound['Point'].play()  # Play Point.mp3 for successful scoring
                    
                    # Change pipes when score reaches 3
                    if score == 3:
                        current_pipe = 'Pipe1'
        else:  # enemy mode
            for enemy in enemies:
                enemyMidPosition = enemy['x'] + Game_Photos['Bat'].get_width()/2
                if enemyMidPosition <= playerMidPosition < enemyMidPosition + 8:  # Wider detection for faster bats
                    if 'scored' not in enemy:  # Prevent multiple scoring from same bat
                        score += 1
                        print(f"Your score is : {score}")
                        enemy['scored'] = True  # Mark this enemy as scored
                        # No sound in enemy mode - silent scoring
            
            
        if playerVelocity_Y < playerMaxVel_Y and not playerFlapped:
            playerVelocity_Y += playerAcceleration_Y

        if playerFlapped:
            playerFlapped = False
            
        playerHeight = Game_Photos['Player'].get_height()
        playery += min(playerVelocity_Y, GroundY - playery - playerHeight)

        if game_mode == 'normal':
            #move pipes to the left 
            for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipeVelocityX
                lowerPipe['x'] += pipeVelocityX
                
            #Add a new pipe when the first pipe is about to cross the leftmost part of the screen
            if len(upperPipes) > 0 and 0 < upperPipes[0]['x'] < 5:
                newpipe = getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])
                
            #if the pipe is out of screen , we need to remove it
            if len(upperPipes) > 0 and upperPipes[0]['x'] < -Game_Photos['Pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)
        else:  # enemy mode
            #move enemies to the left with increased velocity
            for enemy in enemies:
                enemy['x'] += pipeVelocityX * 1.5  # Bats move 50% faster than pipes
                
            #Add a new enemy when needed (adjusted trigger for faster bats)
            if len(enemies) > 0 and 0 < enemies[0]['x'] < 10:
                enemies.append(getRandomEnemy())
                
            #Remove enemies that are out of screen
            if len(enemies) > 0 and enemies[0]['x'] < -Game_Photos['Bat'].get_width():
                enemies.pop(0)
        
        #Blitting the sprites
        Screen.blit(Game_Photos[current_background], (0,0))
        
        if game_mode == 'normal':
            # Draw pipes for normal mode
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
        else:  # enemy mode
            # Draw enemies (bats)
            for enemy in enemies:
                Screen.blit(Game_Photos['Bat'], (enemy['x'], enemy['y']))
            
        Screen.blit(Game_Photos[current_base], (basex, GroundY))
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

def isCollideWithEnemies(playerx, playery, enemies):
    """
    Returns True if player collides with enemies or ground/ceiling.
    """
    playerHeight = Game_Photos['Player'].get_height()
    playerWidth = Game_Photos['Player'].get_width()

    # Check if bird hits the ground or ceiling
    if playery + playerHeight >= GroundY or playery < 0:
        return True
    
    # Check collision with enemies
    for enemy in enemies:
        enemyWidth = Game_Photos['Bat'].get_width()
        enemyHeight = Game_Photos['Bat'].get_height()
        
        # Check if bird overlaps with enemy
        if (playerx < enemy['x'] + enemyWidth and
            playerx + playerWidth > enemy['x'] and
            playery < enemy['y'] + enemyHeight and
            playery + playerHeight > enemy['y']):
            return True
    
    return False
    
            
def gameOverScreen(score):
    """
    Shows Game Over screen with final score and highest score, waits for mouse click
    """
    global highest_score, game_mode
    # Update highest score if current score is higher
    if score > highest_score:
        highest_score = score
        
    # Determine background and base based on current game mode
    current_background = 'Background1' if game_mode == 'enemy' else 'Background'
    current_base = 'Base1' if game_mode == 'enemy' else 'Base'
    
    # Load GameOver image if not already loaded
    if 'GameOver' not in Game_Photos:
        Game_Photos['GameOver'] = pygame.image.load('Gallery/Photos/GameOver.png').convert_alpha()
    
    # Center the GameOver image horizontally and place it slightly above center vertically
    gameOverX = (ScreenWidth - Game_Photos['GameOver'].get_width()) // 2
    gameOverY = (ScreenHeight - Game_Photos['GameOver'].get_height()) // 2 - 50  # Move up by 50 pixels
    
    # Create font for displaying score
    font = pygame.font.Font(None, 36)  # None uses default font, 36 is the size
    
    # Current score
    score_text = str(score)  # Convert score to text
    score_surface = font.render(score_text, True, (0, 0, 0))  # Black color for text
    
    # Highest score
    highest_score_text = str(highest_score)
    highest_score_surface = font.render(highest_score_text, True, (0, 0, 0))
    
    # Position current score next to "Your Score:" text
    scoreX = (ScreenWidth - score_surface.get_width()) // 2 + 12
    scoreY = (ScreenHeight - Game_Photos['GameOver'].get_height()) // 2 + 196
    
    # Position highest score next to "Highest Score:" text
    highscoreX = (ScreenWidth - highest_score_surface.get_width()) // 2 + 24  # Moved right by increasing from 10 to 20
    highscoreY = scoreY + 29  # Moved up by reducing from 40 to 25
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                return
        
        # Keep the game scene visible with GameOver image using current mode's theme
        Screen.blit(Game_Photos[current_background], (0, 0))
        Screen.blit(Game_Photos[current_base], (0, GroundY))
        Screen.blit(Game_Photos['GameOver'], (gameOverX, gameOverY))
        
        # Display current score
        Screen.blit(score_surface, (scoreX, scoreY))
        
        # Display highest score
        Screen.blit(highest_score_surface, (highscoreX, highscoreY))
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

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

def getRandomEnemy():
    """
    Generate a random enemy bat position
    """
    enemyY = random.randrange(50, int(GroundY - 100))  # Random Y position avoiding ground and top
    enemyX = ScreenWidth + 10  # Start from right side
    
    return {'x': enemyX, 'y': enemyY}

if __name__ == "__main__":
    #This will be main point from where our game will start
    pygame.init() #initialize all pygame modules 
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by Rehan')
    # Load number images
    original_numbers = [pygame.image.load(f'Gallery/Photos/{i}.png').convert_alpha() for i in range(10)]
    
    # Create normal size numbers for gameplay
    Game_Photos['numbers'] = tuple(original_numbers)
    
    # Create smaller numbers for game over screen (70% of original size)
    Game_Photos['small_numbers'] = tuple(
        pygame.transform.scale(img, 
            (int(img.get_width() * 0.7), 
             int(img.get_height() * 0.7)))
        for img in original_numbers
    )

    # Load new welcome screen images
    Game_Photos['title'] = pygame.image.load('Gallery/Photos/Flappy _Bird.png').convert_alpha()
    Game_Photos['pipe_mode'] = pygame.image.load('Gallery/Photos/Pipe_Mode.png').convert_alpha()
    Game_Photos['enemy_mode'] = pygame.image.load('Gallery/Photos/Enemy_Mode.png').convert_alpha()
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
    
    # Load background music for enemy mode
    Game_Sound['Background1'] = pygame.mixer.Sound('Gallery/Sound/Background1.mp3')

        
    Game_Photos['Background'] = pygame.image.load(Background).convert()
    Game_Photos['Background1'] = pygame.image.load('Gallery/Photos/Background1.png').convert()
    Game_Photos['Player'] = pygame.image.load(Player).convert_alpha()
    
    # Load all bird options for cycling
    Game_Photos['Bird'] = pygame.image.load('Gallery/Photos/Bird.png').convert_alpha()
    Game_Photos['Blue_Bird'] = pygame.image.load('Gallery/Photos/Blue_Bird.png').convert_alpha()
    Game_Photos['Red_Bird'] = pygame.image.load('Gallery/Photos/Red_Bird.png').convert_alpha()
    
    # Load enemy bat image
    Game_Photos['Bat'] = pygame.image.load('Gallery/Photos/bat.png').convert_alpha()

    while True: 
        welcomeScreen() #Shows welcome Screen to the user until he presses a button
        mainGame() #This is the main Game Function
        # Wait a moment before showing welcome screen again
        pygame.time.wait(500)
