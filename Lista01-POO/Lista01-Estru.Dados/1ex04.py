class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso  # em kg
        self.altura = altura  # em cm

    def envelhecer(self):
        self.idade += 1

    def engordar(self):
        self.peso += 1

    def emagrecer(self):
        self.peso -= 1

    def crescer(self):
        if self.idade < 21:
            self.altura += 0.5
        else:
            self.altura += 0
            
            
Matheus = Pessoa("Matheus", 18, 70, 175)
Matheus.envelhecer()
Matheus.engordar()
Matheus.crescer()

print(f"Nome: {Matheus.nome}, Idade: {Matheus.idade}, Peso: {Matheus.peso} kg, Altura: {Matheus.altura} cm")

