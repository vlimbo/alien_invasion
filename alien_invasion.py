import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        # Initialize the background settings
        pygame.init()

        # Creating a clock to make sure we get consistent fps
        self.clock = pygame.time.Clock() # Again this creates an object
        self.settings = Settings()

        # Set the screen size of the game
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        # Creating an instance of ship class
        # Passing an instance of the AlienInvasion to the ship class
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # This refers to the acutal key that was pressed using event.key
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 1



    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
