import pygame

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ExoKitchen")

loop = True

while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    
pygame.quit()