import pygame

from personagens import Hoshigo
from mapa import Mapa
from inimigos import AlienCalmo
from pedidos import Pedido
from cozinha import Cozinha
from hud import HUD



def iniciar_jogo():

    # ==========================================
    # INICIALIZAÇÃO
    # ==========================================

    pygame.init()


    LARGURA = 800
    ALTURA = 500


    TELA = pygame.display.set_mode(
        (LARGURA, ALTURA)
    )

    pygame.display.set_caption(
        "Exo Kitchen"
    )


    clock = pygame.time.Clock()

    FPS = 60



    # ==========================================
    # OBJETOS
    # ==========================================

    mapa = Mapa()


    jogador = Hoshigo(
        100,
        250
    )


    alien = AlienCalmo(
        "Zorblax",
        700,
        90
    )


    pedido = Pedido()

    pedido.gerar_pedido()



    cozinha = Cozinha()


    hud = HUD()



    tempo = 300


    fonte = pygame.font.SysFont(
        "Arial",
        20
    )


    mensagem = ""



    # Controle de teclas

    e_pressionado = False

    f_pressionado = False



    # ==========================================
    # LOOP DO JOGO
    # ==========================================

    rodando = True


    while rodando:


        clock.tick(FPS)



        # ======================================
        # EVENTOS
        # ======================================

        for event in pygame.event.get():


            if event.type == pygame.QUIT:

                rodando = False



        teclas = pygame.key.get_pressed()



        # ======================================
        # JOGADOR
        # ======================================

        jogador.mover()


        mapa.colisao(
            jogador
        )



        # ======================================
        # ALIEN
        # ======================================

        alien.atualizar()



        # ======================================
        # TEMPO
        # ======================================

        tempo -= 1 / FPS


        if tempo < 0:

            tempo = 0



        mensagem = ""



        # ======================================
        # PEGAR INGREDIENTES
        # ======================================


        pegar = False


        if teclas[pygame.K_e] and not e_pressionado:

            pegar = True


        e_pressionado = teclas[pygame.K_e]



        ingredientes = [

            ("Tomate", mapa.tomate),

            ("Queijo", mapa.queijo),

            ("Carne", mapa.carne),

            ("Pão", mapa.pao),

            ("Massa", mapa.massa)

        ]



        for nome, objeto in ingredientes:


            if jogador.rect.colliderect(
                objeto
            ):


                mensagem = (
                    f"Pressione E para pegar {nome}"
                )


                if pegar:

                    cozinha.adicionar_ingrediente(
                        nome
                    )



        # ======================================
        # ENTREGAR PEDIDO
        # ======================================


        entregar = False


        if teclas[pygame.K_f] and not f_pressionado:

            entregar = True


        f_pressionado = teclas[pygame.K_f]



        if jogador.rect.colliderect(
            alien.rect
        ):


            mensagem = (
                "Pressione F para entregar"
            )



            if entregar:


                prato = cozinha.entregar()



                if pedido.verificar(
                    prato
                ):


                    jogador.adicionar_pontos(
                        20
                    )


                    alien.reagir()


                    print(
                        "Pedido correto!"
                    )


                else:


                    jogador.perder_vida()


                    print(
                        "Pedido errado!"
                    )



                pedido.novo_pedido()



        # ======================================
        # DESENHO
        # ======================================

        mapa.desenhar(
            TELA
        )


        alien.desenhar(
            TELA
        )


        jogador.desenhar(
            TELA
        )



        hud.desenhar(
            TELA,
            jogador,
            alien,
            pedido,
            tempo,
            cozinha
        )



        # ======================================
        # MENSAGEM
        # ======================================

        if mensagem != "":


            pygame.draw.rect(
                TELA,
                (0,0,0),
                (200,455,400,30)
            )


            texto = fonte.render(
                mensagem,
                True,
                (255,255,255)
            )


            TELA.blit(
                texto,
                (215,460)
            )



        pygame.display.flip()



    pygame.quit()







if __name__ == "__main__":

    iniciar_jogo()