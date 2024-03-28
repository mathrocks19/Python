#Utilizando uma pilha resolver o exercício a seguir: Dada uma sequência contendo N (N >0) números reais, imprimi-la na ordem inversa

def inverterOrdem(pilha):
    while pilha.topo:
        print(pilha.topo.dado, end=" ")   # (end= "" )  quebra a linha
        pilha.remove()


class Nos:
    
    def __init__(self, dado=0, Nos_anterior=None):
        self.dado = dado
        self.anterior = Nos_anterior

    def __repr__(self):
        return "%s -> %s" % (self.dado, self.anterior)


class Pilha:
    
    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
       
       
        novo_Nos = Nos(novo_dado)
        novo_Nos.anterior = self.topo
        self.topo = novo_Nos

    def remove(self):
        
        
        assert self.topo, "Não consigo remover valor da pilha vazia"
        self.topo = self.topo.anterior


sequencia = [5, 6, 7, 8, 9, 10]
pilha = Pilha()
print("Sequencia original: ", end=" ")
for numero in sequencia:
    print(numero, end=" ")
    pilha.insere(numero)
print("\nSequência invertida: ", end="")    #\ reverte a string
inverterOrdem(pilha)