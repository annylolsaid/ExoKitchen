import pygame
import random


class HUD:

    def __init__(self):

        self.fonte = pygame.font.SysFont("arial", 24)

        self.pontos = 0

        self.vidas = 3

        self.tempo = 300

    def adicionar_pontos(self, valor):

        self.pontos += valor

    def remover_vida(self):

        if self.vidas > 0:

            self.vidas -= 1

    def atualizar(self):

        if self.tempo > 0:

            self.tempo -= 0.02

    def desenhar(self, tela):

        texto1 = self.fonte.render(
            f"Pontos: {self.pontos}",
            True,
            (255,255,255)
        )

        texto2 = self.fonte.render(
            f"Vidas: {self.vidas}",
            True,
            (255,255,255)
        )

        texto3 = self.fonte.render(
            f"Tempo: {int(self.tempo)}",
            True,
            (255,255,255)
        )

        tela.blit(texto1,(20,15))
        tela.blit(texto2,(20,45))
        tela.blit(texto3,(20,75))

class Ingrediente:

    def __init__(self,nome):

        self.nome = nome

        self.quantidade = 10

    def usar(self):

        if self.quantidade > 0:

            self.quantidade -= 1

            return True

        return False

    def reabastecer(self):

        self.quantidade = 10

class Pedido:

    pratos = [

        "Hambúrguer Galáctico",

        "Pizza Cósmica",

        "Sopa Lunar",

        "Sanduíche Estelar",

        "Macarrão Nebuloso"

    ]

    def __init__(self):

        self.prato = random.choice(self.pratos)

        self.concluido = False

    def finalizar(self):

        self.concluido = True


class TradutorUniversal:

    traducoes = {

        "Grak": "Hambúrguer Galáctico",

        "Zork": "Pizza Cósmica",

        "Blorg": "Sopa Lunar",

        "Nek": "Sanduíche Estelar",

        "Krol": "Macarrão Nebuloso"

    }

    def traduzir(self,palavra):

        if palavra in self.traducoes:

            return self.traducoes[palavra]

        return "Palavra desconhecida"
    
class TradutorUniversal:

    traducoes = {

        "Grak": "Hambúrguer Galáctico",

        "Zork": "Pizza Cósmica",

        "Blorg": "Sopa Lunar",

        "Nek": "Sanduíche Estelar",

        "Krol": "Macarrão Nebuloso"

    }

    def traduzir(self,palavra):

        if palavra in self.traducoes:

            return self.traducoes[palavra]

        return "Palavra desconhecida"

class Cronometro:

    def __init__(self,tempo=300):

        self.tempo = tempo

    def atualizar(self):

        if self.tempo > 0:

            self.tempo -= 0.02

    def acabou(self):

        return self.tempo <= 0