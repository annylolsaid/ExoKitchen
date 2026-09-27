import pygame
import sys

from personagens import Hoshigo, Carlo
from mapa import Mapa
from inimigos import AlienCalmo
from pedidos import Pedido
from cozinha import Cozinha
from hud import HUD


def main():
    pygame.init()
    pygame.font.init()

    LARGURA, ALTURA = 800, 500
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Exo Kitchen - Hoshigo & Carlo")

    relogio = pygame.time.Clock()
    FPS = 60
    fonte = pygame.font.SysFont("arial", 16, bold=True)

    # Instanciando o Mapa, Cozinha, HUD e Alien
    mapa = Mapa()
    cozinha = Cozinha()
    hud = HUD()
    alien = AlienCalmo("Zorblax", 700, 90)

    # Instanciando os Protagonistas
    hoshigo = Hoshigo(x=150, y=250)
    carlo = Carlo(x=220, y=250)
    jogadores = [hoshigo, carlo]

    # Pedidos ativos
    pedidos_ativos = [Pedido(), Pedido()]
    for p in pedidos_ativos:
        p.gerar_pedido()

    tempo = 300
    mensagem = ""

    # Controle de acionamento único de teclas (debouncing)
    teclas_anteriores = {}

    rodando = True
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()

        # 1. Movimentação dos dois jogadores
        hoshigo.mover()
        carlo.mover()

        # Opcional: Colisão com obstáculos do mapa (se o mapa possuir essa função)
        if hasattr(mapa, "colisao"):
            mapa.colisao(hoshigo)
            mapa.colisao(carlo)

        # 2. Atualizar Alien e Tempo
        if hasattr(alien, "atualizar"):
            alien.atualizar()

        tempo -= 5 / FPS
        if tempo < 0:
            tempo = 0

        mensagem = ""

        # Mapeamento dos ingredientes do mapa
        ingredientes = [
            ("Tomate", getattr(mapa, "tomate", None)),
            ("Queijo", getattr(mapa, "queijo", None)),
            ("Carne", getattr(mapa, "carne", None)),
            ("Pão", getattr(mapa, "pao", None)),
            ("Massa", getattr(mapa, "massa", None))
        ]

        # 3. Interação de Pegar Ingredientes
        for jog in jogadores:
            tecla_pegar = jog.controles["pegar"]
            pegar_pressionado = teclas[tecla_pegar] and not teclas_anteriores.get(tecla_pegar, False)

            for nome, obj in ingredientes:
                if obj and jog.rect.colliderect(obj):
                    nome_tecla = pygame.key.name(tecla_pegar).upper()
                    mensagem = f"{jog.nome}: Aperte [{nome_tecla}] para pegar {nome}"

                    if pegar_pressionado:
                        cozinha.adicionar_ingrediente(nome)

        # 4. Interação de Entregar Prato ao Alien
        for jog in jogadores:
            tecla_entregar = jog.controles["entregar"]
            entregar_pressionado = teclas[tecla_entregar] and not teclas_anteriores.get(tecla_entregar, False)

            if jog.rect.colliderect(alien.rect):
                nome_tecla = pygame.key.name(tecla_entregar).upper()
                mensagem = f"{jog.nome}: Aperte [{nome_tecla}] para entregar o prato"

                if entregar_pressionado:
                    prato = cozinha.entregar()
                    pedido_concluido = None

                    for p in pedidos_ativos:
                        if p.verificar(prato):
                            pedido_concluido = p
                            break

                    if pedido_concluido:
                        jog.pontos += 20
                        if hasattr(alien, "reagir"):
                            alien.reagir()
                        pedido_concluido.novo_pedido()
                    else:
                        jog.vidas -= 1

        # Guardar estado atual das teclas para controlar o aperto único
        for jog in jogadores:
            teclas_anteriores[jog.controles["pegar"]] = teclas[jog.controles["pegar"]]
            teclas_anteriores[jog.controles["entregar"]] = teclas[jog.controles["entregar"]]

        # 5. Desenhar Tela
        mapa.desenhar(tela)
        if hasattr(alien, "desenhar"):
            alien.desenhar(tela)

        # Desenha Hoshigo e Carlo
        hoshigo.desenhar(tela, fonte)
        carlo.desenhar(tela, fonte)

        # HUD (Mostra a pontuação de Hoshigo/Carlo e receitas)
        hud.desenhar(
            tela,
            hoshigo,
            alien,
            pedidos_ativos,
            tempo,
            cozinha
        )

        # Exibir Mensagens de Ajuda na Parte Inferior
        if mensagem != "":
            pygame.draw.rect(tela, (0, 0, 0), (180, 460, 440, 30), border_radius=5)
            txt_surface = fonte.render(mensagem, True, (255, 255, 255))
            tela.blit(txt_surface, (190, 465))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()