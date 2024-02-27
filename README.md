# Introduction
This project is based on  *Python Crash Course* by Eric Matthes, third edition, from No Starch Press.

Run the `alien_invasion.py` file to play Alien Invasion. Press the Play button on the screen that appears (or press the P key) to start.

You control a rocket ship that appears at the bottom center of the screen. When the game begins, a fleet of aliens fills the screen above your ship. The fleet moves horizontally across the screen. It changes direction and moves downward if any alien reaches an edge.

You use arrow keys and the spacebar to move horizontally and shoot bullets. Hitting an alien with a bullet destroys the alien. The game gives you points for each alien you shoot down. If you wipe out an entire fleet, you level up: the next fleet moves faster, and shooting down an alien is worth more points. 

If any alien hits your ship or reaches the bottom of the screen, you lose a ship (that is, you die). You return to level 1, but you keep your score. A new fleet appears, moving at the original speed, and you get a new ship. If you lose 3 times, the Play button appears. You can press it to play again, at which point your score reverts to 0, but the high score remains. If you type the Q key or close the window, the program exits.

A screen graphic shows as many ship images as you have lives left. The screen also shows your level and score and your highest score since you started the program. If you exit the program, the high score reverts to 0 next time you start.

# Details
The Python implementation uses the Pygame package. Its Sprite class enables groups of similar items (like aliens or bullets) to be processed efficiently.

The `AlienInvasion` class (in `alien_invasion.py`) contains the main loop, which checks for and processes keyboard, mouse, and clock events, then updates the game model (really just a bunch of values stored in various classes) and the screen display.

## Scoring
The `gamestats.py` file  contains the `GameStats` class, which maintains game statistics. The `scoreboard.py` file contains the `Scoreboard` class which displays them. The program converts numbers to screen images to be updated every time the display is redrawn. 

## Game mechanics
These changes depend on values in the `Settings` class, defined in the `settings.py` file.

The game displays your score and level, the number of lives (ships) you have left, and the high score. If the game ends, you can press the Play button (or the P key) to play another. The high score continues from one play to the next, until you quit the game (type Q or close the window).

High score resets when you quit the game. Not implemented (yet) is an all-time high score, which requires persistent storage.

## images
The images directory contains the bitmap images of the player's ship and the aliens.

## alien_invasion.py

The main file, `alien_invasion.py`, contains the `AlienInvasion` class. This class creates attributes used throughout the game. It puts settings in `settings.py`. It creates a playing screen and a `Ship` instance. 

The `AlienInvasion` class also contains the main loop of the game. It calls `_check_events`, `ship.update`, and `_update_screen`. It also ticks the clock on each pass through the loop.

The `_check_events` method detects relevant events, such as keypresses and releases, and processes each of these types of events through the methods `_check_keydown`_events and `_check_keyup_events`. These methods manage the ship’s movement. The AlienInvasion class also contains `_update_screen`, which redraws the screen on each pass through the main loop.

This file contains a lot of code. It needs refactoring.

## settings.py

The `settings.py` file contains the `Settings` class, which initializes attributes controlling the game's appearance, ship speed, bullet characteristics, and scoring. It contains both static and dynamic settings. The static settings might be better driven from an external initialization file. That would enable persistent storage for something like "highest score ever."

## alien.py

The alien.py file contains the Alien class, which, like bullet.py, inherits from Sprite. Like bullets, aliens are processed in a group.

## bullet.py

The `bullet.py` file contains the `Bullet` class, which inherits from `Sprite` (from `pygame.sprite`). Sprites enable you to group related elements and act on all the grouped elements at once. Bullets are Pygame rectangles -- they do not have an associated bitmap image. 

## ship.py

The `ship.py` file contains the `Ship` class. Its `update` method manages the ship's position, and its `blitme` method draws the ship on the screen. Only one ship appears on the screen, but `Ship` inherits from Sprite to enable a visual display of the number of ships (lives) remaining.

