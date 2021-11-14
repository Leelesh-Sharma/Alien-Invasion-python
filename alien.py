import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_settings,screen) -> None:
        super().__init__()

        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load("IMAGES/Alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y =  self.rect.height

        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)