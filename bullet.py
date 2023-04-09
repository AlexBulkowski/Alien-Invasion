from Settings import Settings
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    #Set bullets be fired from the ship
    def __init__(self, ai_game):
        self.settings = Settings()
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create bullet rect at (0,0) and set correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #bullets position
        self.y = float(self.rect.y)
# The Bullet class inherits from Sprite, which we import from the pygame
# .sprite module. use sprites will group related elements in
#  game and act on all the grouped elements at once. To create a bullet
# instance, __init__() needs the current instance of AlienInvasion, and we call
# super() to inherit properly from Sprite. We also set attributes for the screen
# and settings objects, and for the bullet’s color
    def update(self):
        """move bullet up the screen"""
        #update decimal position of the bullet
        self.y -= self.settings.bullet_speed
        #Update the rect position
        self.rect.y = self.y
    def draw_bullet(self):
        """Draw teh bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)