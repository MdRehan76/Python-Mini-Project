def isCollide(playerx, playery, upperPipes, lowerPipes):
    """
    Returns True if player collides with the ground or pipes.
    """
    global is_invulnerable, invulnerable_start_time
    
    # Check if invulnerability should end
    if is_invulnerable:
        current_time = pygame.time.get_ticks()
        if current_time - invulnerable_start_time >= INVULNERABLE_DURATION:
            is_invulnerable = False
            print("Invulnerability ended")
    
    playerHeight = Game_Photos['Player'].get_height()
    playerWidth = Game_Photos['Player'].get_width()

    # Always check ground and ceiling collisions, even when invulnerable
    if playery + playerHeight >= GroundY:
        is_invulnerable = False  # Reset invulnerability on ground hit
        return True
    elif playery < 0:
        is_invulnerable = False  # Reset invulnerability on ceiling hit
        return True
        
    # Skip pipe collisions if invulnerable
    if is_invulnerable:
        return False
    
    # Check collision with pipes
    for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
        # Get pipe dimensions
        pipeWidth = Game_Photos['Pipe'][0].get_width()
        pipeHeight = Game_Photos['Pipe'][0].get_height()
        
        # Check if bird has passed this pipe (for scoring)
        if (playerx > upperPipe['x'] + pipeWidth) and not ('passed' in upperPipe and upperPipe['passed']):
            upperPipe['passed'] = True
        
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