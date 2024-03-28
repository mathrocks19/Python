#Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente. 

def ordemCrescente(n: int) -> int:
    #caso de uso
    if n <= 0:
        return n
    #caso de repercusividade
    return 1 + ordemCrescente(n - 1)

if __name__ == '__main__':
    n = int(input("Informe um número inteiro para realizar a contagem de números: "))
    print(f"0 até {n}:")
    for x in range(0, n + 1):
        print(ordemCrescente(x))