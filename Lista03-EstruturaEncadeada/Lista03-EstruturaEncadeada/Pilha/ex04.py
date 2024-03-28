#Construa um programa utilizando uma pilha que resolva o seguinte problema: 

#Armazene as placas dos carros (apenas os números) que estão estacionados numa rua sem saída estreita. 
#Dado uma placa verifique se o carro está estacionado na rua. 
#Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair.

        
class Nodo:
    """ Esta classe representa um nodo em uma encadeada"""

    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return "%s -> %s" % (self.dado, self.anterior)


class Pilha:
    """ Esssa classe representa uma pilha usando uma estrutura encadeada"""

    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def inserir(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo

    def remover(self):
        assert self.topo, "Não consigo remover valor da pilha vazia"
        self.topo = self.topo.anterior

    def buscar(self, valor):
        corrente = self.topo
        while corrente and corrente.dado != valor:
            corrente = corrente.anterior
        return corrente

    def carrosRemovidos(self, valor):
        corrente = self.topo
        while True:
            if corrente.dado != valor:
                print(corrente.dado, end=" ")
            if corrente.dado == valor:
                break
            corrente = corrente.anterior



    