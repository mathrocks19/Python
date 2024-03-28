#A função fatorial duplo é definida como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15 Faça uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número.

def fatorial_duplo(n: int) -> int:
    if n <= 1:
        return 1
    return n * fatorial_duplo(n - 2)


if __name__ == '__main__':
    while True:
        numero = int(input("Informe um número impar que seja positivo: "))
        if numero % 2 == 0 or numero < 1:
            print("Número inserido não é impar, por favor informe novamente outro número :")
        else:
            print(fatorial_duplo(numero))
        break  #Caso queira continuar o input só remover o break