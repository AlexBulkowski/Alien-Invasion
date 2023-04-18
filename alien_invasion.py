import sys
import pygame
from Settings import Settings
from Ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        """ Game in windowed mode: """
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        """ Running in full screen: """
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Alien Invasion')

        #Ship
        self.ship = Ship(self)

        #Bullet
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)


    def check_keydown_events(self, event):
        if event.key == pygame.K_LSHIFT: #Shift
            self.ship.turbo = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_RIGHT: #Right
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT: #Left
            self.ship.moving_left = True
        if event.key == pygame.K_UP: #Top
            self.ship.moving_top = True
        if event.key == pygame.K_DOWN: #Bottom
            self.ship.moving_bottom = True

    def check_keyup_events(self, event):
        if event.key == pygame.K_LSHIFT: #Shift
            self.ship.turbo = False
        if event.key == pygame.K_RIGHT: # Right
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT: #Left
            self.ship.moving_left = False
        if event.key == pygame.K_UP: #Top
            self.ship.moving_top = False
        if event.key == pygame.K_DOWN: #Bottom
            self.ship.moving_bottom = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _fire_bullet(self):
        #limiting number of bullets to shoot at the time
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        """" Disappearing the bullet after reach the screen """
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

if __name__ =='__main__':
    ai = AlienInvasion()
    ai.run_game()

