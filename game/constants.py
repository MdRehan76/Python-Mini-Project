from typing import Dict, List

# Game Constants
FPS: int = 32
SCREEN_WIDTH: int = 409
SCREEN_HEIGHT: int = 593
GROUND_Y: float = SCREEN_HEIGHT * 0.8
SCORE_INCREASE_FOR_INVULNERABILITY: int = 5
POWERUP_SPAWN_INTERVAL: int = 12
PIPE_WIDTH: int = 52
PIPE_HEIGHT: int = 320
GAP_SIZE: int = 100

# Asset Paths
ASSET_PATHS: Dict[str, str | List[str]] = {
    'BIRD_OPTIONS': [
        'Gallery/Photos/Bird.png',
        'Gallery/Photos/Blue_Bird.png',
        'Gallery/Photos/Red_Bird.png'
    ],
    'BACKGROUND': 'Gallery/Photos/Background.jpg',
    'BACKGROUND_ENEMY': 'Gallery/Photos/Background1.png',
    'PIPE': 'Gallery/Photos/pipe.png',
    'PIPE_ENEMY': 'Gallery/Photos/pipe1.png',
    'BASE': 'Gallery/Photos/Base.png',
    'BASE_ENEMY': 'Gallery/Photos/Base1.png',
    'POWERUP': 'Gallery/Photos/powerup.png',
    'BAT': 'Gallery/Photos/bat.png',
    'TITLE': 'Gallery/Photos/Flappy _Bird.png',
    'GAMEOVER': 'Gallery/Photos/GameOver.png',
    'PIPE_MODE': 'Gallery/Photos/Pipe_Mode.png',
    'ENEMY_MODE': 'Gallery/Photos/Enemy_Mode.png'
}

# Sound Paths
SOUND_PATHS: Dict[str, str] = {
    'DIE': 'Gallery/Sound/Die.mp3',
    'HIT': 'Gallery/Sound/Hit.mp3',
    'POINT': 'Gallery/Sound/Point.mp3',
    'SWOOSH': 'Gallery/Sound/Swoosh.mp3',
    'WING': 'Gallery/Sound/Wing.mp3',
    'BACKGROUND1': 'Gallery/Sound/Background1.mp3'
}