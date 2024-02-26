class Settings:
    """Settings for Alien Invasion"""

    def __init__(self):
        """Initialize settings"""

        # Start with static settings
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship
        self.ship_limit = 3

        # Bullets
        self.bullet_width = 3  # pixels
        self.bullet_height = 15  # pixels
        self.bullet_color = (60, 60, 60)  # dark gray 
        self.bullets_allowed = 3  # Encourage accuracy

        # Aliens
        self.fleet_drop_speed = 10

        # Difficulty increase rate
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # Initialize dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize (reset) settings that change throughout the game"""
        # Ship
        self.ship_speed = 1.5

        # Bullets
        self.bullet_speed = 2.5

        # Aliens
        self.alien_speed = 1.0
        self.fleet_direction = 1  # 1 = right; -1 = left
        
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Speed up game and increase scoring potential"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


