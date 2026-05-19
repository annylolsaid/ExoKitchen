# classe pai
class Alien:
    def __init__(self,nome,paciencia):
        self.nome = nome
        self.paciencia = paciencia
        self.satisfacao = 100

    def fazer_pedido(self):
        print (f"{self.nome} fez um pedido alienígena")

    def esperar(self): 
        self.paciencia -= 10
        print(f"paciencia restante:{self.paciencia}")

    def reagir (self):
        print(f"{self.nome} recebeu o prato.")

    #classes filhas 
class aliencalmo (Alien):
    def __init__(self, nome,):
        super().__init__(nome, paciencia = 100)
    def reagir(self):
        print(f"{self.nome} ficou feliz e esperou com calma.")


class AlienImpaciente(Alien):

    def __init__(self, nome):
        super().__init__(nome, paciencia=50)

    def esperar(self):
        self.paciencia -= 25
        print(f"{self.nome} está ficando irritado!")
        print(f"Paciência restante: {self.paciencia}")

    def reagir(self):
        print(f"{self.nome} reclamou da demora!")


class AlienExigente(Alien):

    def __init__(self, nome):
        super().__init__(nome, paciencia=70)

    def reagir(self):
        print(f"{self.nome} analisou cuidadosamente a comida.")
        print("Qualquer erro fará ele perder pontos.")



        
                  