#Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente. 

def numerosParesDecrescentes(n: int) -> int:
    if n <= 0:
        return 0
    return 1 + numerosParesDecrescentes(n - 1)

# print(pares_crescentes(10))
if __name__ == '__main__':
    while True:
        numeroescolhido = int(input("Insira um numero par: "))
        if numeroescolhido % 2 == 0: #condição do n° par
            break
        else:
            print("Número inválido, tente novamente.")

    for m in range(numeroescolhido, -1, -2): #condicao decrescente
        print(numerosParesDecrescentes(m))