import os
import sys
import pygame
import math


# ==========================================
# IMPORTAR MAIN (pasta acima)
# ==========================================

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

import main



# ==========================================
# INICIALIZAÇÃO
# ==========================================

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


display = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption(
    "ExoKitchen"
)



# ==========================================
# CAMINHO DOS ARQUIVOS
# ==========================================

BASE_PATH = os.path.dirname(
    os.path.abspath(__file__)
)



# ==========================================
# IMAGENS
# ==========================================

TITLE_PATH = os.path.join(
    BASE_PATH,
    "titulo.png"
)


BG_PATH = os.path.join(
    BASE_PATH,
    "background.png"
)



titulo_img = pygame.image.load(
    TITLE_PATH
).convert_alpha()


titulo_img = pygame.transform.scale(
    titulo_img,
    (540,455)
)


titulo_rect = titulo_img.get_rect(
    center=(
        SCREEN_WIDTH // 2,
        180
    )
)



# ==========================================
# FUNDO ANIMADO
# ==========================================

class Fundo:


    def __init__(self, bg_path):

        self.bg = pygame.image.load(
            bg_path
        ).convert_alpha()


        self.img_x = self.bg.get_width()


        self.tiles = math.ceil(
            SCREEN_WIDTH / self.img_x
        ) + 1


        self.scroll = 0



    def atualizar(self):

        self.scroll -= 0.5


        if self.scroll <= -self.img_x:

            self.scroll = 0



    def desenhar(self, superficie):

        for i in range(self.tiles):

            superficie.blit(
                self.bg,
                (
                    i * self.img_x + self.scroll,
                    0
                )
            )




# ==========================================
# BOTÕES
# ==========================================

class Botao:


    def __init__(
        self,
        x,
        y,
        largura,
        altura,
        sprite_path
    ):

        self.rect = pygame.Rect(
            x,
            y,
            largura,
            altura
        )


        self.sprite = pygame.image.load(
            sprite_path
        ).convert_alpha()


        self.sprite = pygame.transform.scale(
            self.sprite,
            (
                largura,
                altura
            )
        )



    def desenhar(self, superficie):

        superficie.blit(
            self.sprite,
            self.rect
        )



    def clicado(self,pos):

        return self.rect.collidepoint(
            pos
        )




# ==========================================
# OBJETOS
# ==========================================

fundo = Fundo(
    BG_PATH
)



botao_jogar = Botao(
    300,
    250,
    200,
    75,
    os.path.join(
        BASE_PATH,
        "botão_jogar.png"
    )
)



botao_creditos = Botao(
    300,
    335,
    200,
    75,
    os.path.join(
        BASE_PATH,
        "botão_créditos.png"
    )
)



botao_sair = Botao(
    300,
    420,
    200,
    75,
    os.path.join(
        BASE_PATH,
        "botão_sair.png"
    )
)




# ==========================================
# MENU
# ==========================================

running = True



while running:


    fundo.atualizar()


    fundo.desenhar(
        display
    )


    display.blit(
        titulo_img,
        titulo_rect
    )


    botao_jogar.desenhar(
        display
    )


    botao_creditos.desenhar(
        display
    )


    botao_sair.desenhar(
        display
    )



    for event in pygame.event.get():


        if event.type == pygame.QUIT:

            running = False



        if event.type == pygame.MOUSEBUTTONDOWN:


            if botao_jogar.clicado(
                event.pos
            ):


                running = False


                main.iniciar_jogo()



            elif botao_creditos.clicado(
                event.pos
            ):


                print(
                    "Desenvolvido pela ExoTeam"
                )



            elif botao_sair.clicado(
                event.pos
            ):


                running = False




    pygame.display.update()



pygame.quit()