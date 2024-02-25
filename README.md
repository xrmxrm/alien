# Introduction
This project is based on the *Python Crash Course* book. It uses the Pygame package.

Run the `alien_invasion.py` file to play Alien Invasion.

In Alien Invasion, you control a rocket ship that appears at the bottom center of the screen. You can move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen. You shoot and destroy the aliens. If you destroy all the aliens, a new fleet appears and moves faster than the previous fleet. If any alien hits the ship or reaches the bottom of the screen, you lose a ship. If you lose three ships, the game ends.

# Details
Here is an overview of what the parts of this package do.

## alien_invasion.py

The main file, `alien_invasion.py`, contains the `AlienInvasion` class. This class creates attributes used throughout the game. It puts settings in `settings.py`. It creates a playing screen and a `Ship` instance. 

The `AlienInvasion` class also contains the main loop of the game. It calls `_check_events`, `ship.update`, and `_update_screen`. It also ticks the clock on each pass through the loop.

The `_check_events` method detects relevant events, such as keypresses and releases, and processes each of these types of events through the methods `_check_keydown`_events and `_check_keyup_events`. These methods manage the ship’s movement. The AlienInvasion class also contains `_update_screen`, which redraws the screen on each pass through the main loop.

## settings.py

The `settings.py` file contains the `Settings` class, which initializes attributes controlling the game's appearance, ship speed, and bullet characteristics.

## ship.py

The `ship.py` file contains the `Ship` class. Its `update` method manages the ship's position, and its `blitme` method draws the ship on the screen.

## bullet.py

The `bullet.py` file contains the `Bullet` class, which inherits from `Sprite` (from `pygame.sprite`). Sprites enable you to group related elements and act on all the grouped elements at once. Bullets are Pygame rectangles -- they do not have an associated bitmap image. 
