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
│   │   └── 0.png - 9.png     # Number sprites for scoring (all PNG format)
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
  - All 10 number sprites (0-9) in PNG format for scoring display
  - Bird, background, base, message, and pipe graphics
  - 5 audio files for game sound effects
- **Welcome Screen**: Interactive start screen with background, bird, and message
  - Calculated positioning for message (centered horizontally, 10% from top)
  - Bird positioned at 1/7 screen width, vertically centered
  - Base/ground positioned at 80% screen height
- **Event Handling**: Keyboard input detection (SPACE, UP arrow, ESC)
- **Graphics Rendering**: Optimized sprite blitting and display updates
- **Game Loop Structure**: Main game loop with FPS control (32 FPS)
- **Sound System**: Complete audio file loading for game sound effects
- **Image Optimization**: Convert alpha for better performance and transparency support
- **Pipe System**: Dual pipe setup (normal and rotated 180°) for obstacles

## 🎯 Current Implementation Status
- ✅ **Welcome Screen**: Fully functional with proper event handling and positioning
- ✅ **Asset Management**: All 15+ game assets (images/sounds) properly loaded and optimized
- ✅ **Game Window**: Proper pygame initialization and window setup
- ✅ **Input System**: Keyboard controls for navigation (SPACE, UP, ESC)
- ✅ **Sprite Loading**: Complete number system (0-9) and game graphics loaded
- ✅ **Sound Loading**: All 5 game sound effects loaded and ready
- 🔄 **Main Game Loop**: Basic structure with player variables initialized
  - Score tracking variable initialized
  - Player position variables set up
  - Base movement variable ready
- ❌ **Game Physics**: Not yet implemented (bird movement, gravity)
- ❌ **Collision Detection**: Not yet implemented
- ❌ **Scoring System**: Not yet implemented (but number sprites ready)
- ❌ **Pipe Generation**: Not yet implemented (but pipe assets loaded)

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
- **Global Variables**: Screen dimensions (409x593), FPS (32), asset paths
- **Image Formats**: PNG and JPG support with alpha channel optimization
- **Asset Organization**: Structured loading of 10 number sprites, game graphics, and sounds
- **Positioning System**: Mathematical calculations for centered and proportional positioning
- **Audio Formats**: MP3 sound effects (Die, Hit, Point, Swoosh, Wing)
- **Event System**: PyGame event handling for user input with proper exit conditions
- **Display Management**: Double buffering with pygame.display.update()
- **Memory Optimization**: convert_alpha() used for all sprites for better performance
- **Sprite Transformation**: Pipe rotation (180°) for top/bottom obstacle pairs

## 👨‍💻 Developer
Created by **Mohd.Rehan** as a Python mini-project demonstrating game development skills with PyGame.
