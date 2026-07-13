import pygame
import random

from inimigos import Alien


class BossKaublorg(Alien):

    def __init__(self, x, y):

        super().__init__(
            nome="General Kaublorg",
            paciencia=200,
            x=x,
            y=y,
            cor=(180, 30, 30)
        )

        self.velocidade = 1

        self.raiva = 0

        self.vida = 100

        self.pedidos_concluidos = 0

        self.pedidos_necessarios = 5

        self.pratos = [

            "Hambúrguer Galáctico",

            "Pizza Cósmica",

            "Mega Burger Alien",

            "Sanduíche Lunar"

        ]

        self.pedido = self.novo_pedido()

    # =====================================

    def novo_pedido(self):

        return random.choice(self.pratos)

    # =====================================

    def esperar(self):

        if self.chegou_balcao:

            self.paciencia -= 0.15

            self.raiva += 0.08

            if self.paciencia < 0:
                self.paciencia = 0

            if self.raiva > 100:
                self.raiva = 100

    # =====================================

    def receber_pedido(self, correto):

        if correto:

            print("Kaublorg aprovou o prato!")

            self.pedidos_concluidos += 1

            self.raiva -= 20

            if self.raiva < 0:
                self.raiva = 0

            if self.pedidos_concluidos >= self.pedidos_necessarios:

                self.vencer()

            else:

                self.pedido = self.novo_pedido()

            return 40

        else:

            print("Kaublorg odiou o prato!")

            self.raiva += 25

            self.vida -= 10

            if self.raiva > 100:
                self.raiva = 100

            if self.vida <= 0:

                self.derrota()

            return -20

    # =====================================

    def ataque_especial(self):

        print("KAUBLORG UTILIZOU A AMEAÇA INTERGALÁCTICA!")

    # =====================================

    def atualizar(self):

        self.mover()

        self.esperar()

        if self.raiva >= 70:

            self.ataque_especial()

    # =====================================

    def desenhar(self, tela):

        super().desenhar(tela)

        fonte = pygame.font.SysFont("Arial", 18, True)

        texto = fonte.render(
            "GENERAL KAUBLORG",
            True,
            (255,255,255)
        )

        tela.blit(texto, (560,10))

        pygame.draw.rect(
            tela,
            (90,90,90),
            (560,35,200,18)
        )

        pygame.draw.rect(
            tela,
            (255,0,0),
            (
                560,
                35,
                200*(self.raiva/100),
                18
            )
        )

    # =====================================

    def vencer(self):

        print()

        print("===================================")
        print("GENERAL KAUBLORG FOI SATISFEITO!")
        print("A HUMANIDADE ESTÁ SALVA!")
        print("===================================")

    # =====================================

    def derrota(self):

        print()

        print("===================================")
        print("KAUBLORG ANIQUILOU A HUMANIDADE!")
        print("GAME OVER")
        print("===================================")