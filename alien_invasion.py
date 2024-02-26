import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
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

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        self.game_active = False  # Let player decide when to start
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()  # Move ship
                self._update_bullets()  # Move all the bullets
                self._update_aliens()  # Move all aliens
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos) 

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

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
        elif event.key == pygame.K_p  and not self.game_active: 
            self._start_game()

    
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

        # Delete bullets that reach the top of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # If bullet hits alien, delete both
        _ = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
        # If all aliens shot down
        if not self.aliens:
            # Delete all bullets, create new fleet, speed up game
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
                
    def _update_aliens(self):
        """Update entire alien fleet -- turn and drop at edge"""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

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

    def _check_fleet_edges(self):
        """Check for aliens at edge and act accordingly"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop fleet and reverse its direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Ship hit -- clear bullets & aliens. Start again or die"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Give player time to notice
            sleep(0.5)
        else:
            self.game_active = False 
            pygame.mouse.set_visible(True)   

    def _start_game(self):
        self.stats.reset_stats()  # Reset game stats
        self.game_active = True

        self.settings.initialize_dynamic_settings()  # Reset level

        self.bullets.empty() # Clear old game
        self.aliens.empty()

        self._create_fleet()  # Start a new one
        self.ship.center_ship()

        pygame.mouse.set_visible(False)  # Hide cursor


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)

        # Update bullets, then the ship, then the aliens
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()