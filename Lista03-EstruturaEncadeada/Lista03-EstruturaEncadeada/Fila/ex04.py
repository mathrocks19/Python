#4. Escreva uma função que inverta a ordem dos elementos da fila.  Por exemplo:  [1] [4] [5] [2] → [2] [5] [4] [1]

import random

class Nodo:
    def __init__(self, dado=0, proximo=None):
        self.dado = dado
        self.proximo = proximo

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def push(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        if self.ultimo:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.primeiro = self.ultimo = novo_nodo

    def pop(self):
        if self.primeiro:
            self.primeiro = self.primeiro.proximo
            if not self.primeiro:
                self.ultimo = None

    def inverter(self):
        anterior = None
        corrente = self.primeiro
        while corrente:
            proximo = corrente.proximo
            corrente.proximo = anterior
            anterior = corrente
            corrente = proximo
        self.primeiro, self.ultimo = self.ultimo, self.primeiro

    def __repr__(self):
        elementos = []
        corrente = self.primeiro
        while corrente:
            elementos.append(corrente.dado)
            corrente = corrente.proximo
        return str(elementos)

if __name__ == "__main__":
    fila = Fila()
    valores = [1,4,5,2]
    
    for valor in valores:
        fila.push(valor)

    print("Fila:", fila)
    fila.inverter()
    print("Fila invertida:", fila)