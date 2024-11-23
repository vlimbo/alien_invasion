import sys
import pygame
from settings import Settings

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

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
