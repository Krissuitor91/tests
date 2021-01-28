import pygame

class Ship:

    def __init__(self, ai_game):
        """Initialize the ship and set it's starting location."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """Load the ship image and get it's rect."""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        """Start each new ship at bottom center of the screen."""
        self.rect.center = self.screen_rect.midleft

        """Store a decimal value for the ships vertical position."""
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        """Movement flags."""
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update position based on movement flag."""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed



    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)
