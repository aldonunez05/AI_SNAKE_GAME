# AI Snake Game with A* Pathfinding

A Python-based AI-powered Snake game that uses the A* search algorithm to autonomously find the optimal path to food while avoiding collisions with itself and walls. The game is built using the Pygame library for real-time graphics rendering and grid-based movement.

## Features

- **Autonomous Snake AI**: Uses the A* pathfinding algorithm to make intelligent decisions in real time.
- **Grid-Based Game Logic**: The snake navigates a discretized 2D grid environment.
- **Real-Time Rendering**: Built with Pygame to render smooth graphics and animations.
- **Dynamic Difficulty**: The AI must continually adjust its path as the snake grows longer.

## How It Works

- The game grid is defined as a matrix of cells.
- The snake AI uses the A* algorithm to compute the shortest safe path to the food.
- Each move considers all valid directions, avoiding collisions with the snake's body and walls.
- Upon consuming food, the snake grows, and new food is placed randomly on the grid.

## Technologies Used

- **Python 3**
- **Pygame** for graphics and event handling
- **Heapq** for priority queue management in A* implementation

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/aldonunez05/ai-snake-game.git
   cd ai-snake-game
2. Install dependencies
   ```bash
    pip install pygame
   ```
   Debian based systems:
   
   ```bash
    sudo apt-install python3-pygame
   ```

   Arch based systems:
   ```bash
   sudo pacman -S python3-pygame
4. Run the game
   ```bash
    python snake_ai.py
Screenshots
![Screenshot 2025-04-29 150700](https://github.com/user-attachments/assets/17768f69-b429-4b32-b56c-f23403a5d783)

## Future Improvements
Add a scoring system and UI.

Implement more advanced AI (e.g. Hamiltonian cycles, BFS fallback).

Add a manual vs. AI play mode.

Refactor into an object-oriented design for scalability.

## License
This project is open source under the MIT License.

## Author
Aldo Nunez
