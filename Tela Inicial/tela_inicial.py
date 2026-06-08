import os
import pygame

# Inicializa o pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ExoKitchen")

# Caminhos dos arquivos
BASE_PATH = os.path.dirname(__file__)

TITLE_PATH = os.path.join(BASE_PATH, "titulo.png")

# Carrega a imagem do título
titulo_img = pygame.image.load(TITLE_PATH).convert_alpha()

# Ajuste o tamanho conforme necessário
titulo_img = pygame.transform.scale(titulo_img, (550, 450))

# Centraliza o título
titulo_rect = titulo_img.get_rect(center=(SCREEN_WIDTH // 2, 180))

# Fonte dos botões
fonte = pygame.font.SysFont("Arial", 28)


class Botao:
    def __init__(self, x, y, largura, altura, texto):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto

    def desenhar(self, tela):
        pygame.draw.rect(tela, (50, 120, 220), self.rect, border_radius=12)

        texto_render = fonte.render(self.texto, True, (255, 255, 255))
        texto_rect = texto_render.get_rect(center=self.rect.center)

        tela.blit(texto_render, texto_rect)

    def clicado(self, pos):
        return self.rect.collidepoint(pos)


# Botões do menu
botao_jogar = Botao(300, 220, 200, 60, "Jogar")
botao_creditos = Botao(300, 300, 200, 60, "Créditos")
botao_sair = Botao(300, 380, 200, 60, "Sair")

running = True

while running:
    display.fill((240, 240, 240))

    # Desenha o título (imagem)
    display.blit(titulo_img, titulo_rect)

    # Desenha os botões
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
                print("Desenvolvido pela equipe ExoKitchen")

            elif botao_sair.clicado(event.pos):
                running = False

    pygame.display.update()

pygame.quit()