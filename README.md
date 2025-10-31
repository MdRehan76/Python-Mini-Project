Flappy Bird – Python/PyGame Mini Project 🎮

---

1) Project Overview 🎯
This is a polished Flappy Bird-style game built with Python and PyGame. It features two play modes, three collectible powerups that activate immediately on pickup, dynamic pipe visuals that switch every few points, precise restart controls, sound effects, and a clean user interface. The project showcases core game-loop architecture, sprite rendering, collision detection, and state management.

Highlights:
- Normal mode with pipes and powerups
- Enemy mode with flying bats and background music
- Fixed horizontal pipe spacing for consistent difficulty: 150px normally, 300px during Powerup2
- Dynamic pipe skin switching at scores 4, 8, 12 (and repeats)
 - Enemy mode: Powerup3 (invulnerability) starts at score 14, then 29/44…, and lasts for 5 bats

2) Features ✨
- Powerups :
	- Powerup1 — Height Boost: Larger vertical gap for the next 3 pipes
	- Powerup2 — Width Boost: Fixed 300px spacing for the next 3 pipes (normal spacing is 150px)
	- Powerup3 — Invulnerability:
		- Normal mode → lasts 3 pipes
		- Enemy mode → lasts 5 bats; spawns from score 14 (then 29, 44, …)
- Visual polish: score HUD, animated indicators, particles, subtle effects
- Audio: flap, point, hit/die, UI swoosh; background music in enemy mode
- Dynamic pipe sprites: alternate assets used on a 4-point cycle (4/8/12, then repeat)

---

3) How to Play 🕹️
- Press SPACE or the UP arrow to flap the bird
- Avoid colliding with pipes (or bats in enemy mode)
- Fly through gaps to score points; pick up powerups for temporary advantages
- When the game is over, restart with SPACE or by clicking the restart button area
- Enemy mode: from score 14 onward, collect Powerup3 for 5-bat invulnerability; the HUD shows remaining “bats”

Optional quick start on Windows (PowerShell):
```pwsh
pip install pygame
python .\main.py
```

---

4) File Structure 📁
```
Python-Mini-Project/
├── main.py                    # Main game file with all game logic
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── tempCodeRunnerFile.py      # Temporary execution file
├── tempfix.py                 # Temporary fix file
├── __pycache__/               # Python bytecode cache
├── Gallery/                   # Game assets directory
│   ├── Photos/                # Image assets
│   │   ├── Bird.png           # Default bird sprite
│   │   ├── Blue_Bird.png      # Blue bird variant
│   │   ├── Red_Bird.png       # Red bird variant
│   │   ├── Background.jpg     # Normal mode background
│   │   ├── Background1.png    # Enemy mode background
│   │   ├── Base.png           # Normal mode ground
│   │   ├── Base1.png          # Enemy mode ground
│   │   ├── pipe.png           # Default pipe sprite
│   │   ├── pipe1.png          # Alternate pipe sprite
│   │   ├── bat.png            # Enemy bat sprite
│   │   ├── powerup1.png       # Height boost powerup
│   │   ├── powerup2.png       # Width boost powerup
│   │   ├── powerup3.png       # Invulnerability powerup
│   │   ├── GameOver.png       # Game over screen
│   │   ├── Flappy _Bird.png   # Title screen
│   │   ├── Pipe_Mode.png      # Normal mode button
│   │   ├── Enemy_Mode.png     # Enemy mode button
│   │   └── [0-9].png          # Number sprites for scoring
│   ├── Sound/                 # Audio assets
│   │   ├── Wing.mp3           # Bird flap sound
│   │   ├── Point.mp3          # Score point sound
│   │   ├── Hit.mp3            # Collision sound (normal mode)
│   │   ├── Die.mp3            # Death sound
│   │   ├── Swoosh.mp3         # UI/collision sound (enemy mode)
│   │   └── Background1.mp3    # Enemy mode background music
│   └── Screenshots/           # Game screenshots
│       ├── Screenshot 1.png   # Welcome screen
│       ├── Screenshot 2.png   # Normal gameplay
│       ├── Screenshot 3.png   # Enemy mode gameplay
│       ├── Screenshot 4.png   # Powerup effects
│       └── Screenshot 5.png   # Game over screen
└── game/                      # Additional game modules
    ├── __init__.py            # Package initializer
    ├── constants.py           # Game constants
    ├── game.py                # Additional game logic
    └── __pycache__/           # Module bytecode cache
```

---

5) User Interface & Rendering 🖼️
- Built with PyGame surfaces; sprites are blitted each frame over the background and base
- Score is rendered at the top; powerups are drawn as world sprites and collected on overlap
- Two backgrounds/bases (normal and enemy mode) with corresponding obstacles (pipes/bats)
- Visual effects: powerup feedback (e.g., glow/expand cues), spacing indicators during Powerup2
- Enemy-mode powerup3 icon adds a pulsing golden glow, rotating particles, and gentle scaling
- Enemy-mode powerup3 uses safe spawning (no overlap with bats)
- All assets live under `Gallery/Photos` and `Gallery/Sound`

---

6) Architecture & Design 🏗️
- Game loop and state management in `main.py`
	- Welcome screen → gameplay → game-over screen → restart
	- Modes: `normal` (pipes + powerups) and `enemy` (bats + music)
- Key functions:
	- `getPipeType(score)`: cycles pipe sprite variants at 4/8/12 points (repeats)
	- `getPowerupType(score)`: schedules which powerup to spawn by score milestone
	- `getRandomPipe()`: computes the upper/lower pipe positions and applies active powerups
- Powerup system:
	- Immediate activation on collection
	- Duration tracked per mode (pipes in normal mode; bats in enemy mode)
	- Enemy-mode Powerup3: spawns at 14 + 15n, lasts 5 bats, HUD shows “bats” remaining
	- Fixed horizontal spacing in pipe generation:
		- 150px normally; 300px during Powerup2 (next 3 pipes)
- Assets and sounds are loaded once and cached in dictionaries (`Game_Photos`, `Game_Sound`)

---

7) Concepts Learned 📚
- Building a real-time game loop (input → update → render) at a fixed timestep
- Sprite rendering, layering, and simple particle/indicator effects
- Axis-aligned collision checks for player vs. obstacles/powerups
- State machines for screens (welcome, gameplay, game over) and modes (normal/enemy)
- Timing and duration-based mechanics (powerups lasting for N pipes)
- Deterministic obstacle generation with tunable difficulty via spacing and gap size

---

8) Challenges Faced 🧩
- Powerup timing: switching from "delayed" to "immediate" activation without side-effects
- Consistent feel: keeping spacing and gap sizes fair when powerups start/stop
- Restart UX: allowing spacebar and precise click region without accidental restarts
- Asset cohesion: balancing visibility/readability of sprites, backgrounds, and HUD
- Mode parity: ensuring enemy-mode scoring and pacing feel comparable to normal mode

---

9) Future Improvements 🚀
- Leaderboard with high scores (local file or online backend)
- Achievements for score milestones and no-hit runs
- Additional obstacles and themed levels; daily challenges
- Accessibility options: adjustable base difficulty (gap size, gravity)
- Performance/asset pipeline tweaks (sprite atlases, lazy loads)

---

Screenshots 

![alt text](<Gallery/Screenshots/Screenshot 1.png>)
![alt text](<Gallery/Screenshots/Screenshot 2.png>)
![alt text](<Gallery/Screenshots/Screenshot 3.png>)
![alt text](<Gallery/Screenshots/Screenshot 4.png>)
![alt text](<Gallery/Screenshots/Screenshot 5.png>)