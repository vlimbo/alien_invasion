import pygame

class Ship:
    def __init__(self, ai_game):
        # Setting the position of the ship on the screen
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() # Not sure what rect is?

        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()


        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
