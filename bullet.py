from Settings import Settings
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    #Set bullets be fired from the ship
    def __init__(self, ai_game):
        self.settings = Settings()
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.color = self.setting.bullet_color

        #Create bullet rect at (0,0) and set correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #bullets position
        self.y = float(self.rect.y)
