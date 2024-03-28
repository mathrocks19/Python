#2. Crie uma função de busca em que o usuário insere um valor (inteiro) e o programa retorna a sua posição na fila.

import random


def buscarValor(fila, valor):
    corrente = fila.primeiro
    a = 1
    while corrente and corrente.dado != valor:
        corrente = corrente.proximo
        a += 1
    return corrente, a


class Nodo:

    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):                                  #representacao do objeto
        return "%s -> %s" % (self.dado, self.proximo)


class Fila:   

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def push(self, novo_dado):#Inseri um elemento 
    

        novo_nodo = Nodo(novo_dado)

        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def pop(self): #Remove o primeiro elemento da fila
        
        assert self.primeiro != None, "Impossível remover elemento de fila vazia"

        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None


fila = Fila()

for i in range(5):
    fila.push(random.randint(0,10))

print("Fila = ", fila)

valor = int(input("Quer mudar a posição de algum elemento? Se sim, informe um número : "))
posicao = buscarValor(fila, valor)
if posicao[0] is not None:
    print(f"Pronto! agora a posição do elemento {valor} é a posição {posicao[1]} da fila")