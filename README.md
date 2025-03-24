<h1 align="center">Othello</h1>
<p align="center">
  <img src="https://github.com/tings17/prj-othello/assets/yourID/screenshot.png" alt="Othello Game Screenshot" width="600">
</p>
<p align="center">
  A recreation of the classic Othello/Reversi board game with AI implementation using minimax algorithm with alpha-beta pruning.
  <br />
</p>
<p align="center">
  <a href="https://github.com/tings17/prj-othello"><strong>Explore the repo »</strong></a>
</p>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#game-rules">Game Rules</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#ai-implementation">AI Implementation</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



## About The Project
This project is a Python implementation of the classic board game Othello (also known as Reversi). It features:
* A user-friendly GUI built with Pygame
* Multiple AI difficulty levels using the minimax algorithm with alpha-beta pruning
* Player selection menu to choose between human and AI players
* Real-time move highlighting and score tracking

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Game Rules
Othello is played on an 8×8 board. The game pieces, called discs, are white on one side and black on the other.

* The game begins with four discs placed in the center of the board, forming a square with same-colored pieces on a diagonal
* Black moves first, placing a disc on the board to capture at least one white disc
* Capture occurs when a disc is placed such that it creates a straight line (horizontal, vertical, or diagonal) between the new disc and another disc of the same color, with one or more of the opponent's discs in between
* Captured discs are flipped to the player's color
* Players take turns placing discs on the board
* If a player cannot make a valid move, their turn is skipped
* The game ends when neither player can make a valid move or when the board is full
* The player with the most discs of their color on the board wins

### Built With

* Python
* Pygame
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Python
* Pygame library 
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/tings17/prj-othello.git
   ```
2. Navigate to the project directory
   ```sh
   cd prj-othello
   ```
5. Install the required packages
    ```sh
    pip install pygame
    ```
6. Run the game
    ```sh
    python main.py
    ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
After launching the game, you'll see a player selection menu where you can choose:
1. Player settings
* Human - For manual play
* Easy AI - Basic computer opponent
* Medium AI - Moderate difficulty computer opponent
* Hard AI - Challenging computer opponent

2. Sidebar and game features
* Click on valid moves (highlighted on the board)
* The sidebar displays current score and whose turn it is
* Game automatically handles turn switching and calculating valid moves


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## AI Implementation
The AI uses the minimax algorithm with alpha-beta pruning to determine the best move:

* Easy AI: Searches 1 move ahead
* Medium AI: Searches 2 moves ahead
* Hard AI: Searches 3 moves ahead

The evaluation function considers:

* Piece count
* Board position value
* Mobility (number of available moves)
* Stability of pieces

<!-- ROADMAP -->
## Roadmap

- [X] Player set up menu
- [X] AI players with varying levels
- [ ] Enhanced design
- [ ] Improved heuristics

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

tingsun0517@gmail.com

Project Link: [https://github.com/tings17/prj-othello](https://github.com/tings17/prj-othello)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
