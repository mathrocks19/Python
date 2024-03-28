
class ContaCorrente:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self.saldo = 0

    def alternar_nome(self):
        self.nome = str(input("Insira o seu nome por favor :  "))
        print(self.nome)

    def deposito(self):
        while True:
            deposito = float(input("Quanto vossa excelencia depositar? "))
            if deposito > 0:
                self.saldo += deposito
                break
            else:
                print("Valor inválido")
        print(f"Seu saldo é {conta.saldo:.2f}")

    def saque(self):
        while True:
            saque = float(input("Quanto vossa excelencia quer sacar? "))
            if saque > 0:
                self.saldo -= saque
                break
            else:
                print("Valor inválido")
        print(f"Seu saldo é {conta.saldo:.2f}")


conta = ContaCorrente(123456, "João")
conta.alternar_nome()
conta.deposito()
conta.saque()