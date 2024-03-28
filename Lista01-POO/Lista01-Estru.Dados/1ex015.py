
class Bichinho:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def __str__(self):
        return f"Características do Bichinho Virtual: Nome: {self.nome} Fome: {self.fome} Saúde: {self.saude} Idade: {self.idade}"

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def alterar_nome(self, novoNome):
        self.nome = novoNome

    def alterar_fome(self, comida):
        self.fome += comida/2

    def alterar_saude(self, novaSaude):
        self.saude = novaSaude

    def alterar_idade(self, novaIdade):
        self.idade = novaIdade

    def retornar_humor(self, tempoParaBrincar=0):
        humor = self.saude / 2 + self.fome / 2
        humor += tempoParaBrincar/5
        
        return humor
       


bichinho = Bichinho("Crypto", 6, 7, 7)
bichinho.alterar_fome(2)
print(bichinho)