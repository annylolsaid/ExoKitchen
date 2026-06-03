import os
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ExoKitchen")

BASE_PATH = os.path.dirname(__file__)
IMAGE_PATH = os.path.join(BASE_PATH, "360_F_239548402_7WZPRebyuCHJAnpw3f4ne9tfVff1LKPJ.jpg")

button_image = pygame.image.load(IMAGE_PATH).convert_alpha()

class Botao:
    def __init__(self, x, y, img):
        self.img = img
        self.rect = self.img.get_rect(topleft=(x, y))

    def desenhar(self, surface):
        surface.blit(self.img, self.rect)


botao_comecar = Botao(25, 50, button_image)
botao_sair = Botao(62, 50, button_image)

running = True
while running:
    display.fill(('white'))

    botao_comecar.desenhar(display)
    botao_sair.desenhar(display)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
