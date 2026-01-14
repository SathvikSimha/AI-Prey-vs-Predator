# 🧠 Predator vs Prey – Human vs AI

### *Intelligent Grid-Based Game using Search & Adversarial AI*

---

## 📌 Project Overview

**Predator vs Prey – Human vs AI** is a grid-based strategy game that demonstrates **classical Artificial Intelligence techniques** through an interactive human-vs-AI gameplay experience.

The human player can choose to play as either:

* **Prey** — survive while the AI predator tries to catch you, or
* **Predator** — chase and capture an AI prey that intelligently escapes.

The project showcases **A* Search** and **Minimax with Alpha-Beta Pruning** in a visually understandable and interactive environment.

---

## 🎯 Objectives

* Demonstrate **autonomous intelligent agents**
* Apply **A* search** for optimal escape pathfinding
* Apply **Minimax with Alpha-Beta Pruning** for strategic chasing
* Visualize AI decision-making in real time
* Build a turn-based **Human vs AI** game

---

## 🎮 Game Modes

### 🟦 Human as Prey

* Human tries to survive for a fixed number of turns
* AI Predator uses **Minimax** to chase intelligently

### 🟥 Human as Predator

* Human tries to catch the AI
* AI Prey uses **A*** search to escape optimally

Each human move is followed by an AI response, making the game strategic and interactive.

---

## 🗺️ Game World

* **15×15 grid** environment
* Randomly generated obstacles
* Turn-based movement (Up / Down / Left / Right)
* Obstacles block both human and AI movement

---

## 🧠 AI Techniques Used

### 🟢 AI Prey

* **A* Search Algorithm**
* Heuristic: Maximize distance from predator
* Avoids dead ends and unsafe areas
* Replans path dynamically

### 🔴 AI Predator

* **Minimax Algorithm**
* **Alpha-Beta Pruning** for efficiency
* Predicts human movement
* Chooses optimal chasing strategy

---

## 🛠️ Tech Stack

* **Python 3**
* **Pygame** – visualization & game loop
* **A* Search** – pathfinding
* **Minimax + Alpha-Beta Pruning** – adversarial decision making
* **VS Code / PyCharm** – development
* **GitHub** – version control (optional)

---

## 📂 Project Structure

```
PredatorPreyGame/
├── main.py          # Game loop and mode control
├── grid.py          # Grid and obstacle handling
├── player.py        # Human player logic
├── ai_prey.py       # AI Prey (A* escape logic)
├── ai_predator.py   # AI Predator (Minimax chase logic)
├── settings.py      # Game settings and constants
├── utils.py         # Helper functions (optional)
└── assets/          # (Optional) sprites, sounds
```

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install pygame
```

### 2️⃣ Run the Game

```bash
python main.py
```

### 3️⃣ Choose Mode

In `main.py`, set:

```python
HUMAN_IS_PREY = True   # Human = Prey, AI = Predator
# or
HUMAN_IS_PREY = False  # Human = Predator, AI = Prey
```

---

## 🎮 Controls

* **Move:**

  * Arrow Keys
  * or W / A / S / D
* **Restart:** R key after game over

---

## 🏆 Win Conditions

### If Human is Prey:

* **Win:** Survive for required number of turns
* **Lose:** AI predator catches you

### If Human is Predator:

* **Win:** Catch AI prey
* **Lose:** AI prey survives until timer ends

---

## 📈 Results

* A* significantly improves prey survival
* Minimax improves predator’s chasing efficiency
* Intelligent behavior emerges from simple rules
* Each match feels different due to dynamic obstacles

---

## 🚀 Future Enhancements

* Multiple predators or prey
* Fog-of-war (limited visibility)
* Different terrain types
* Difficulty levels
* Reinforcement learning-based AI
* Enhanced UI & animations

---

## 🎓 Academic Relevance

This project aligns strongly with **Artificial Intelligence syllabus topics**, including:

* Intelligent agents
* State-space search
* Heuristic algorithms
* Adversarial search
* Planning and decision-making

---

## 👨‍💻 Authors

* **Gagan S G**
* **Likith S**
* **S Sathvik**

---

## 📜 License

This project is intended for **academic and educational purposes only**.
