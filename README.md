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

4) User Interface & Rendering 🖼️
- Built with PyGame surfaces; sprites are blitted each frame over the background and base
- Score is rendered at the top; powerups are drawn as world sprites and collected on overlap
- Two backgrounds/bases (normal and enemy mode) with corresponding obstacles (pipes/bats)
- Visual effects: powerup feedback (e.g., glow/expand cues), spacing indicators during Powerup2
- Enemy-mode powerup3 icon adds a pulsing golden glow, rotating particles, and gentle scaling
- Enemy-mode powerup3 uses safe spawning (no overlap with bats)
- All assets live under `Gallery/Photos` and `Gallery/Sound`

---

5) Architecture & Design 🏗️
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

6) Concepts Learned 📚
- Building a real-time game loop (input → update → render) at a fixed timestep
- Sprite rendering, layering, and simple particle/indicator effects
- Axis-aligned collision checks for player vs. obstacles/powerups
- State machines for screens (welcome, gameplay, game over) and modes (normal/enemy)
- Timing and duration-based mechanics (powerups lasting for N pipes)
- Deterministic obstacle generation with tunable difficulty via spacing and gap size

---

7) Challenges Faced 🧩
- Powerup timing: switching from “delayed” to “immediate” activation without side-effects
- Consistent feel: keeping spacing and gap sizes fair when powerups start/stop
- Restart UX: allowing spacebar and precise click region without accidental restarts
- Asset cohesion: balancing visibility/readability of sprites, backgrounds, and HUD
- Mode parity: ensuring enemy-mode scoring and pacing feel comparable to normal mode

---

8) Future Improvements 🚀
- Leaderboard with high scores (local file or online backend)
- Achievements for score milestones and no-hit runs
- Additional obstacles and themed levels; daily challenges
- Accessibility options: adjustable base difficulty (gap size, gravity)
- Performance/asset pipeline tweaks (sprite atlases, lazy loads)

---

