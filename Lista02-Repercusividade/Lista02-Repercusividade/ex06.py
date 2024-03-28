# Crie um programa em python, que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule k^n . Utilize apenas multiplicações. O programa principal deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da função. 

def potenciacao(k: int, n: int) -> int:
        #caso de uso
    if n == 0:
        return 1
    if n == 1:
        return k
        #caso de repercusividade
    return k * potenciacao(k, n - 1)

if __name__ == '__main__':
    numero = int(input("Informe um numero que seja inteiro: "))
    potencia = int(input(f"Informe um numero deseja calcular a potenciação ({numero}): "))

    print(f"{numero} elevado a {potencia} é {potenciacao(numero, potencia)}.")
