import pygame


# ==================================================
# CLASSE abstrata
# ==================================================

class Alien:


    def __init__(
        self,
        nome,
        paciencia,
        x,
        y,
        cor=(0, 255, 0)
    ):

        self.nome = nome

        self.paciencia = paciencia

        self.satisfacao = 100


        # Aparência

        self.cor = cor


        # Posição

        self.rect = pygame.Rect(
            x,
            y,
            50,
            70
        )


        # Movimento

        self.velocidade = 2


        # Estado

        self.chegou_balcao = False


        # Mensagem de interação

        self.mensagem = ""



    # ==================================================
    # MOVIMENTO
    # ==================================================

    def mover(self):

        # Caminha até o balcão

        if self.rect.x > 620:

            self.rect.x -= self.velocidade


        else:

            self.chegou_balcao = True



    # ==================================================
    # PACIÊNCIA
    # ==================================================

    def esperar(self):

        if self.chegou_balcao:

            self.paciencia -= 0.03


            if self.paciencia < 0:

                self.paciencia = 0



    # ==================================================
    # ATUALIZAÇÃO
    # ==================================================

    def atualizar(self):

        self.mover()


        if self.chegou_balcao:

            self.esperar()



    # ==================================================
    # DESENHO
    # ==================================================

    def desenhar(self, tela):

        pygame.draw.rect(
            tela,
            self.cor,
            self.rect,
            border_radius=8
        )


        self.desenhar_barra_paciencia(
            tela
        )



    # ==================================================
    # BARRA DE PACIÊNCIA
    # ==================================================

    def desenhar_barra_paciencia(self, tela):

        largura = 50

        altura = 6


        porcentagem = self.paciencia / 100


        if porcentagem < 0:

            porcentagem = 0



        # Fundo da barra

        pygame.draw.rect(
            tela,
            (180,180,180),
            (
                self.rect.x,
                self.rect.y - 12,
                largura,
                altura
            )
        )



        # Barra atual

        pygame.draw.rect(
            tela,
            (0,255,0),
            (
                self.rect.x,
                self.rect.y - 12,
                largura * porcentagem,
                altura
            )
        )



    # ==================================================
    # AÇÕES
    # ==================================================

    def fazer_pedido(self):

        print(
            f"{self.nome} fez um pedido alienígena!"
        )



    def reagir(self):

        self.mensagem = (
            "Cliente recebeu o prato!"
        )


        print(
            f"{self.nome} recebeu o prato!"
        )



# ==================================================
# ALIEN CALMO
# ==================================================

class AlienCalmo(Alien):


    def __init__(
        self,
        nome,
        x,
        y
    ):

        super().__init__(
            nome,
            paciencia=100,
            x=x,
            y=y,
            cor=(50,220,50)
        )



    def reagir(self):

        self.mensagem = (
            "Pedido aprovado! Cliente satisfeito."
        )


        print(
            f"{self.nome} ficou feliz e esperou com calma."
        )



# ==================================================
# ALIEN IMPACIENTE
# ==================================================

class AlienImpaciente(Alien):


    def __init__(
        self,
        nome,
        x,
        y
    ):

        super().__init__(
            nome,
            paciencia=60,
            x=x,
            y=y,
            cor=(255,80,80)
        )


        self.velocidade = 3



    def esperar(self):

        if self.chegou_balcao:

            self.paciencia -= 0.08


            if self.paciencia < 0:

                self.paciencia = 0



    def reagir(self):

        self.mensagem = (
            "O alien reclamou da demora!"
        )


        print(
            f"{self.nome} reclamou da demora!"
        )



# ==================================================
# ALIEN EXIGENTE
# ==================================================

class AlienExigente(Alien):


    def __init__(
        self,
        nome,
        x,
        y
    ):

        super().__init__(
            nome,
            paciencia=80,
            x=x,
            y=y,
            cor=(120,120,255)
        )



    def reagir(self):

        self.mensagem = (
            "Pedido analisado cuidadosamente."
        )


        print(
            f"{self.nome} analisou cuidadosamente a comida."
        )

        print(
            "Qualquer erro fará ele perder pontos."
        )