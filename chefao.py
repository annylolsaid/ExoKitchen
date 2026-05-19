class Alien:

    def __init__(self, nome, paciencia):
        self.nome = nome
        self.paciencia = paciencia
        self.satisfacao = 100

    def fazer_pedido(self):
        print(f"{self.nome} fez um pedido alienígena!")

    def esperar(self):
        self.paciencia -= 10
        print(f"Paciência restante: {self.paciencia}")

    def reagir(self):
        print(f"{self.nome} recebeu o prato.")


# CLASSE FILHA - BOSS


class BossKaublorg(Alien):

    def __init__(self, nome):
        super().__init__(nome, paciencia=200)
        self.raiva = 0

    def esperar(self):
        self.paciencia -= 20
        self.raiva += 10

        print(f"{self.nome} está ficando furioso!")
        print(f"Paciência restante: {self.paciencia}")
        print(f"Nível de raiva: {self.raiva}")

    def reagir(self):
        if self.raiva >= 50:
            print(f"{self.nome} odiou o atendimento!")
            print("A humanidade está em perigo!")
        else:
            print(f"{self.nome} aprovou a comida.")
            print("A humanidade foi salva!")

    def ataque_especial(self):
        print(f"{self.nome} lançou uma ameaça intergaláctica!")