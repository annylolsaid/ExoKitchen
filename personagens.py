import os
import pygame


class Protagonistas:
    def __init__(self, nome, id, x, y, cor=(0, 150, 255), controles=None):
        self.nome = nome
        self.id = id

       
        self.largura = 40
        self.altura = 50
        self.rect = pygame.Rect(x, y, self.largura, self.altura)

        self.cor = cor

       
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

        # Sprites
        self.sprites = None
        self.direcao = "frente"
        self.andando = False
        self.com_prato = False
        self.tempo_animacao = 0

    def mover(self):
        teclas = pygame.key.get_pressed()

        antes = self.rect.topleft

        if teclas[self.controles["esquerda"]]:
            self.rect.x -= self.velocidade
        if teclas[self.controles["direita"]]:
            self.rect.x += self.velocidade
        if teclas[self.controles["cima"]]:
            self.rect.y -= self.velocidade
        if teclas[self.controles["baixo"]]:
            self.rect.y += self.velocidade

        self.colisao()


        if teclas[self.controles["esquerda"]] != teclas[self.controles["direita"]]:
            self.direcao = "esquerda" if teclas[self.controles["esquerda"]] else "direita"
        elif teclas[self.controles["cima"]] != teclas[self.controles["baixo"]]:
            self.direcao = "costas" if teclas[self.controles["cima"]] else "frente"

        self.andando = self.rect.topleft != antes

    def colisao(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 500:
            self.rect.bottom = 500

    def adicionar_pontos(self, pontos):
        self.pontos += pontos

    def perder_vida(self):
        if self.vidas > 0:
            self.vidas -= 1

    ALTURA_SPRITE = 100 

    def carregar_sprites(self, pasta, prefixo):

        base = os.path.dirname(os.path.abspath(__file__))
        pasta = os.path.join(base, pasta)
        imagens = {}
        for dir_ in ("frente", "costas", "esquerda", "direita"):
            for andando in (False, True):
                for prato in (False, True):
                    nome = prefixo + "_" + dir_
                    if andando:
                        nome += "_andando"
                    if prato:
                        nome += "_prato"
                    caminho = os.path.join(pasta, nome + ".png")
                    if os.path.exists(caminho):
                        imagens[(dir_, andando, prato)] = pygame.image.load(caminho).convert_alpha()


        ref = imagens[("frente", False, False)]
        escala = self.ALTURA_SPRITE / ref.get_height()
        self.sprites = {}
        for chave, img in imagens.items():
            tam = (round(img.get_width() * escala), round(img.get_height() * escala))
            self.sprites[chave] = pygame.transform.smoothscale(img, tam)

    def sprite_atual(self):
        andando = self.andando
        if andando:
            # alterna entre o sprite parado e o andando (~6 trocas/s)
            self.tempo_animacao += 1
            andando = (self.tempo_animacao // 10) % 2 == 0
        else:
            self.tempo_animacao = 0

        # Tenta o sprite exato; se não existir (ex.: costas parado com prato),
        # cai para a versão sem prato / parada.
        for chave in (
            (self.direcao, andando, self.com_prato),
            (self.direcao, andando, False),
            (self.direcao, False, False),
        ):
            if chave in self.sprites:
                return self.sprites[chave]

    def desenhar(self, tela, fonte):
        # Desenha o personagem
        if self.sprites:
            img = self.sprite_atual()

            tela.blit(img, img.get_rect(midbottom=self.rect.midbottom))
        else:
            pygame.draw.rect(tela, self.cor, self.rect, border_radius=8)

        # Desenha o nome em cima
        texto = fonte.render(self.nome, True, (255, 255, 255))
        pos_x = self.rect.x + (self.largura // 2) - (texto.get_width() // 2)
        pos_y = self.rect.bottom - (self.ALTURA_SPRITE if self.sprites else self.altura) - 20
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
                "pegar": pygame.K_e,      
                "entregar": pygame.K_f   
            }
        )
        self.carregar_sprites(os.path.join("Sprites", "hoshigo"), "hoshigo")


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
                "pegar": pygame.K_k,     
                "entregar": pygame.K_l   
            }
        )