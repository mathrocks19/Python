# Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais. Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.



class reverterPilha:
    def __init__(self):
        self.elemento = []  

    def adicionarValor(self, valor):
        self.elemento.append(valor)
        
    def removerValor(self):
        if not self.esta_vazia():
            return self.elemento.pop()
        else:
            return None  #Se a pilha  estiver vazia não faz nada

  
def verificarIgualdade(pilha1, pilha2):
    if len(pilha1.elemento) == len(pilha2.elemento):                 # Verifica se as pilhas são iguais. / #len = obter número da lista
        return True
   
    
def verificarIgualdade2(pilha1, pilha2):
    if len(pilha1.elemento) != len(pilha2.elemento):
        return False

    # Compara os elementos das pilhas na mesma ordem
    for num1, num2 in zip(pilha1.elemento, pilha2.elemento):         #zip= comparar a ordem das pilhas 
        if num1 != num2:
         return False
   

# Exemplo de uso
pilha1 = reverterPilha()
pilha2 = reverterPilha()

pilha1.adicionarValor(1)
pilha1.adicionarValor(9)
pilha1.adicionarValor(0)

pilha2.adicionarValor(1)
pilha2.adicionarValor(9)
pilha2.adicionarValor(0)


resultado = verificarIgualdade   (pilha1, pilha2)
resultado2 = verificarIgualdade2 (pilha1, pilha2)

print(resultado, " , Suas Pilhas são idênticas! ")  # Isso imprimirá True, pois as pilhas são iguais
print(resultado2, " , Suas Pilhas NÃO são idênticas!" )