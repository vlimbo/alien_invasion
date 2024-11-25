import pygame

class Ship:
    def __init__(self, ai_game):
        # Setting the position of the ship on the screen
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() # Not sure what rect is?

        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.settings = ai_game.settings
        # Allowing us to use floats as ship speed
        self.x = float(self.rect.x)


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Updating the position of the ship on the screen
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
