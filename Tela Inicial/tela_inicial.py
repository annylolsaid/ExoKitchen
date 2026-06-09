import os
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ExoKitchen")

BASE_PATH = os.path.dirname(__file__)

TITLE_PATH = os.path.join(BASE_PATH, "titulo.png")

titulo_img = pygame.image.load(TITLE_PATH).convert_alpha()

titulo_img = pygame.transform.scale(titulo_img, (550, 450))

titulo_rect = titulo_img.get_rect(center=(SCREEN_WIDTH // 2, 180))


class Botao:
    def __init__(self, x, y, largura, altura, texto, sprite_path):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.sprite = self.carrega_sprite(sprite_path)

    def carrega_sprite(self, path):
        imagem = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(imagem, (self.rect.width, self.rect.height))

    def desenhar(self, superficie):
        if self.sprite:
            superficie.blit(self.sprite, self.rect)

    def clicado(self, pos):
        return self.rect.collidepoint(pos)

botao_jogar   = Botao(300, 300, 200, 60, "Jogar",    os.path.join(BASE_PATH, "botão_jogar.png"))
botao_creditos = Botao(300, 370, 200, 60, "Créditos", os.path.join(BASE_PATH, "botão_créditos.png"))
botao_sair    = Botao(300, 440, 200, 60, "Sair",     os.path.join(BASE_PATH, "botão_sair.png"))

running = True

while running:
    display.fill((240, 240, 240))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if botao_jogar.clicado(event.pos):
                print("Iniciando jogo...")

            elif botao_creditos.clicado(event.pos):
                print("Créditos:")
                print("Desenvolvido pela ExoTeam")

            elif botao_sair.clicado(event.pos):
                running = False

    pygame.display.update()

pygame.quit()