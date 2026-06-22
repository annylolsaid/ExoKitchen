import os
import pygame
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ExoKitchen")

BASE_PATH = os.path.dirname(__file__)

TITLE_PATH = os.path.join(BASE_PATH, "titulo.png")
BG_PATH = os.path.join(BASE_PATH, "background.png")

titulo_img = pygame.image.load(TITLE_PATH).convert_alpha()
titulo_img = pygame.transform.scale(titulo_img, (540, 455))
titulo_rect = titulo_img.get_rect(center=(SCREEN_WIDTH // 2, 180))


class Fundo:
    def __init__(self, bg_path):
        self.bg = pygame.image.load(bg_path).convert_alpha()  # corrigido: () no convert_alpha
        self.img_x = self.bg.get_width()
        self.tiles = math.ceil(SCREEN_WIDTH / self.img_x) + 1  # +1 para cobrir a borda direita
        self.scroll = 0  # estado persistente como atributo da instância

    def atualizar(self):
        self.scroll -= 0.5
        if self.scroll <= -self.img_x:  # reseta o scroll quando a imagem sai completamente
            self.scroll = 0

    def desenhar(self, superficie):
        for i in range(self.tiles):
            superficie.blit(self.bg, (i * self.img_x + self.scroll, 0))


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


# instanciado ANTES do loop
fundo = Fundo(BG_PATH)

botao_jogar    = Botao(300, 250, 200, 75, "Jogar",    os.path.join(BASE_PATH, "botão_jogar.png"))
botao_creditos = Botao(300, 335, 200, 75, "Créditos", os.path.join(BASE_PATH, "botão_créditos.png"))
botao_sair     = Botao(300, 420, 200, 75, "Sair",     os.path.join(BASE_PATH, "botão_sair.png"))

running = True

while running:
    # fundo substitui o display.fill — desenha antes de tudo
    fundo.atualizar()
    fundo.desenhar(display)

    display.blit(titulo_img, titulo_rect)
    botao_jogar.desenhar(display)
    botao_creditos.desenhar(display)
    botao_sair.desenhar(display)

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