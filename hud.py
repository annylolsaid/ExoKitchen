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
        pedidos,  # Alterado para aceitar a lista de pedidos
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
                (260, 40)
            )



        # ==================================================
        # PEDIDOS (SUPORTA MÚLTIPLOS PEDIDOS)
        # ==================================================

        # Caixinha cinza para abrigar os pedidos
        pygame.draw.rect(
            tela,
            (60, 60, 60),
            (450, 10, 335, 75)
        )

        # Garante tratamento correto se for lista ou pedido único
        lista_pedidos = pedidos if isinstance(pedidos, list) else [pedidos]

        y_pos = 15

        for i, p in enumerate(lista_pedidos):

            if hasattr(p, "prato_atual") and p.prato_atual:

                nome_prato = p.prato_atual["nome"]
                ingredientes_str = ", ".join(p.prato_atual["ingredientes"])

                texto_pedido = self.fonte.render(
                    f"P{i+1}: {nome_prato} ({ingredientes_str})",
                    True,
                    self.AMARELO if i == 0 else self.BRANCO
                )

                tela.blit(
                    texto_pedido,
                    (455, y_pos)
                )

                y_pos += 30



        # ==================================================
        # PRATO DO JOGADOR
        # ==================================================

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