class Carro:
    def __init__(self, autonomia):
        self.autonomia = autonomia
        self.combustivel = 0

    def adicionar_gasolina(self, litros):
        self.combustivel = litros
        if self.combustivel > 100:
            self.combustivel = 100 
        return self.combustivel



    # distancia / litros
    def andar(self, distancia):  
        gasto = distancia / self.autonomia
        self.combustivel -= gasto
        if self.combustivel < 0:
            self.combustivel = 0
        return self.combustivel

    def obter_gasolina(self):
        return self.combustivel


meuSkyline = Carro(15)
meuSkyline.adicionar_gasolina(20)
meuSkyline.andar(100)
meuSkyline.obter_gasolina()
print(meuSkyline.obter_gasolina())