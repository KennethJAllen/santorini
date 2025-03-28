# Santorini

[Santorini](https://en.wikipedia.org/wiki/Santorini_(game)), is an abstract board game, first [published in 2004](https://boardgamegeek.com/boardgame/9963/santorini). It is a two to three player game that is typically played on a $5 \times 5$ grid.

![Santorini being played](/images/santorini.png)

## 📜 Rules
The [rules](http://www.boardspace.net/santorini/english/santorini-rules.html) are fairly simple. Each player sets up the game by placing two workers on the board. Each turn, a worker can be moved to an adjacent square, followed by building on a square adjacent to the square that worker just moved to.

Building increases the height of that square by one. The move destination space must be unoccupied by a worker. The height must be no more than one level higher than your starting height. If a worker builds on a space with height three, that space is capped and can no longer be moved to or built on.

When a player's piece reaches the third level, that player wins. If a player cannot move any of their pieces, that player loses.

## ♟️ Playing the Game

### In the browser

To play in the browser, visit https://www.kennethallenmath.com/santorini/.

Note: If autoplay is blocked, a refresh might be required.

### Using `main.py`

To play the game, execute the script `main.py`.

The user can interact with the game via UI generated by pygame.

## 🔧 Installation

### Clone the Repository:

```
git clone https://github.com/KennethJAllen/santorini
cd santorini
```
### Install Dependencies with Poetry:

*   Install Poetry if not already installed.
*   Run the following command in the project directory:

```
poetry install
```
### Activate the Virtual Environment:
```
poetry shell
```
You can now run the project's scripts within the poetry shell.

## Credits

Python WebAssembly by Pygbag.

Assets were created with Aseprite.
