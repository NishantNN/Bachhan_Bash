🎮 Bachhan-Bash

A simple 2D arcade-style shooting game built using Python and Pygame, inspired by classic space-invader mechanics. The player controls a spaceship, shoots incoming enemies, and tries to achieve the highest possible score before enemies reach the danger zone. The game contains explicit use of 18+ language. Viewer description is advised.

📌 Overview

Bachhan-Bash is a single-player desktop game where:

The player moves horizontally at the bottom of the screen

Enemies spawn at the top and move sideways while slowly descending

The player fires bullets to destroy enemies

The game ends if any enemy crosses a vertical limit

Scores and high scores are displayed and stored persistently

🧠 Core Features

Real-time gameplay loop using Pygame

Multiple enemies with independent movement

Bullet firing with collision detection

Persistent high score storage using pickle

Background music and sound effects

Game over detection and display

Screen boundary enforcement

🎮 Controls
Key	Action
Left Arrow	Move player left
Right Arrow	Move player right
Spacebar	Fire bullet
Close Window	Exit game
🖥️ Screen & Gameplay Details

Screen Resolution: 800 × 600

Player Movement: Horizontal only

Number of Enemies: 6

Bullet System: Single bullet at a time

Game Over Condition: Enemy Y-position > 430

📁 Required Files

All files must be in the same directory as the Python script.

Images

amitab.png – Enemy sprite and game icon

space-game.png – Player sprite

fire.png – Bullet sprite

bg.jpg – Background image

Audio

background.wav – Background music (looped)

aagg.mp3 – Enemy hit sound

mkb_aagg.mp3 – Game over sound

Data

highscore.dat – Auto-generated file storing the high score

🧩 Dependencies

Python 3.x is required.

Install Pygame:

pip install pygame


Modules used:

pygame

pygame.mixer

random

math

pickle

💾 High Score System

High score is stored locally using Python’s pickle module

Saved in highscore.dat

Automatically loaded at startup

Updated only if the current score exceeds the stored high score

⚙️ Game Logic Summary

Game Loop: Runs continuously until quit

Input Handling: Keyboard-based movement and firing

Enemy Behavior:

Horizontal movement

Direction reversal on screen edges

Gradual vertical descent

Collision Detection:

Based on Euclidean distance

Collision threshold ≈ 50 pixels

Bullet Mechanics:

One bullet active at a time

Bullet resets after collision or leaving the screen

⚠️ Known Limitations

Enemy drawing function is poorly structured (defined inside a loop)

No restart or reset option after game over

Heavy use of hardcoded values

No object-oriented structure

Approximate collision detection

Limited gameplay depth due to single-bullet system

This is learning-level code, not production-quality.

🚀 How to Run
python main.py


(Replace main.py with your actual filename.)

🧠 Intended Purpose

Learn Pygame fundamentals

Understand game loops and event handling

Practice collision detection

Learn file handling using pickle

📜 License

Free to use, modify, and experiment with for educational purposes.