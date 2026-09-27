import pygame

# classe abstrata 
class Protagonistas:
    def __init__(self, nome, id, x, y, cor=(0, 150, 255), controles=None):
        self.nome = nome
        self.id = id

        # Posição e tamanho
        self.largura = 40
        self.altura = 50
        self.rect = pygame.Rect(x, y, self.largura, self.altura)

        self.cor = cor

        # Teclas de movimentação e ação padrão
        self.controles = controles or {
            "cima": pygame.K_UP,
            "baixo": pygame.K_DOWN,
            "esquerda": pygame.K_LEFT,
            "direita": pygame.K_RIGHT,
            "pegar": pygame.K_k,
            "entregar": pygame.K_l
        }

        self.velocidade = 5
        self.vidas = 3
        self.pontos = 0

    def mover(self):
        teclas = pygame.key.get_pressed()

        if teclas[self.controles["esquerda"]]:
            self.rect.x -= self.velocidade
        if teclas[self.controles["direita"]]:
            self.rect.x += self.velocidade
        if teclas[self.controles["cima"]]:
            self.rect.y -= self.velocidade
        if teclas[self.controles["baixo"]]:
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

    def desenhar(self, tela, fonte):
        # Desenha o personagem
        pygame.draw.rect(tela, self.cor, self.rect, border_radius=8)

        # Desenha o nome em cima
        texto = fonte.render(self.nome, True, (255, 255, 255))
        pos_x = self.rect.x + (self.largura // 2) - (texto.get_width() // 2)
        pos_y = self.rect.y - 20
        tela.blit(texto, (pos_x, pos_y))


class Hoshigo(Protagonistas):
    def __init__(self, x, y):
        super().__init__(
            nome="Hoshigo",
            id=1,
            x=x,
            y=y,
            cor=(60, 170, 255),
            controles={
                "cima": pygame.K_w,
                "baixo": pygame.K_s,
                "esquerda": pygame.K_a,
                "direita": pygame.K_d,
                "pegar": pygame.K_e,      # Tecla E para pegar
                "entregar": pygame.K_f   # Tecla F para entregar
            }
        )


class Carlo(Protagonistas):
    def __init__(self, x, y):
        super().__init__(
            nome="Carlo",
            id=2,
            x=x,
            y=y,
            cor=(255, 170, 50),
            controles={
                "cima": pygame.K_UP,
                "baixo": pygame.K_DOWN,
                "esquerda": pygame.K_LEFT,
                "direita": pygame.K_RIGHT,
                "pegar": pygame.K_k,      # Tecla K para pegar
                "entregar": pygame.K_l   # Tecla L para entregar
            }
        )