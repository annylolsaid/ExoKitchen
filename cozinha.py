class Cozinha:

    def __init__(self):

        # Ingredientes disponíveis
        self.ingredientes_disponiveis = [
            "Pão",
            "Carne",
            "Queijo",
            "Tomate",
            "Massa"
        ]

        # Ingredientes do prato atual
        self.prato = []

    # ------------------------------------

    def adicionar_ingrediente(self, ingrediente):

        if ingrediente in self.ingredientes_disponiveis:

            self.prato.append(ingrediente)

            print(f"{ingrediente} adicionado ao prato.")

        else:

            print("Ingrediente inválido.")

    # ------------------------------------

    def remover_ingrediente(self, ingrediente):

        if ingrediente in self.prato:

            self.prato.remove(ingrediente)

            print(f"{ingrediente} removido.")

    # ------------------------------------

    def limpar_prato(self):

        self.prato.clear()

        print("Prato limpo.")

    # ------------------------------------

    def mostrar_prato(self):

        return self.prato

    # ------------------------------------
    def entregar(self):

        prato = self.prato.copy()

        self.prato.clear()

        return prato