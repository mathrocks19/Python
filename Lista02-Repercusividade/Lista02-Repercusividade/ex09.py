#Crie uma função recursiva que receba um número inteiro positivo N e calcule o produtório dos números de 1 a N. 

def produtorio(n: int) -> int:
    #caso de uso
    if n < 1:
        return 1
        #caso de repercusividade
    return n * produtorio(n - 1)

if __name__ == '__main__':
    while True:
        try:
            numero = int(input("Informe um número que seja inteiro positivo para calcular o produtório: "))
            if numero > 0:
                print(f"Soma dos números de 1 até {numero}: {produtorio(numero)}")
                break
            else:
                print("Número precisa ser positivo")
        except ValueError:
            print("Caracter informado não é um número inteiro, Por favor informe novamente")