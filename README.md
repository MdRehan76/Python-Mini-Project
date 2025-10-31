# 🎮 Flappy Bird Game (Python)

A fully functional **Flappy Bird Game** built using the **Python** and **PyGame**, that allows players to enjoy the classic bird-flying experience with enhanced features and multiple game modes.

It features **Dual Game Modes**, **Powerup System**, **Multiple Bird Selection**, **Dynamic Pipe Switching**, and **Enhanced Visual Effects**, offering both functionality and an engaging gameplay experience.

Developed as part of the **Python Mini Project** for academic evaluation.

| Name | Contribution |
|------|-------------|
| **Mohd Rehan** | Game Development, Feature Implementation, Visual Effects |
| **Python Community** | PyGame Library Development and Documentation |

## 💡 Project Overview

The **Flappy Bird Game** allows users to control a bird through obstacle courses efficiently by flapping, avoiding pipes, and collecting powerups for enhanced gameplay.

Each game session provides a **personalized gaming experience** with different bird selections and game modes.

Users can **start playing**, **select birds**, and **switch between game modes** seamlessly.

## ⚙️ Features

### 🎮 Game Modes

- Players can choose **Normal Mode** or **Enemy Mode**
- **Normal Mode**: Classic pipe obstacles with powerup system
- **Enemy Mode**: Bat enemies with background music and faster gameplay
- Each mode has its own **unique background**, **base design**, and **sound effects**

### 🐦 Bird Selection System

- **Multiple bird options**: Default Bird, Blue Bird, Red Bird
- **Interactive bird selection** with circular button interface
- **Dynamic bird switching** during welcome screen
- **Visual preview** of selected bird in game

### 🎯 Powerup System

- **Powerup 1** (Score 5, 20, 35...): Increases pipe gap height by 80%
- **Powerup 2** (Score 10, 25, 40...): Increases horizontal spacing between pipes by 140%
- **Powerup 3** (Score 15, 30, 45...): Provides invulnerability through 3 pipes
- **Visual effects** for each powerup type with glowing animations
- **Pending activation system**: Effects start after skipping the next pipe

### 🎨 Visual Effects & Animation

- **Dynamic pipe switching** every 4 points (pipe.png ↔ pipe1.png)
- **Glowing bird effects** during powerup activation
- **Particle systems** and **sparkle effects** around powered-up bird
- **Burst effects** when collecting powerups
- **Height/Width expansion indicators** for powerup effects
- **Scaling animations** and **pulsing effects**

### 📊 Game Progress & Scoring

- **Real-time score tracking** with number sprite display
- **Highest score persistence** across game sessions
- **Powerup status display** showing active effects and remaining pipes
- **Dynamic scoring** with different mechanics for each game mode

### 🔄 Game Physics & Controls

- **Gravity system** with realistic bird movement
- **Flap mechanics** with velocity and acceleration
- **Collision detection** for pipes, ground, ceiling, and enemies
- **Smooth animations** at 32 FPS for optimal performance

### 🎵 Audio System

- **Background music** for enemy mode with looping
- **Sound effects** for wing flaps, scoring, collisions, and game over
- **Dynamic audio** that responds to game events and mode changes

## 🎯 Core Features

- **Add, navigate, and avoid** obstacles dynamically
- **Collect powerups** for enhanced abilities
- **Switch between** game modes and bird selections
- Set **high scores** and track progress

## 🎮 Game Modes

- **Normal Mode**: Classic Flappy Bird with pipes and powerups
- **Enemy Mode**: Dodge bat enemies with background music and faster pace

## 📱 Game Interface & Rendering

- Built using **Python**, **PyGame**, and **mathematical calculations** for smooth gameplay
- **Dynamic sprite rendering** that loads assets based on game state
- **Responsive visual effects** for better player engagement and feedback
- **Intuitive controls** for flap, restart, and mode selection actions

## �️ Architecture & Game Structure

### 🎯 Architecture

The project follows **Modular Game Development** structure:

**Flow:**
1. Player interacts with welcome screen (UI).
2. Game modes handle gameplay logic and user interactions.
3. Powerup system manages enhanced abilities and visual effects.
4. Rendering engine displays updated game state back to the player.

### �️ Game Structure

| Component | Key Elements | Description |
|-----------|-------------|-------------|
| **Main Game** | mainGame(), collision detection, scoring, powerup handling | Stores core gameplay mechanics and state management |
| **Welcome System** | welcomeScreen(), bird selection, mode selection, event handling | Stores menu interactions linked to game modes |

**Relationships:**
- **One-to-Many**: A single game session can have multiple powerup collections.
- **Mode Selection**: Game mode connects each session to its respective gameplay style.

## 🎨 Design Decisions

1. **Framework Choice**:
   PyGame was chosen for its built-in graphics rendering, sound management, and cross-platform compatibility.

2. **Asset Organization**:
   Gallery folder structure was selected for simplicity and organized asset management during development.

3. **Game Design**:
   - Implemented a **clean and engaging visual style** using sprite animations.
   - Prioritized **smooth gameplay** and **responsive controls** across different systems.
   - Added **visual effects and particle systems** for a professional gaming experience.

4. **Powerup System & Game Modes**:
   - Added **dropdown functionality** for mode selection and bird customization.
   - Integrated **visual feedback systems** and **status indicators** for better player experience.

## 🧠 Concepts Learned

During the development of this project, our team learned and implemented the following core concepts:

### 💎 Python & PyGame Concepts

- Understanding **PyGame's game loop architecture** and **event-driven programming**.
- Working with **Sprite Management** for efficient game object rendering.
- Implementing **collision detection systems** and **physics simulations**.
- Managing **sound effects**, **background music**, and **audio timing**.

### 🤝 Game Development Practices

- Using **modular function design** for maintainable code structure.
- **Object-oriented programming** for game state management and entity handling.
- **Performance optimization** techniques and **memory management**.
- **User interface design** and **interactive menu systems**.

## 🧩 Challenges Faced

1. **Powerup Timing System**:
   Ensuring powerup effects activate at the correct pipe sequence required careful state management using pending activation logic.

2. **Visual Effects Synchronization**:
   Implementing multiple simultaneous visual effects while maintaining smooth 32 FPS performance.

3. **Multi-Mode Game Logic**:
   Balancing different gameplay mechanics between Normal Mode (pipes) and Enemy Mode (bats) while sharing core systems.

## 🚀 Future Improvements

- 📅 **Add Leaderboard System**: Online score tracking and player rankings.
- ⚠️ **Achievement System**: Unlock achievements for score milestones and powerup usage.
- 📆 **Level Progression**: Multiple difficulty levels with varying obstacle patterns.
- 🌙 **Theme Customization**: Additional background themes and seasonal variations.
- 🔍 **Mobile Port**: Adaptation for mobile devices with touch controls.

## 🎮 Controls & Usage

### Game Controls
- **SPACE** or **UP Arrow**: Make the bird flap / Start game
- **Mouse Click**: Navigate menus and restart game
- **ESC**: Exit game

### Welcome Screen
- **Click Bird Button**: Cycle through bird options (Default → Blue → Red)
- **Click Pipe Mode**: Start normal mode with pipes and powerups
- **Click Enemy Mode**: Start enemy mode with bats and background music

### Game Over Screen
- **SPACEBAR**: Restart the game
- **Click Restart Button**: Restart the game (precise clicking required)
- **ESC**: Exit to main menu

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- PyGame library

### Installation Steps

1. **Clone or download the project**:
   ```bash
   git clone https://github.com/MdRehan76/Python-Mini-Project.git
   cd Python-Mini-Project
   ```

2. **Install PyGame**:
   ```bash
   pip install pygame
   ```

3. **Run the game**:
   ```bash
   python main.py
   ```

### Project Structure
```
Python-Mini-Project/
├── main.py                    # Main game file
├── Gallery/
│   ├── Photos/                # Game images and sprites
│   │   ├── Bird.png          # Default bird sprite
│   │   ├── Blue_Bird.png     # Blue bird option
│   │   ├── Red_Bird.png      # Red bird option
│   │   ├── Background.jpg    # Normal mode background
│   │   ├── Background1.png   # Enemy mode background
│   │   ├── Base.png          # Normal mode ground
│   │   ├── Base1.png         # Enemy mode ground
│   │   ├── pipe.png          # Normal pipes
│   │   ├── pipe1.png         # Alternate pipes
│   │   ├── bat.png           # Enemy bat sprite
│   │   ├── powerup1.png      # Height boost powerup
│   │   ├── powerup2.png      # Width boost powerup
│   │   ├── powerup3.png      # Invulnerability powerup
│   │   ├── GameOver.png      # Game over screen
│   │   ├── Flappy_Bird.png   # Game title
│   │   ├── Pipe_Mode.png     # Normal mode button
│   │   ├── Enemy_Mode.png    # Enemy mode button
│   │   └── 0.png - 9.png     # Number sprites for scoring
│   └── Sound/                 # Game audio files
│       ├── Die.mp3           # Game over sound
│       ├── Hit.mp3           # Collision sound
│       ├── Point.mp3         # Score sound
│       ├── Swoosh.mp3        # Menu navigation sound
│       ├── Wing.mp3          # Bird flap sound
│       └── Background1.mp3   # Enemy mode music
└── README.md                  # Project documentation
```

## 🏆 Game Features Summary

- **Dual Game Modes**: Normal (pipes) and Enemy (bats) modes
- **Bird Customization**: 3 different bird sprites to choose from
- **Powerup System**: 3 unique powerups with visual effects
- **Dynamic Obstacles**: Pipes that switch appearance every 4 points
- **Visual Effects**: Glowing birds, particle systems, and animations
- **Audio System**: Complete sound effects and background music
- **High Score Tracking**: Persistent high score across sessions
- **Responsive Controls**: Keyboard and mouse input support
