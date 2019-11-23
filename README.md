# Tetris + Autoplayer

A reenvisioned version of Alexey Pajitnov's orignal Tetris game with a built-in autoplayer. Tetris has been released for virtually every computer and electronic gaming system, and it is often revered as a classic. Though numerous sequels have been spawned, Tetris games almost always have the same play mechanics: differently shaped blocks drop at varying speeds, and, as the blocks descend, the player must rotate and arrange them to create an uninterrupted horizontal row on the screen. When the player forms one or more solid rows, the completed rows disappear. The goal of the game is to prevent the blocks from stacking up to the top of the screen for as long as possible. This version of the game essentially uses the same mechanics, but comes with an auto-player.

![demo](/demo.gif)

The auto-player algorithm is a very simple genetic algorithm. It does the following:

1. Look at the current block and the next block and simulate ALL possible combinations (positions and rotations) of the two blocks.
2. Calculate a score for each of the positions.
3. Move the block to the position with the highest score and repeat.

To calculate the score, the auto-player uses parameters such as the  height of each column, the number of inaccesible holes a move would create, the jaggedness/variation between column heights and the number of lines a move would clear. Naturally, each paramter is assigned a different weight.

# Usage

The game is implemented to work using ```tkinter```, ```pygame```, and can also be displayed on the command line in a terminal window.

### To run the game with the autoplayer, execute:

```python3 visual.py``` if you wish to launch the game using ```tkinter```

```python3 visual-pygame.py``` if you wish to launch the game using ```pygame```

```python3 cmdline.py``` if you wish to launch the on the command line.

### To play the game yourself, execute:

```python3 visual.py -m``` if you wish to launch the game using ```tkinter```

```python3 visual-pygame.py -m``` if you wish to launch the game using ```pygame```

```python3 cmdline.py -m``` if you wish to launch the on the command line.
