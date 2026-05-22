class Protagonistas:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def mostrar_informações(self):
        return f"Nome do Personagem: {self.name}, ID: {self.id}"   

class Hoshigo(Protagonistas):
    
    def cozinhando(self):
        return f"{self.name} está cozinhando."
    
    def pegar_tomate(self):
        cesta_tomates = 10
        cesta_tomates -= 1




        return f"{self.name} pegou o tomate. Restam {cesta_tomates} tomates."