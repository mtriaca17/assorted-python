import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
import os

def run_game():
    #initialize the game and create screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #make a ship
    ship = Ship(ai_settings, screen)

    #start main loop for the game
    while True:
        #watch for keyboard and mouse events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        

run_game()