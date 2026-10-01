import math
import os

import pygame

from personagens import Hoshigo
from mapa import Mapa
from inimigos import AlienCalmo
from pedidos import Pedido
from cozinha import Cozinha
from hud import HUD


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
MENU_PATH = os.path.join(BASE_PATH, "Tela_Inicial")


class Fundo:
    def __init__(self, bg_path):
        self.bg = pygame.image.load(bg_path).convert_alpha()
        self.img_x = self.bg.get_width()
        self.tiles = math.ceil(800 / self.img_x) + 1
        self.scroll = 0

    def atualizar(self):
        self.scroll -= 0.5
        if self.scroll <= -self.img_x:
            self.scroll = 0

    def desenhar(self, superficie):
        for i in range(self.tiles):
            superficie.blit(self.bg, (i * self.img_x + self.scroll, 0))


class Botao:
    def __init__(self, x, y, largura, altura, sprite_path):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (largura, altura))

    def desenhar(self, superficie):
        superficie.blit(self.sprite, self.rect)

    def clicado(self, pos):
        return self.rect.collidepoint(pos)


def iniciar_jogo():
    pygame.init()

    largura = 800
    altura = 500
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Exo Kitchen")

    clock = pygame.time.Clock()
    fps = 60

    mapa = Mapa()
    jogador = Hoshigo(100, 250)
    alien = AlienCalmo("Zorblax", 700, 90)
    pedido = Pedido()
    pedido.gerar_pedido()
    cozinha = Cozinha()
    hud = HUD()

    tempo = 300
    fonte = pygame.font.SysFont("Arial", 20)
    mensagem = ""

    e_pressionado = False
    f_pressionado = False
    rodando = True

    while rodando:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()

        jogador.mover()
        mapa.colisao(jogador)
        alien.atualizar()

        tempo -= 1 / fps
        if tempo < 0:
            tempo = 0

        mensagem = ""

        pegar = False
        if teclas[pygame.K_e] and not e_pressionado:
            pegar = True
        e_pressionado = teclas[pygame.K_e]

        ingredientes = [
            ("Tomate", mapa.tomate),
            ("Queijo", mapa.queijo),
            ("Carne", mapa.carne),
            ("Pão", mapa.pao),
            ("Massa", mapa.massa),
        ]

        for nome, objeto in ingredientes:
            if jogador.rect.colliderect(objeto):
                mensagem = f"Pressione E para pegar {nome}"
                if pegar:
                    cozinha.adicionar_ingrediente(nome)

        entregar = False
        if teclas[pygame.K_f] and not f_pressionado:
            entregar = True
        f_pressionado = teclas[pygame.K_f]

        if jogador.rect.colliderect(alien.rect):
            mensagem = "Pressione F para entregar"

            if entregar:
                prato = cozinha.entregar()

                if pedido.verificar(prato):
                    jogador.adicionar_pontos(20)
                    alien.reagir()
                    print("Pedido correto!")
                else:
                    jogador.perder_vida()
                    print("Pedido errado!")

                pedido.novo_pedido()

        mapa.desenhar(tela)
        alien.desenhar(tela)
        jogador.desenhar(tela)
        hud.desenhar(tela, jogador, alien, pedido, tempo, cozinha)

        if mensagem != "":
            pygame.draw.rect(tela, (0, 0, 0), (200, 455, 400, 30))
            texto = fonte.render(mensagem, True, (255, 255, 255))
            tela.blit(texto, (215, 460))

        pygame.display.flip()

    pygame.quit()


def mostrar_menu():
    pygame.init()

    largura = 800
    altura = 500
    display = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("ExoKitchen")

    title_path = os.path.join(MENU_PATH, "titulo.png")
    bg_path = os.path.join(MENU_PATH, "background.png")

    titulo_img = pygame.image.load(title_path).convert_alpha()
    titulo_img = pygame.transform.scale(titulo_img, (540, 455))
    titulo_rect = titulo_img.get_rect(center=(largura // 2, 180))

    fundo = Fundo(bg_path)
    botao_jogar = Botao(300, 250, 200, 75, os.path.join(MENU_PATH, "botão_jogar.png"))
    botao_creditos = Botao(300, 335, 200, 75, os.path.join(MENU_PATH, "botão_créditos.png"))
    botao_sair = Botao(300, 420, 200, 75, os.path.join(MENU_PATH, "botão_sair.png"))

    running = True

    while running:
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
                    running = False
                    iniciar_jogo()
                elif botao_creditos.clicado(event.pos):
                    print("Desenvolvido pela ExoTeam")
                elif botao_sair.clicado(event.pos):
                    running = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    mostrar_menu()
