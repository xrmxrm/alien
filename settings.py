class Settings:
    """Settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship
        self.ship_speed = 1.5

        # Bullets
        self.bullet_speed = 2.0
        self.bullet_width = 3  # pixels
        self.bullet_height = 15  # pixels
        self.bullet_color = (60, 60, 60)  # dark gray        