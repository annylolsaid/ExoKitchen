import pygame


class Protagonistas:
    def __init__(self, nome, id, x, y, cor=(0, 150, 255)):
        self.nome = nome
        self.id = id

        # Posição
        self.x = x
        self.y = y

        # Tamanho
        self.largura = 50
        self.altura = 70

        # Retângulo do personagem
        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.largura,
            self.altura
        )

        # Aparência temporária
        self.cor = cor

        # Atributos
        self.velocidade = 5
        self.vidas = 3
        self.pontos = 0

        # Ingredientes
        self.tomates = 10
        self.queijos = 10
        self.carnes = 10
        self.paes = 10

    # ------------------------
    # MOVIMENTAÇÃO
    # ------------------------

    def mover(self):

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade

        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.rect.y -= self.velocidade

        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidade

        self.colisao()

    def colisao(self):

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > 800:
            self.rect.right = 800

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > 500:
            self.rect.bottom = 500

    # ------------------------
    # DESENHO
    # ------------------------

    def desenhar(self, tela):

        pygame.draw.rect(
            tela,
            self.cor,
            self.rect,
            border_radius=8
        )

    # ------------------------
    # PONTUAÇÃO
    # ------------------------

    def adicionar_pontos(self, quantidade):

        self.pontos += quantidade

    def perder_pontos(self, quantidade):

        self.pontos -= quantidade

        if self.pontos < 0:
            self.pontos = 0

    # ------------------------
    # VIDAS
    # ------------------------

    def perder_vida(self):

        if self.vidas > 0:
            self.vidas -= 1

    def ganhar_vida(self):

        self.vidas += 1

    # ------------------------
    # INGREDIENTES
    # ------------------------

    def pegar_tomate(self):

        if self.tomates > 0:
            self.tomates -= 1
            return True

        return False

    def pegar_queijo(self):

        if self.queijos > 0:
            self.queijos -= 1
            return True

        return False

    def pegar_carne(self):

        if self.carnes > 0:
            self.carnes -= 1
            return True

        return False

    def pegar_pao(self):

        if self.paes > 0:
            self.paes -= 1
            return True

        return False

    # ------------------------
    # STATUS
    # ------------------------

    def mostrar_status(self):

        print("========== STATUS ==========")
        print(f"Nome: {self.nome}")
        print(f"Pontos: {self.pontos}")
        print(f"Vidas: {self.vidas}")
        print(f"Tomates: {self.tomates}")
        print(f"Queijos: {self.queijos}")
        print(f"Carnes: {self.carnes}")
        print(f"Pães: {self.paes}")
        print("============================")


# ==========================================
# HOSHIGO
# ==========================================

class Hoshigo(Protagonistas):

    def __init__(self, x, y):

        super().__init__(
            nome="Hoshigo",
            id=1,
            x=x,
            y=y,
            cor=(60, 170, 255)
        )

    def cozinhar(self):

        print(f"{self.nome} começou a cozinhar.")

    def entregar_pedido(self):

        print(f"{self.nome} entregou o pedido.")

    def falar(self):

        print("Vamos salvar a humanidade!")


# ==========================================
# CARLO
# ==========================================

class Carlo(Protagonistas):

    def __init__(self, x, y):

        super().__init__(
            nome="Carlo",
            id=2,
            x=x,
            y=y,
            cor=(255, 170, 50)
        )

    def cozinhar(self):

        print(f"{self.nome} está preparando um prato.")

    def entregar_pedido(self):

        print(f"{self.nome} entregou o pedido.")

    def falar(self):

        print("Hora de trabalhar!")