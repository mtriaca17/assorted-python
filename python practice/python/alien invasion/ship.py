import pygame
import os
class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen

        #load ship image and get its rect
        self.image = pygame.image.load('alien invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect= screen.get_rect()
        self.ai_settings = ai_settings

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for ship's center
        self.center = float(self.rect.centerx)

        #movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """update based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

print(os.getcwd())