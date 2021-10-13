import sys
import pygame 

def check_events(ship):
    for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False

def update_screen(ai_seetings,screen,ship):
    
    screen.fill(ai_seetings.bg_color)
    
    ship.blitme()

    pygame.display.flip()