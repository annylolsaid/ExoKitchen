import pygame


class Mapa:

    def __init__(self):

        # ==========================
        # TAMANHO DA TELA
        # ==========================

        self.largura = 800
        self.altura = 500


        # ==========================
        # CORES
        # ==========================

        self.COR_FUNDO = (215, 215, 215)
        self.COR_BALCAO = (120, 80, 45)
        self.COR_PAREDE = (70, 70, 70)



        # ==========================
        # BALCÃO
        # ==========================

        self.balcao = pygame.Rect(
            0,
            80,
            800,
            60
        )



        # ==========================
        # PAREDES
        # ==========================

        self.parede_esquerda = pygame.Rect(
            0,
            0,
            10,
            500
        )


        self.parede_direita = pygame.Rect(
            790,
            0,
            10,
            500
        )


        self.parede_superior = pygame.Rect(
            0,
            0,
            800,
            10
        )


        self.parede_inferior = pygame.Rect(
            0,
            490,
            800,
            10
        )



        # ==========================
        # INGREDIENTES
        # ==========================

        # Mantidos no lado esquerdo
        # para não bater com o HUD do prato

        self.tomate = pygame.Rect(
            70,
            400,
            30,
            30
        )


        self.queijo = pygame.Rect(
            170,
            400,
            30,
            30
        )


        self.carne = pygame.Rect(
            270,
            400,
            30,
            30
        )


        self.pao = pygame.Rect(
            370,
            400,
            30,
            30
        )


        self.massa = pygame.Rect(
            470,
            400,
            30,
            30
        )



        self.ingredientes = {

            "Tomate": self.tomate,

            "Queijo": self.queijo,

            "Carne": self.carne,

            "Pão": self.pao,

            "Massa": self.massa

        }



    # =====================================================
    # DESENHAR MAPA
    # =====================================================

    def desenhar(self, tela):


        tela.fill(
            self.COR_FUNDO
        )



        # ==========================
        # BALCÃO
        # ==========================

        pygame.draw.rect(
            tela,
            self.COR_BALCAO,
            self.balcao
        )



        # ==========================
        # PAREDES
        # ==========================

        pygame.draw.rect(
            tela,
            self.COR_PAREDE,
            self.parede_esquerda
        )


        pygame.draw.rect(
            tela,
            self.COR_PAREDE,
            self.parede_direita
        )


        pygame.draw.rect(
            tela,
            self.COR_PAREDE,
            self.parede_superior
        )


        pygame.draw.rect(
            tela,
            self.COR_PAREDE,
            self.parede_inferior
        )



        # ==========================
        # INGREDIENTES
        # ==========================

        pygame.draw.rect(
            tela,
            (255,0,0),
            self.tomate
        )


        pygame.draw.rect(
            tela,
            (255,255,0),
            self.queijo
        )


        pygame.draw.rect(
            tela,
            (120,70,30),
            self.carne
        )


        pygame.draw.rect(
            tela,
            (255,220,120),
            self.pao
        )


        pygame.draw.rect(
            tela,
            (240,240,240),
            self.massa
        )



        # ==========================
        # NOMES
        # ==========================

        fonte = pygame.font.SysFont(
            "Arial",
            14
        )


        tela.blit(
            fonte.render(
                "Tomate",
                True,
                (0,0,0)
            ),
            (60,440)
        )


        tela.blit(
            fonte.render(
                "Queijo",
                True,
                (0,0,0)
            ),
            (160,440)
        )


        tela.blit(
            fonte.render(
                "Carne",
                True,
                (0,0,0)
            ),
            (260,440)
        )


        tela.blit(
            fonte.render(
                "Pao",
                True,
                (0,0,0)
            ),
            (375,440)
        )


        tela.blit(
            fonte.render(
                "Massa",
                True,
                (0,0,0)
            ),
            (460,440)
        )



    # =====================================================
    # COLISÕES
    # =====================================================

    def colisao(self, jogador):


        if jogador.rect.colliderect(
            self.balcao
        ):

            jogador.rect.top = (
                self.balcao.bottom
            )



        if jogador.rect.left < 10:

            jogador.rect.left = 10



        if jogador.rect.right > 790:

            jogador.rect.right = 790



        if jogador.rect.top < 10:

            jogador.rect.top = 10



        if jogador.rect.bottom > 490:

            jogador.rect.bottom = 490



    # =====================================================
    # MENSAGEM
    # =====================================================

    def desenhar_texto(
        self,
        tela,
        texto
    ):


        fonte = pygame.font.SysFont(
            "Arial",
            20
        )


        pygame.draw.rect(
            tela,
            (0,0,0),
            (190,450,420,35)
        )


        render = fonte.render(
            texto,
            True,
            (255,255,255)
        )


        tela.blit(
            render,
            (205,457)
        )