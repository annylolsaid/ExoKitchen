import random


class Pedido:

    def __init__(self):

        # Lista de pratos disponíveis

        self.pratos = [

            {
                "nome": "Hambúrguer Galáctico",
                "ingredientes": [
                    "Pão",
                    "Carne",
                    "Queijo"
                ]
            },


            {
                "nome": "Pizza Cósmica",
                "ingredientes": [
                    "Massa",
                    "Queijo",
                    "Tomate"
                ]
            },


            {
                "nome": "Sanduíche Lunar",
                "ingredientes": [
                    "Pão",
                    "Tomate",
                    "Queijo"
                ]
            },


            {
                "nome": "Mega Burger Alien",
                "ingredientes": [
                    "Pão",
                    "Carne",
                    "Tomate",
                    "Queijo"
                ]
            }

        ]


        # Pedido que está ativo no momento

        self.prato_atual = None



    # ==================================================
    # GERAR PEDIDO
    # ==================================================

    def gerar_pedido(self):

        self.prato_atual = random.choice(
            self.pratos
        )

        print(
            f"Novo pedido: {self.prato_atual['nome']}"
        )



    # ==================================================
    # VERIFICAR PEDIDO
    # ==================================================

    def verificar(self, prato):

        # Caso não exista pedido

        if self.prato_atual is None:

            return False


        ingredientes_pedido = sorted(
            self.prato_atual["ingredientes"]
        )


        ingredientes_entregues = sorted(
            prato
        )


        return ingredientes_pedido == ingredientes_entregues



    # ==================================================
    # PEGAR INGREDIENTES DO PEDIDO
    # ==================================================

    def mostrar_ingredientes(self):

        if self.prato_atual:

            return self.prato_atual["ingredientes"]

        return []



    # ==================================================
    # PEGAR NOME DO PRATO
    # ==================================================

    def mostrar_nome(self):

        if self.prato_atual:

            return self.prato_atual["nome"]

        return "Nenhum pedido"



    # ==================================================
    # NOVO PEDIDO
    # ==================================================

    def novo_pedido(self):

        self.gerar_pedido()