import pygame.font

class Button:
    """Represent a game button"""

    def __init__(self, ai_game, msg):
        # Button attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Button's rect object, centered
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button text needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Render msg as an image and center it on the button"""
        self.msg_image = self.font.render(
            msg,   # Button text
            True,  # Antialiasing on
            self.text_color, # Text color
            self.button_color  # Background color -- None = transparent
            )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button, then draw button text"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)