#1. Escrever uma função que receba como parâmetro uma pilha. A função deve retornar o maior elemento da pilha.

def acharMaiorElemento(duracell):
    maiorElemento = duracell[0]  
    
    for elemento in duracell:
        if elemento> maiorElemento:
            maiorElemento = elemento #Resultando no maior elemento da pilha
            
    return elemento

duracell = [0,1,2,3,4,5,6,7,8,9,10]
maiorElemento = acharMaiorElemento(duracell)
print(maiorElemento)