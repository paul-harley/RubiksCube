import pygame
import globals

screen = pygame.display.set_mode((globals.SCREEN_HEIGHT, globals.SCREEN_WIDTH))


resume = True

while resume:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False 
    pygame.display.update()
pygame.quit()