import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()  # Move ship
            self.bullets.update()  # Move all the bullets
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key down event"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        elif event.key == pygame.K_q:
            sys.exit()  
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()     
    
    def _check_keyup_events(self, event):
        """Respond to key up event"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False    

    def _fire_bullet(self):
            """Create new bullet and add it to bullets"""
            if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions.
        self.bullets.update()  # Move all the bullets

        # Delete the bullets that reach the top of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))  # Make sure it's working
                
    def _create_fleet(self):
        """Create fleet of aliens"""
        # Make the first alien and use it as a size guide
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Avoid upper left corner & right edge. Don't get too close to ship 
        left_limit = alien_width
        top_limit = alien_height
        right_limit = self.settings.screen_width - 2 * alien_width
        bottom_limit = self.settings.screen_height - 3 * alien_height
        horizontal_spacing = 2 * alien_width
        vertical_spacing = 2 * alien_height

        current_x, current_y = left_limit, top_limit 
        while current_y < bottom_limit:
            while current_x < right_limit:
                self._create_alien(current_x, current_y)
                current_x += horizontal_spacing
            current_x = left_limit  # Start new row lower by vertical spacing
            current_y += vertical_spacing

    def _create_alien(self, x_position, y_position):
        """Create alien and place in row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)

        # Update bullets, then the ship, then the aliens
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()