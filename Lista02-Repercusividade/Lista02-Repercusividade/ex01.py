#Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N

def fatorial(n: int) -> int:  #recebe numero inteiro e devolve numero inteiro
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


m = int(input("escreva algo ai: "))
res= fatorial(m)
print("o seu fatorial %d é %d " % (m,res))  #%d coloca numero inteiro na tela
    