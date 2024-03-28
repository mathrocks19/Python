#Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente. 

def ordemDecrescente(n: int) -> int:
    if n <= 0:
        return n
    return ordemDecrescente(n - 1) + 1

if __name__ == '__main__':
    n = int(input("Informe um número inteiro para realizar a contagem de números decrescente: "))
    print(f"0 até {n}:")
    for x in range(n, -1, -1):
        print(ordemDecrescente(x))