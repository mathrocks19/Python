#Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N. 

#Soma de 1 até N = (N * (N + 1)) / 2

def somatorio(n: int) -> int:
    if n < 1:
        return 0
    return n + somatorio(n - 1)

if __name__ == '__main__':
    while True:
        try:
            numero = int(input("Informe um número que seja inteiro positivo: "))
            if numero > 0:
                print(f"Soma dos números de 1 até {numero}: {somatorio(numero)}")
                break
            else:
                print("Número precisa ser positivo")
        except ValueError:
            print("Caracter informado não é um número inteiro, Por favor informe novamente")