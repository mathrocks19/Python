#1. Implemente uma fila dinâmica contendo todas as funcionalidades de uma fila padrão. Para isso, resolvar:
#–Crie um nó padrão da fila.
#–Crie uma função de inicialização da fila vazia
#–Crie uma função push que cria e insere um novo nó para o final da fila.
#–Crie uma função pop que remove o primeiro elemento da fila.


class Nó:

    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return "%s -> %s" % (self.dado, self.proximo)
    
class Fila:
    
    def __init__(self):
        self.primeiroDaFila = None
        self.ultimoDaFila = None

    def __repr__(self):
        return "[" + str(self.primeiroDaFila) + "]"

    def push(self, novo_dado):
        """Inseri um elemento no final da fila"""

        novo_nodo = Nó(novo_dado)

        if self.primeiroDaFila is None:
            self.primeiroDaFila = novo_nodo
            self.ultimoDaFila = novo_nodo
        else:
            self.ultimoDaFila.proximo = novo_nodo
            self.ultimoDaFila = novo_nodo

    def pop(self):
        """Remove o primeiro elemento da fila"""

        assert self.primeiroDaFila is not None, "Impossível remover elemento de fila vazia"

        self.primeiroDaFila = self.primeiroDaFila.proximo
        if self.primeiroDaFila is None:
            self.ultimoDaFila = None


fila = Fila()
print("Fila vazia: ", fila)

for i in range(5):
    fila.push(i)
    print(f"Inseri o valor {i} no final da fila {fila}")

while fila.primeiroDaFila is not None:
    fila.pop()
    print("Removendo o elemento que está no começo da fila: ", fila)
    
    
    