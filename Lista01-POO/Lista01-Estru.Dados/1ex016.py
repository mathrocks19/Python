#Porta escondida

class Bichinho:
    def __init__(self, Nome, Fome = 10, Saude = 0, Idade = 1):
        self.Nome=(Nome)
        self.Fome=(Fome)
        self.Saude=(Saude)
        self.Idade=(Idade)

    def Nome(self, Nome):
        self.Nome = Nome

    def Nome(self):
        return self.Nome

    def Fome(self, Fome):
        self.Fome = Fome

    def Fome(self):
        return self.Fome

    def Saude(self, Saude):
        self.Saude = Saude

    def Saude(self):
        return self.Saude
        
    def Idade(self, Idade):
        self.Idade = Idade

    def Idade(self):
        return self.Idade
    
Bichinho = Bichinho('Vanderlei')
Bichinho.Nome('Nome')
Bichinho.Fome(9)
Bichinho.Saude(5)
Bichinho.Idade(10)

    
    