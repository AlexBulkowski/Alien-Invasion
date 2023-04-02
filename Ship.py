import pygame
from Settings import Settings

class Ship:
    def __init__(self, ai_game):
        #setting starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.size = (100, 100)
        self.settings = Settings()


        #Load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, self.size) #setting new size
        self.rect = self.image.get_rect()


        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Value for horizontal position
        self.x = float(self.rect.x)

        #Movement
        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x #Updateing rect object


    def blitme(self):
        #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)




""" n Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates 
increase as you go down and to the right. On a 1200 by 800 screen, the origin is 
at the top-left corner, and the bottom-right corner has the coordinates (1200, 800). 
These coordinates refer to the game window, not the physical screen. """