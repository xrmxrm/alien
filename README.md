# Introduction
This project is based on the *Python Crash Course* book, third edition, from No Starch Press. It uses the Pygame package.

Run the `alien_invasion.py` file to play Alien Invasion.

In Alien Invasion, you control a rocket ship that appears at the bottom center of the screen. You can move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen. You shoot and destroy the aliens. If you destroy all the aliens, a new fleet appears and moves faster than the previous fleet. If any alien hits the ship or reaches the bottom of the screen, you lose a ship. If you lose three ships, the game ends.

# Details
This package relies on the following.

## Scoring
The `gamestats.py` file  contains the `GameStats` class, which maintains game statistics. The `scoreboard.py` file contains the `Scoreboard` class which displays them. 

The game assigns points to each alien you shoot down. If you wipe out an entire fleet, you level up: the next fleet moves faster, and shooting down an alien is worth more points. These changes depend on values in the `Settings` class, defined in the `settings.py` file.

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

