# import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion - Leelesh")
    
    ship = Ship(screen, ai_settings)

    alien = Alien(ai_settings, screen)

    bullets = Group()

    while True:
        
        gf.check_events(ai_settings,screen,ship,bullets)
        
        ship.update()
        
        gf.update_bullet(bullets)

        gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()