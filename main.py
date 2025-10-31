import random #For generating random numbers
import sys # we will use sys.exit to exit the program
import pygame
import math # For mathematical functions in effects
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

# Powerup system variables
active_powerup = None  # Track which powerup is active
powerup_pipes_remaining = 0  # How many pipes the powerup affects
powerups_on_screen = []  # List of powerups currently on screen
powerup_collected_time = 0  # Track when powerup was collected for burst effect
pipe_creation_effects = []  # Track visual effects when pipes are created
## Powerup2 now returns to normal spacing immediately after ending
bird_options = ['Gallery/Photos/Bird.png', 'Gallery/Photos/Blue_Bird.png', 'Gallery/Photos/Red_Bird.png']
Player = bird_options[current_bird_index]  # Use current bird selection
Background = 'Gallery/Photos/Background.jpg'
Pipe = 'Gallery/Photos/pipe.png'

def welcomeScreen():
    """
    Shows Welcome Images on the screen 
    """ 
    global current_bird_index, Player, game_mode
    
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
                # Prevent keyboard from starting the game
                pass
            
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_size = 60  # Same as in drawing section
                
                # Handle different click areas
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
                    game_mode = 'enemy'
                    return  # Start enemy mode
                
                # Check if click is on Pipe Mode button
                elif (pipeModeX <= mouse_x <= pipeModeX + Game_Photos['pipe_mode'].get_width() and
                      pipeModeY <= mouse_y <= pipeModeY + Game_Photos['pipe_mode'].get_height()):
                    game_mode = 'normal'
                    return  # Start normal mode
                
                # All other clicks (including title) do nothing
                else:
                    pass
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
def getPipeType(score):
    """
    Returns the pipe type based on score:
    - Score 0-3: Pipe
    - Score 4-7: Pipe1 
    - Score 8-11: Pipe
    - Score 12-15: Pipe1
    - And so on...
    """
    cycle = (score // 4) % 2
    return 'Pipe1' if cycle == 1 else 'Pipe'

def getPowerupType(score):
    """
    Returns powerup type based on score:
    - Score 5, 20, 35, ... : powerup1 (height increase)
    - Score 10, 25, 40, ... : powerup2 (width increase) 
    - Score 15, 30, 45, ... : powerup3 (no collision)
    """
    if score % 15 == 5:
        return 'powerup1'
    elif score % 15 == 10:
        return 'powerup2'
    elif score % 15 == 0 and score > 0:
        return 'powerup3'
    return None

def mainGame():
    global game_mode, active_powerup, powerup_pipes_remaining, powerups_on_screen, powerup_collected_time, pipe_creation_effects
    score = 0
    playerx = int(ScreenWidth/5)
    playery = int(ScreenWidth/2)
    basex = 0
    
    # Initialize powerup system
    active_powerup = None
    powerup_pipes_remaining = 0
    powerups_on_screen = []
    last_powerup_score = 0
    powerup_collected_time = 0
    pipe_creation_effects = []
    last_pipe_x = 0  # Track last pipe position for spacing effects
    ## Powerup2 returns to normal spacing after ending
    
    # Variables to track game elements based on mode
    current_pipe = 'Pipe'
    current_background = 'Background1' if game_mode == 'enemy' else 'Background'
    current_base = 'Base1' if game_mode == 'enemy' else 'Base'
    
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
            
            # Show game over screen and wait for restart button click
            if gameOverScreen(score):
                # Return True if restart button was clicked
                return True
            else:
                # Return False if game was quit
                return False
        
        #checks the score 
        playerMidPosition = playerx + Game_Photos['Player'].get_width()/2
        
        if game_mode == 'normal':
            for pipe in upperPipes:
                # Use current pipe type for scoring calculations
                current_pipe_type = getPipeType(score)
                pipeMidPosition = pipe['x'] + Game_Photos[current_pipe_type][0].get_width()/2
                if pipeMidPosition <= playerMidPosition < pipeMidPosition + 4:
                    score += 1
                    print(f"Your score is : {score}")
                    
                    # Decrease powerup3 counter when passing through pipes
                    if active_powerup == 'powerup3' and powerup_pipes_remaining > 0:
                        powerup_pipes_remaining -= 1
                        print(f"Powerup3: {powerup_pipes_remaining} pipes remaining")
                        if powerup_pipes_remaining <= 0:
                            active_powerup = None
                            print("Powerup3 effect ended!")
                    
                    Game_Sound['Point'].play()  # Play Point.mp3 for successful scoring
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
            
            # Move pipe creation effects with pipes
            for effect in pipe_creation_effects:
                if effect['type'] == 'spacing_indicator':
                    effect['x1'] += pipeVelocityX
                    effect['x2'] += pipeVelocityX
                else:
                    effect['x'] += pipeVelocityX
                
            #Add a new pipe when the first pipe is about to cross the leftmost part of the screen
            if len(upperPipes) > 0 and 0 < upperPipes[0]['x'] < 5:
                # Track previous pipe position for width effect
                if len(upperPipes) > 0:
                    last_pipe_x = upperPipes[-1]['x']
                
                newpipe = getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])
                
                # Add spacing indicator effect for powerup2
                if active_powerup == 'powerup2' and powerup_pipes_remaining > 0:
                    current_pipe_x = newpipe[0]['x']
                    spacing_distance = current_pipe_x - last_pipe_x
                    if spacing_distance > 200:  # Only show if significant spacing
                        pipe_creation_effects.append({
                            'type': 'spacing_indicator',
                            'x1': last_pipe_x + 52,  # End of previous pipe
                            'x2': current_pipe_x,     # Start of new pipe
                            'y': int(GroundY * 0.4),  # Middle height
                            'start_time': pygame.time.get_ticks()
                        })
                
            #if the pipe is out of screen , we need to remove it
            if len(upperPipes) > 0:
                current_pipe_type = getPipeType(score)
                if upperPipes[0]['x'] < -Game_Photos[current_pipe_type][0].get_width():
                    upperPipes.pop(0)
                    lowerPipes.pop(0)
            
            # Handle powerup spawning
            powerup_type = getPowerupType(score)
            if powerup_type and score != last_powerup_score:
                last_powerup_score = score
                # Spawn powerup ahead of the rightmost pipe
                if len(upperPipes) >= 1:
                    rightmost_pipe = upperPipes[-1]
                    powerup_x = rightmost_pipe['x'] + 150
                    
                    # Position powerup in the middle of the gap
                    upper_pipe_bottom = rightmost_pipe['y'] + Game_Photos['Pipe'][0].get_height()
                    lower_pipe_top = lowerPipes[-1]['y']
                    gap_center = upper_pipe_bottom + (lower_pipe_top - upper_pipe_bottom) / 2
                    
                    powerups_on_screen.append({
                        'x': powerup_x, 
                        'y': gap_center - 15, 
                        'type': powerup_type
                    })
                    print(f"Spawned {powerup_type} at score {score}")
            
            # Move and handle powerup collection
            remaining_powerups = []
            for powerup in powerups_on_screen:
                powerup['x'] += pipeVelocityX
                
                # Check collision with bird
                if (playerx < powerup['x'] + Game_Photos[powerup['type']].get_width() and
                    playerx + Game_Photos['Player'].get_width() > powerup['x'] and
                    playery < powerup['y'] + Game_Photos[powerup['type']].get_height() and
                    playery + Game_Photos['Player'].get_height() > powerup['y']):
                    
                    # Activate powerup immediately
                    active_powerup = powerup['type']
                    powerup_pipes_remaining = 3  # All powerups last for 3 pipes
                    powerup_collected_time = pygame.time.get_ticks()  # Record collection time
                    Game_Sound['Point'].play()
                    print(f"Collected {powerup['type']}! Effect activated immediately!")
                    
                    # Apply immediate visual effects based on powerup type
                    if powerup['type'] == 'powerup1':
                        print("Height boost activated! Increased pipe gap for 3 pipes.")
                    elif powerup['type'] == 'powerup2':
                        print("Width boost activated! Increased pipe spacing for 3 pipes.")
                    elif powerup['type'] == 'powerup3':
                        print("Invulnerability activated! You are invincible for 3 pipes!")
                else:
                    # Keep powerup if still on screen and not collected
                    if powerup['x'] > -Game_Photos[powerup['type']].get_width():
                        remaining_powerups.append(powerup)
            
            powerups_on_screen = remaining_powerups
            
            # Clean up pipe creation effects that are off-screen or expired
            current_time = pygame.time.get_ticks()
            remaining_effects = []
            for effect in pipe_creation_effects:
                if effect['type'] == 'spacing_indicator':
                    # Keep spacing indicators if they're on screen and not expired
                    if effect['x2'] > -100 and current_time - effect['start_time'] < 3000:
                        remaining_effects.append(effect)
                # bonus_spacing effects removed - no longer used
                else:
                    # Keep other effects if they're on screen and not expired
                    if effect['x'] > -100 and current_time - effect['start_time'] < 3000:
                        remaining_effects.append(effect)
            pipe_creation_effects = remaining_effects
            
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
        
        # Draw powerups
        if game_mode == 'normal':
            for powerup in powerups_on_screen:
                Screen.blit(Game_Photos[powerup['type']], (powerup['x'], powerup['y']))
        
        if game_mode == 'normal':
            # Draw pipes for normal mode
            # Get current pipe type based on score
            current_pipe_type = getPipeType(score)
            for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
                # Draw upper pipe using score-based pipe type
                Screen.blit(Game_Photos[current_pipe_type][0],(upperPipe['x'],upperPipe['y']))
                
                # Draw lower pipe (scaled to reach base)
                if 'height' in lowerPipe:
                    # Scale the lower pipe to extend to the base
                    pipeWidth = Game_Photos[current_pipe_type][1].get_width()
                    scaledLowerPipe = pygame.transform.scale(Game_Photos[current_pipe_type][1], (pipeWidth, lowerPipe['height']))
                    Screen.blit(scaledLowerPipe,(lowerPipe['x'],lowerPipe['y']))
                else:
                    # Fallback to normal pipe
                    Screen.blit(Game_Photos[current_pipe_type][1],(lowerPipe['x'],lowerPipe['y']))
        else:  # enemy mode
            # Draw enemies (bats)
            for enemy in enemies:
                Screen.blit(Game_Photos['Bat'], (enemy['x'], enemy['y']))
        
        # Draw pipe creation effects (height expansion for powerup1)
        current_time = pygame.time.get_ticks()
        for effect in pipe_creation_effects:
            if effect['type'] == 'height_expand':
                time_elapsed = current_time - effect['start_time']
                if time_elapsed < 1500:  # Effect lasts 1.5 seconds
                    progress = time_elapsed / 1500.0
                    
                    # Create expanding height indicator
                    max_height = effect['gap_size'] - 100  # Show the extra height gained
                    current_height = int(max_height * (1 - progress))  # Shrink over time
                    alpha = int(255 * (1 - progress))  # Fade out
                    
                    if current_height > 0:
                        # Draw vertical expansion lines
                        line_color = (0, 255, 0, alpha)
                        center_y = effect['y']
                        
                        # Create surface for the effect
                        effect_surface = pygame.Surface((20, current_height * 2), pygame.SRCALPHA)
                        
                        # Draw expansion lines
                        for i in range(5):
                            line_x = 4 + i * 3
                            pygame.draw.line(effect_surface, line_color,
                                           (line_x, current_height), 
                                           (line_x, current_height * 2), 2)
                        
                        # Draw arrows pointing up and down to show expansion
                        arrow_color = (0, 255, 0, min(alpha + 50, 255))
                        
                        # Up arrow
                        pygame.draw.polygon(effect_surface, arrow_color, [
                            (10, 0), (5, 10), (15, 10)
                        ])
                        
                        # Down arrow  
                        pygame.draw.polygon(effect_surface, arrow_color, [
                            (10, current_height * 2), (5, current_height * 2 - 10), (15, current_height * 2 - 10)
                        ])
                        
                        # Add pulsing text
                        if time_elapsed < 800:  # Show text for first part of effect
                            text_font = pygame.font.Font(None, 20)
                            text_surface = text_font.render("HEIGHT+", True, (0, 255, 0))
                            effect_surface.blit(text_surface, (25, current_height - 10))
                        
                        Screen.blit(effect_surface, (effect['x'] - 10, center_y - current_height))
            
            elif effect['type'] == 'width_expand':
                time_elapsed = current_time - effect['start_time']
                if time_elapsed < 1500:  # Effect lasts 1.5 seconds
                    progress = time_elapsed / 1500.0
                    
                    # Create expanding width indicator
                    max_width = 120  # Show the extra width gained
                    current_width = int(max_width * (1 - progress))  # Shrink over time
                    alpha = int(255 * (1 - progress))  # Fade out
                    
                    if current_width > 0:
                        # Draw horizontal expansion lines
                        line_color = (0, 150, 255, alpha)  # Blue color for width boost
                        center_x = effect['x'] + 60  # Center point
                        center_y = effect['y']
                        
                        # Create surface for the effect
                        effect_surface = pygame.Surface((current_width * 2, 30), pygame.SRCALPHA)
                        
                        # Draw expansion lines horizontally
                        for i in range(5):
                            line_y = 5 + i * 4
                            pygame.draw.line(effect_surface, line_color,
                                           (current_width, line_y), 
                                           (current_width * 2, line_y), 2)
                        
                        # Draw arrows pointing left and right to show width expansion
                        arrow_color = (0, 150, 255, min(alpha + 50, 255))
                        
                        # Left arrow
                        pygame.draw.polygon(effect_surface, arrow_color, [
                            (0, 15), (10, 10), (10, 20)
                        ])
                        
                        # Right arrow  
                        pygame.draw.polygon(effect_surface, arrow_color, [
                            (current_width * 2, 15), (current_width * 2 - 10, 10), (current_width * 2 - 10, 20)
                        ])
                        
                        # Add pulsing text
                        if time_elapsed < 800:  # Show text for first part of effect
                            text_font = pygame.font.Font(None, 20)
                            text_surface = text_font.render("WIDTH+", True, (0, 150, 255))
                            effect_surface.blit(text_surface, (current_width - 25, 0))
                        
                        # Add stretching effect lines
                        stretch_color = (100, 200, 255, alpha // 2)
                        for j in range(3):
                            stretch_y = 8 + j * 6
                            pygame.draw.line(effect_surface, stretch_color,
                                           (current_width // 2, stretch_y), 
                                           (current_width * 2 - current_width // 2, stretch_y), 1)
                        
                        Screen.blit(effect_surface, (center_x - current_width, center_y - 15))
            
            elif effect['type'] == 'spacing_indicator':
                time_elapsed = current_time - effect['start_time']
                if time_elapsed < 2000:  # Effect lasts 2 seconds
                    progress = time_elapsed / 2000.0
                    alpha = int(255 * (1 - progress))  # Fade out
                    
                    # Draw spacing indicator line between pipes
                    line_color = (0, 200, 255, alpha)
                    line_y = effect['y']
                    
                    # Animate the line drawing from left to right
                    animated_x2 = effect['x1'] + (effect['x2'] - effect['x1']) * min(progress * 2, 1.0)
                    
                    if animated_x2 > effect['x1']:
                        # Draw main spacing line
                        pygame.draw.line(Screen, line_color[:3], 
                                       (int(effect['x1']), line_y), 
                                       (int(animated_x2), line_y), 3)
                        
                        # Draw measurement marks
                        mark_color = (100, 255, 255, alpha)
                        pygame.draw.line(Screen, mark_color[:3],
                                       (int(effect['x1']), line_y - 10),
                                       (int(effect['x1']), line_y + 10), 2)
                        
                        if animated_x2 >= effect['x2']:
                            pygame.draw.line(Screen, mark_color[:3],
                                           (int(effect['x2']), line_y - 10),
                                           (int(effect['x2']), line_y + 10), 2)
                        
                        # Add distance text
                        if progress > 0.3:  # Show text after line animation
                            distance = int(effect['x2'] - effect['x1'])
                            text_font = pygame.font.Font(None, 18)
                            text_surface = text_font.render(f"+{distance}px", True, (0, 200, 255))
                            text_x = (effect['x1'] + effect['x2']) / 2 - text_surface.get_width() / 2
                            text_y = line_y - 25
                            Screen.blit(text_surface, (int(text_x), int(text_y)))
            
            # bonus_spacing effect removed - pipes return to normal spacing after powerup2
            
        Screen.blit(Game_Photos[current_base], (basex, GroundY))
        
        # Draw player with special effects based on active powerup
        if active_powerup and powerup_pipes_remaining > 0:
            if active_powerup == 'powerup1':
                # Green glow effect for height boost
                glow_size = 5
                glow_color = (0, 255, 0, 100)  # Green color with transparency
                # Create pulsing effect
                pulse = abs(int((pygame.time.get_ticks() / 200) % 10 - 5))
                glow_size += pulse
                
                glow_surface = pygame.Surface((Game_Photos['Player'].get_width() + glow_size*2, 
                                             Game_Photos['Player'].get_height() + glow_size*2), 
                                             pygame.SRCALPHA)
                pygame.draw.ellipse(glow_surface, glow_color, 
                                  (0, 0, glow_surface.get_width(), glow_surface.get_height()))
                Screen.blit(glow_surface, (playerx - glow_size, playery - glow_size))
                
                # Add sparkle effects around the bird
                import math
                time = pygame.time.get_ticks() / 100
                for i in range(4):
                    angle = (time + i * 90) * math.pi / 180
                    sparkle_x = playerx + Game_Photos['Player'].get_width()//2 + math.cos(angle) * 25
                    sparkle_y = playery + Game_Photos['Player'].get_height()//2 + math.sin(angle) * 25
                    pygame.draw.circle(Screen, (0, 255, 0), (int(sparkle_x), int(sparkle_y)), 3)
                    
            elif active_powerup == 'powerup2':
                # Blue glow effect for width boost
                glow_size = 4
                glow_color = (0, 150, 255, 110)  # Blue color with transparency
                # Create expanding/contracting effect
                breath = abs(int((pygame.time.get_ticks() / 150) % 8 - 4))
                glow_size += breath
                
                glow_surface = pygame.Surface((Game_Photos['Player'].get_width() + glow_size*2, 
                                             Game_Photos['Player'].get_height() + glow_size*2), 
                                             pygame.SRCALPHA)
                pygame.draw.ellipse(glow_surface, glow_color, 
                                  (0, 0, glow_surface.get_width(), glow_surface.get_height()))
                Screen.blit(glow_surface, (playerx - glow_size, playery - glow_size))
                
                # Add trailing effect
                trail_color = (0, 100, 200, 80)
                trail_surface = pygame.Surface((Game_Photos['Player'].get_width() + 10, 
                                             Game_Photos['Player'].get_height() + 10), 
                                             pygame.SRCALPHA)
                pygame.draw.ellipse(trail_surface, trail_color, 
                                  (0, 0, trail_surface.get_width(), trail_surface.get_height()))
                Screen.blit(trail_surface, (playerx - 15, playery - 5))
                
            elif active_powerup == 'powerup3':
                # Golden glow effect for invulnerability with enhanced effects
                glow_size = 7
                glow_color = (255, 215, 0, 130)  # Golden color with transparency
                # Create intense pulsing effect
                pulse = abs(int((pygame.time.get_ticks() / 100) % 12 - 6))
                glow_size += pulse
                
                # Multiple glow layers for more dramatic effect
                for layer in range(3):
                    layer_size = glow_size - layer * 2
                    layer_alpha = 130 - layer * 30
                    layer_color = (255, 215 - layer * 20, 0, max(layer_alpha, 40))
                    
                    glow_surface = pygame.Surface((Game_Photos['Player'].get_width() + layer_size*2, 
                                                 Game_Photos['Player'].get_height() + layer_size*2), 
                                                 pygame.SRCALPHA)
                    pygame.draw.ellipse(glow_surface, layer_color, 
                                      (0, 0, glow_surface.get_width(), glow_surface.get_height()))
                    Screen.blit(glow_surface, (playerx - layer_size, playery - layer_size))
                
                # Add golden particles around the bird
                import math
                time = pygame.time.get_ticks() / 50
                for i in range(8):
                    angle = (time + i * 45) * math.pi / 180
                    particle_distance = 30 + math.sin(time + i) * 10
                    particle_x = playerx + Game_Photos['Player'].get_width()//2 + math.cos(angle) * particle_distance
                    particle_y = playery + Game_Photos['Player'].get_height()//2 + math.sin(angle) * particle_distance
                    particle_size = 2 + abs(int(math.sin(time * 2 + i)))
                    pygame.draw.circle(Screen, (255, 215, 0), (int(particle_x), int(particle_y)), particle_size)
                    pygame.draw.circle(Screen, (255, 255, 255), (int(particle_x), int(particle_y)), max(1, particle_size-1))
        
        # Draw bird with scaling effect when powerup is active
        if active_powerup and powerup_pipes_remaining > 0:
            # Create subtle scaling effect
            scale_factor = 1.0 + 0.1 * abs(math.sin(pygame.time.get_ticks() / 200))
            bird_width = int(Game_Photos['Player'].get_width() * scale_factor)
            bird_height = int(Game_Photos['Player'].get_height() * scale_factor)
            scaled_bird = pygame.transform.scale(Game_Photos['Player'], (bird_width, bird_height))
            
            # Center the scaled bird
            offset_x = (bird_width - Game_Photos['Player'].get_width()) // 2
            offset_y = (bird_height - Game_Photos['Player'].get_height()) // 2
            Screen.blit(scaled_bird, (playerx - offset_x, playery - offset_y))
        else:
            Screen.blit(Game_Photos['Player'], (playerx, playery))
        
        # Draw collection burst effect
        current_time = pygame.time.get_ticks()
        if powerup_collected_time > 0 and current_time - powerup_collected_time < 1000:  # Effect lasts 1 second
            time_since_collection = current_time - powerup_collected_time
            burst_progress = time_since_collection / 1000.0  # 0 to 1
            
            # Create expanding ring effect
            ring_radius = int(burst_progress * 60)
            ring_alpha = int(255 * (1 - burst_progress))
            
            if active_powerup == 'powerup1':
                ring_color = (0, 255, 0, ring_alpha)
            elif active_powerup == 'powerup2':
                ring_color = (0, 150, 255, ring_alpha)
            elif active_powerup == 'powerup3':
                ring_color = (255, 215, 0, ring_alpha)
            else:
                ring_color = (255, 255, 255, ring_alpha)
            
            # Draw expanding rings
            center_x = playerx + Game_Photos['Player'].get_width() // 2
            center_y = playery + Game_Photos['Player'].get_height() // 2
            
            for i in range(3):
                current_radius = ring_radius - i * 15
                if current_radius > 0:
                    # Create surface for the ring
                    ring_surface = pygame.Surface((current_radius * 2, current_radius * 2), pygame.SRCALPHA)
                    pygame.draw.circle(ring_surface, ring_color, (current_radius, current_radius), current_radius, 3)
                    Screen.blit(ring_surface, (center_x - current_radius, center_y - current_radius))
            
            # Reset burst effect when done
            if burst_progress >= 1.0:
                powerup_collected_time = 0
            
        #Score digits
        myDigits = [int(x) for x in list(str(score))]
        width = 0 
        
        for digit in myDigits:
            width += Game_Photos['numbers'][digit].get_width()
        Xoffset = (ScreenWidth - width)/2
        
        for digit in myDigits:
            Screen.blit(Game_Photos['numbers'][digit], (Xoffset, ScreenHeight*0.12))
            Xoffset += Game_Photos['numbers'][digit].get_width()
        
        # Display active powerup information
        if active_powerup and powerup_pipes_remaining > 0:
            font = pygame.font.Font(None, 24)
            powerup_names = {
                'powerup1': 'Height Boost',
                'powerup2': 'Width Boost', 
                'powerup3': 'Invulnerable'
            }
            text = font.render(f"{powerup_names[active_powerup]}: {powerup_pipes_remaining} pipes", True, (255, 255, 255))
            Screen.blit(text, (10, 10))
            
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def isCollide(playerx, playery, upperPipes, lowerPipes):
    """
    Returns True if player collides with the ground or pipes.
    """
    global active_powerup, powerup_pipes_remaining
    
    playerHeight = Game_Photos['Player'].get_height()
    playerWidth = Game_Photos['Player'].get_width()

    # Check ground and ceiling collisions (always active)
    if playery + playerHeight >= GroundY or playery < 0:
        return True
    
    # Skip pipe collision if powerup3 is active
    if active_powerup == 'powerup3' and powerup_pipes_remaining > 0:
        return False
    
    # Check collision with pipes
    for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
        # Get current pipe type based on score for collision detection
        current_pipe_type = getPipeType(0)  # Use default pipe type for collision
        # Get pipe dimensions
        pipeWidth = Game_Photos[current_pipe_type][0].get_width()
        pipeHeight = Game_Photos[current_pipe_type][0].get_height()
        
        # Check if bird is in the horizontal range of the pipe
        if (playerx < upperPipe['x'] + pipeWidth) and (playerx + playerWidth > upperPipe['x']):
            # Check collision with upper pipe
            if playery < upperPipe['y'] + pipeHeight:
                return True
            # Check collision with lower pipe (use custom height if available)
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
    Shows Game Over screen with final score and highest score.
    Returns True if restart button was clicked, False otherwise.
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
    scoreX = (ScreenWidth - score_surface.get_width()) // 2 + 55
    scoreY = (ScreenHeight - Game_Photos['GameOver'].get_height()) // 2 + 193
    
    # Position highest score next to "Highest Score:" text
    highscoreX = (ScreenWidth - highest_score_surface.get_width()) // 2 + 55  # Moved right by increasing from 10 to 20
    highscoreY = scoreY + 34  # Moved up by reducing from 40 to 25
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                # Spacebar press - restart game immediately
                print("Spacebar pressed - Restarting game!")
                return True
            elif event.type == MOUSEBUTTONDOWN:
                # Get mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(f"Clicked at position: x={mouse_x}, y={mouse_y}")
                
                # Calculate the restart button area based on game over image position
                restart_x_min = gameOverX + 117  # Relative to game over image X
                restart_x_max = gameOverX + 259  # Relative to game over image X
                restart_y_min = gameOverY + 351  # Relative to game over image Y
                restart_y_max = gameOverY + 393  # Relative to game over image Y
                
                print(f"Restart button area: X({restart_x_min}, {restart_x_max}), Y({restart_y_min}, {restart_y_max})")
                
                # Only restart if click is within the specific restart button area
                if (restart_x_min <= mouse_x <= restart_x_max and 
                    restart_y_min <= mouse_y <= restart_y_max):
                    print("Click detected in restart button area - Restarting game!")
                    return True
                else:
                    print("Click was outside restart button area - No action taken")
        
        # Keep the game scene visible with GameOver image using current mode's theme
        Screen.blit(Game_Photos[current_background], (0, 0))
        Screen.blit(Game_Photos[current_base], (0, GroundY))
        Screen.blit(Game_Photos['GameOver'], (gameOverX, gameOverY))
        
        # Display current score
        Screen.blit(score_surface, (scoreX, scoreY))
        
        # Display highest score
        Screen.blit(highest_score_surface, (highscoreX, highscoreY))
        
        # Add instruction text for restart options with blinking effect
        instruction_font = pygame.font.Font(None, 28)
        
        # Create blinking effect for restart text
        blink_time = pygame.time.get_ticks() // 500  # Blink every 500ms
        text_color = (255, 255, 100) if blink_time % 2 == 0 else (255, 255, 255)  # Alternate between yellow and white
        
        instruction_text1 = instruction_font.render("Press SPACEBAR or Click RESTART Button", True, text_color)
        instruction_text2 = instruction_font.render("Press ESC to Exit", True, (200, 200, 200))
        
        # Position instructions below the game over screen
        text1_x = (ScreenWidth - instruction_text1.get_width()) // 2
        text1_y = gameOverY + Game_Photos['GameOver'].get_height() + 20
        
        text2_x = (ScreenWidth - instruction_text2.get_width()) // 2
        text2_y = text1_y + 35
        
        # Add background for better readability
        text_bg = pygame.Surface((ScreenWidth, 80), pygame.SRCALPHA)
        text_bg.fill((0, 0, 0, 120))  # Semi-transparent black
        Screen.blit(text_bg, (0, text1_y - 10))
        
        Screen.blit(instruction_text1, (text1_x, text1_y))
        Screen.blit(instruction_text2, (text2_x, text2_y))
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def getRandomPipe():
    """
    Generate positions of two pipes (upper and lower) with classic Flappy Bird gap
    Lower pipe ALWAYS extends to the base, upper pipe comes from top
    """
    global active_powerup, powerup_pipes_remaining
    
    pipeHeight = Game_Photos['Pipe'][0].get_height()
    
    # Base gap size - improved for better gameplay
    gapSize = 120  # Increased from 100 to 120 for more comfortable gameplay
    
    # Apply powerup effects
    if active_powerup == 'powerup1' and powerup_pipes_remaining > 0:
        # Dramatically increase height (gap size) for powerup1
        gapSize = 200  # Even larger gap to maintain significant difference
        print(f"Powerup1 active: Increased gap height to {gapSize}")
    elif active_powerup == 'powerup2' and powerup_pipes_remaining > 0:
        # For powerup2, we'll handle width in the pipe positioning
        print(f"Powerup2 active: Increased horizontal pipe spacing to 150px")
    
    # Calculate the range where gap can be positioned
    minGapY = 80  # Minimum distance from top
    maxGapY = int(GroundY - gapSize - 80)  # Ensure lower pipe has space to reach base
    
    # Random position for the gap TOP edge
    gapTopY = random.randrange(minGapY, maxGapY)
    
    # Base pipe spacing - significantly improved for comfortable gameplay
    pipeX = ScreenWidth + 50  # Increased base spacing for much better playability
    
    # Apply powerup2 effect (much wider spacing between pipes)
    if active_powerup == 'powerup2' and powerup_pipes_remaining > 0:
        pipeX = ScreenWidth + 150  # Extra wide spacing during powerup2 (200% increase from base)
    # After powerup2 ends, pipes return to improved normal spacing (ScreenWidth + 50)

    # Powerups are now activated immediately when collected, no pending system needed
    
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
    
    # No bonus spacing effects needed - pipes return to normal after powerup2 ends
    
    # Decrease powerup counter when creating a new pipe (for powerup1 and powerup2 only)
    if active_powerup in ['powerup1', 'powerup2'] and powerup_pipes_remaining > 0:
        # Add visual effect for powerup1 (height increase effect)
        if active_powerup == 'powerup1':
            gap_center_y = upperPipeY + pipeHeight + (gapSize / 2)
            pipe_creation_effects.append({
                'type': 'height_expand',
                'x': pipeX + 26,  # Center of pipe
                'y': gap_center_y,
                'start_time': pygame.time.get_ticks(),
                'gap_size': gapSize
            })
        
        # Add visual effect for powerup2 (width spacing effect)
        elif active_powerup == 'powerup2':
            gap_center_y = upperPipeY + pipeHeight + (gapSize / 2)
            pipe_creation_effects.append({
                'type': 'width_expand',
                'x': pipeX - 60,  # Show effect before the pipe
                'y': gap_center_y,
                'start_time': pygame.time.get_ticks(),
                'pipe_x': pipeX
            })
        
        powerup_pipes_remaining -= 1
        print(f"Powerup {active_powerup}: {powerup_pipes_remaining} pipes remaining")
        if powerup_pipes_remaining <= 0:
            active_powerup = None
            print(f"Powerup effect ended! Pipes return to normal spacing.")

    # Powerups are activated immediately upon collection
    
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
    pygame.display.set_caption('Flappy Bird')
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
    
    # Load powerup images
    Game_Photos['powerup1'] = pygame.image.load('Gallery/Photos/powerup1.png').convert_alpha()
    Game_Photos['powerup2'] = pygame.image.load('Gallery/Photos/powerup2.png').convert_alpha()
    Game_Photos['powerup3'] = pygame.image.load('Gallery/Photos/powerup3.png').convert_alpha()

    while True: 
        welcomeScreen() #Shows welcome Screen to the user until he presses a button
        mainGame() #This is the main Game Function
        # Wait a moment before showing welcome screen again
        pygame.time.wait(500)
