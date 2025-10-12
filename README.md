# Flappy Bird Game - Python Mini Project

A Python implementation of the popular Flappy Bird game using PyGame library.

## 🎮 Game Overview
This is a Flappy Bird clone developed by Rehan using Python and PyGame. The game features a bird that the player controls by pressing keys to navigate through obstacles.

## 🛠️ Technologies Used
- **Python** - Core programming language
- **PyGame** - Game development library for graphics, sounds, and event handling

## 📁 Project Structure
```
Python-Mini-Project/
├── main.py                    # Main game file
├── Gallery/
│   ├── Photos/                # Game images and sprites
│   │   ├── Bird.png          # Player bird sprite
│   │   ├── Background.jpg    # Game background
│   │   ├── Base.png          # Ground/base image
│   │   ├── message.png       # Welcome screen message
│   │   ├── pipe.png          # Obstacle pipes
│   │   └── 0.png - 9.jpg     # Number sprites for scoring
│   └── Sound/                 # Game audio files
│       ├── Die.mp3           # Game over sound
│       ├── Hit.mp3           # Collision sound
│       ├── Point.mp3         # Score sound
│       ├── Swoosh.mp3        # Menu navigation sound
│       └── Wing.mp3          # Bird flap sound
└── README.md
```

## ✅ Features Implemented
- **Game Initialization**: PyGame setup with window creation (409x593 resolution)
- **Asset Loading**: Comprehensive loading of game graphics and sound effects
- **Welcome Screen**: Interactive start screen with background, bird, and message
- **Event Handling**: Keyboard input detection (SPACE, UP arrow, ESC)
- **Graphics Rendering**: Sprite blitting and display updates
- **Game Loop Structure**: Main game loop with FPS control (32 FPS)
- **Sound System**: Audio file loading for game sound effects
- **Image Optimization**: Convert alpha for better performance

## 🎯 Current Implementation Status
- ✅ **Welcome Screen**: Fully functional with proper event handling
- ✅ **Asset Management**: All game assets (images/sounds) properly loaded
- ✅ **Game Window**: Proper pygame initialization and window setup
- ✅ **Input System**: Keyboard controls for navigation
- 🔄 **Main Game Loop**: Basic structure implemented (placeholder)
- ❌ **Game Physics**: Not yet implemented
- ❌ **Collision Detection**: Not yet implemented
- ❌ **Scoring System**: Not yet implemented

## 🎮 Controls
- **SPACE** or **UP Arrow**: Start game / Bird flap (when implemented)
- **ESC**: Quit game

## 🚀 How to Run
1. Ensure Python and PyGame are installed:
   ```bash
   pip install pygame
   ```
2. Navigate to the project directory
3. Run the game:
   ```bash
   python main.py
   ```

## 📝 Game Configuration
- **Screen Dimensions**: 409 x 593 pixels
- **FPS**: 32 frames per second
- **Ground Level**: 80% of screen height
- **Game Assets**: Organized in Gallery folder structure

## 🔧 Technical Details
- **Global Variables**: Screen dimensions, FPS, asset paths
- **Image Formats**: PNG and JPG support with alpha channel optimization
- **Audio Formats**: MP3 sound effects
- **Event System**: PyGame event handling for user input
- **Display Management**: Double buffering with pygame.display.update()

## 👨‍💻 Developer
Created by **Mohd.Rehan** as a Python mini-project demonstrating game development skills with PyGame.
