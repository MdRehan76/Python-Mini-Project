# 🐤 Flappy Bird – Python/PyGame Mini Project 🎮

---

## 👥 Team Members & Contributions

| Name        | Roll No. | GitHub ID                | Contribution Highlights            |
|-------------|----------|--------------------------|------------------------------------|
| **Rehan**    | 328      | [@MdRehan76](https://github.com/MdRehan76)                | Game logic, UI, core framework, Enemy modes     |
| **Tanmay**      | 351      | [@This-is-Tanmay](https://github.com/This-is-Tanmay)           | Physics, collisions, scoring, docs, powerup system |
| **Asmita**      | 331      | [@asmita24beit-cyber](https://github.com/asmita24beit-cyber)       | Art, assets, menu & bug fixes      |
| **Minakshee**   | 338      | [@minakshee24beit-blip](https://github.com/minakshee24beit-blip)     | Sound, animation, tuning & testing |

---

## 🧭 Project Overview

**Flappy Bird – Python/PyGame Edition** is a polished clone of the classic Flappy Bird game, enhanced with **two unique modes**, **dynamic powerups**, **animated visuals**, and **custom sound effects**.

It demonstrates strong fundamentals in **real-time game loop design**, **collision mechanics**, **state management**, and **UI rendering** using the PyGame library.

### 🎯 Highlights
- **Normal Mode** – Classic pipe dodging gameplay with powerups  
- **Enemy Mode** – Introduces flying bats, background music, and advanced invulnerability logic  
- **Dynamic Difficulty** – Pipe visuals switch every few points  
- **Precision Controls** – Restart via spacebar or click detection  
- **Optimized Flow** – Clean loop, minimal lag, and responsive HUD

---

## ✨ Features

✅ **3 Powerups**
- **3 Color Bird Options**: Choose from 3 different bird colors (default, blue, red) available in both normal and enemy modes
- **Powerup System** with score-based spawning:
	- Powerup1 — Height Boost: Appears at Score = 5, 20, 35... (every 15 points starting at 5)
		- Effect: Larger vertical gap for the next 3 pipes
	- Powerup2 — Width Boost: Appears at Score = 10, 25, 40... (every 15 points starting at 10)
		- Effect: Fixed 300px spacing for the next 3 pipes (normal spacing is 150px)
	- Powerup3 — Invulnerability: Appears at Score = 15, 30, 45... (every 15 points starting at 15)
		- Normal mode → lasts 3 pipes
		- Enemy mode → lasts 5 bats; spawns from score 14 (then 29, 44, …)
- Visual polish: score HUD, animated indicators, particles, subtle effects
- Audio: flap, point, hit/die, UI swoosh; background music in enemy mode
- Dynamic pipe sprites: alternate assets used on a 4-point cycle (4/8/12, then repeat)
---

## 🕹️ How to Play

1. **Press** `SPACE` or `UP Arrow` to flap 🕊️  
2. **Avoid** colliding with pipes or bats  
3. **Collect Powerups** to temporarily boost your abilities  
4. **Restart** with `SPACE` or a click after game over  
5. **Enemy Mode:** Invulnerability appears from score **14+**, lasting for **5 bats**

💻 **Quick Start (Windows PowerShell)**
```bash
pip install pygame
python main.py
````

---

## 📁 File Structure

```
Python-Mini-Project/
├── main.py                    # Main game logic & state management
├── requirements.txt           # Dependencies
├── Gallery/
│   ├── Photos/                # All image assets
│   ├── Sound/                 # Sound effects & music
│   └── Screenshots/           # Gameplay screenshots
├── game/
│   ├── constants.py           # Game constants
│   └── game.py                # Additional logic
└── README.md                  # Documentation
```

---

## 🖼️ User Interface & Rendering

* Built using **PyGame surfaces** (frame-by-frame rendering)
* Real-time blitting of sprites over dynamic backgrounds
* Two visual themes:

  * 🌄 Normal Mode (pipes, blue sky)
  * 🌌 Enemy Mode (bats, darker ambience)
* Responsive HUD: score, powerups, invulnerability indicator
* Smooth animation & powerup glow feedback system

---

## 🏗️ Architecture & Design

* **Main Game Loop:** Input → Update → Render
* **Modes:** `normal` (pipes) and `enemy` (bats)
* **Core Functions:**

  * `getPipeType(score)` → Cycles pipe design (4/8/12 pattern)
  * `getPowerupType(score)` → Determines spawn timing
  * `getRandomPipe()` → Computes pipe placement & gap logic
* **Powerup System:**

  * Instant activation
  * Duration varies per mode
  * Invulnerability tracked via HUD counter

---

## 📚 Concepts Learned

* Game-loop architecture in PyGame
* Sprite rendering & layering
* Collision detection (axis-aligned)
* State management & restart logic
* Powerup scheduling & timing control
* Visual synchronization between audio & feedback

---

## 🧩 Challenges Faced

* Managing immediate powerup activation logic
* Maintaining fairness in obstacle spacing
* Balancing visual readability & aesthetics
* Syncing audio cues with gameplay
* Ensuring consistent difficulty across both modes

---

## 🚀 Future Enhancements

* 🏆 Local/Online leaderboard
* 🎯 Achievements for high scores & streaks
* 🔥 More levels & themed obstacles
* ⚙️ Adjustable difficulty settings
* 💡 Performance optimization (sprite atlases, caching)

---

## 📸 Screenshots

| Gameplay Scene      | Preview                                              |
| ------------------- | ---------------------------------------------------- |
| **Welcome Screen**  | ![Welcome](Gallery/Screenshots/Screenshot%201.png)   |
| **Normal Mode**     | ![Normal](Gallery/Screenshots/Screenshot%202.png)    |
| **Enemy Mode**      | ![Enemy](Gallery/Screenshots/Screenshot%204.png )     |
| **Powerup Active** | ![Powerup](Gallery/Screenshots/Screenshot%203.png)  |
| **Game Over**       | ![Game Over](Gallery/Screenshots/Screenshot%205.png) |

---

## 🧰 Tech Stack

| Layer               | Technology                         |
| ------------------- | ---------------------------------- |
| **Language**        | Python                             |
| **Framework**       | PyGame                             |
| **IDE**             | VS Code                            |
| **Version Control** | Git & GitHub                       |
| **Platform**        | Cross-platform (Windows/Linux/Mac) |

---

## 🌿 Git Workflow

| Branch | Purpose                   | Maintained By      |
| ------ | ------------------------- | ------------------ |
| `main` | Final release build       | All members        |
| `dev`  | Development & testing     | Tanmay             |
| `game` | Game logic experiments    | Rehan              |
| `ui`   | Art, sound, and UI tweaks | Asmita & Minakshee |

---