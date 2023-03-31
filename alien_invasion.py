import sys
import pygame
from Settings import Settings
from Ship import Ship

class AlienInvasion:
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        #Ship
        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get(): #This function returns a list of events that have taken place...
                if event.type == pygame.QUIT: #...since the last time this function was called Any keyboard or...
                    sys.exit()                #...mouse event will cause this for loop to run
            self.screen.fill(self.settings.bg_color) #Redraw the screen during each pass through the loop
            self.ship.blitme() #setting ship
            pygame.display.flip()

if __name__ =='__main__':
    ai = AlienInvasion()
    ai.run_game()

