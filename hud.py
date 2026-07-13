import pygame


class HUD:

    def __init__(self):

        self.fonte = pygame.font.SysFont(
            "Arial",
            20
        )

        self.titulo = pygame.font.SysFont(
            "Arial",
            24,
            bold=True
        )

        self.BRANCO = (255, 255, 255)
        self.PRETO = (0, 0, 0)
        self.CINZA = (40, 40, 40)
        self.AZUL = (80, 170, 255)
        self.VERDE = (0, 220, 0)
        self.AMARELO = (255, 255, 0)



    # ======================================================
    # DESENHAR HUD
    # ======================================================

    def desenhar(
        self,
        tela,
        jogador,
        alien,
        pedido,
        tempo,
        cozinha
    ):


        # ==================================================
        # PAINEL SUPERIOR
        # ==================================================

        pygame.draw.rect(
            tela,
            self.CINZA,
            (0, 0, 800, 90)
        )



        # ==================================================
        # VIDAS
        # ==================================================

        vidas = self.fonte.render(
            f"❤️ Vidas: {jogador.vidas}",
            True,
            self.BRANCO
        )

        tela.blit(
            vidas,
            (15, 10)
        )



        # ==================================================
        # PONTOS
        # ==================================================

        pontos = self.fonte.render(
            f"⭐ Pontos: {jogador.pontos}",
            True,
            self.BRANCO
        )

        tela.blit(
            pontos,
            (15, 40)
        )



        # ==================================================
        # TEMPO
        # ==================================================

        txt_tempo = self.fonte.render(
            f"⏱ Tempo: {int(tempo)}",
            True,
            self.BRANCO
        )

        tela.blit(
            txt_tempo,
            (260, 10)
        )



        # ==================================================
        # CLIENTE
        # ==================================================

        if alien:

            cliente = self.fonte.render(
                f"👽 Cliente: {alien.nome}",
                True,
                self.VERDE
            )

            tela.blit(
                cliente,
                (500, 10)
            )



        # ==================================================
        # PEDIDO
        # ==================================================

        pygame.draw.rect(
            tela,
            (60, 60, 60),
            (500, 35, 280, 55)
        )


        titulo = self.fonte.render(
            "Pedido:",
            True,
            self.AMARELO
        )


        tela.blit(
            titulo,
            (510, 40)
        )



        if pedido.prato_atual:


            nome = self.fonte.render(
                pedido.prato_atual["nome"],
                True,
                self.BRANCO
            )


            tela.blit(
                nome,
                (580, 40)
            )



            ingredientes = self.fonte.render(
                ", ".join(
                    pedido.prato_atual["ingredientes"]
                ),
                True,
                self.AMARELO
            )


            tela.blit(
                ingredientes,
                (510, 65)
            )



        # ==================================================
        # PRATO DO JOGADOR
        # ==================================================

        # Agora fica no canto inferior direito
        # para não cobrir os ingredientes

        pygame.draw.rect(
            tela,
            (25, 25, 25),
            (520, 410, 270, 80)
        )



        titulo_prato = self.fonte.render(
            "Prato:",
            True,
            self.AZUL
        )


        tela.blit(
            titulo_prato,
            (530, 418)
        )



        ingredientes_jogador = cozinha.mostrar_prato()



        if len(ingredientes_jogador) == 0:


            vazio = self.fonte.render(
                "(vazio)",
                True,
                self.BRANCO
            )


            tela.blit(
                vazio,
                (600, 418)
            )



        else:


            texto = ", ".join(
                ingredientes_jogador
            )



            if len(texto) > 18:


                primeira_linha = texto[:18]

                segunda_linha = texto[18:]



                linha1 = self.fonte.render(
                    primeira_linha,
                    True,
                    self.BRANCO
                )


                linha2 = self.fonte.render(
                    segunda_linha,
                    True,
                    self.BRANCO
                )



                tela.blit(
                    linha1,
                    (600, 418)
                )


                tela.blit(
                    linha2,
                    (600, 440)
                )



            else:


                prato = self.fonte.render(
                    texto,
                    True,
                    self.BRANCO
                )


                tela.blit(
                    prato,
                    (600, 418)
                )