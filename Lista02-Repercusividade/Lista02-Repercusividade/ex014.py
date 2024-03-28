# Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente.  

def NumerosParesCrescentes(n: int) -> int:
    #caso de uso
    if n <= 0:
        return 0
    #caso de repercusividade
    return 1 + NumerosParesCrescentes(n - 1)


if __name__ == '__main__':
    while True:
        numero = int(input("Informe um numero que seja par: "))
        if numero % 2 == 0: #condição do n° par
            break
        else:
            print("Número informado não é par, por favor informe novamente: ")

    print(f"Numeros pares de 0 a {numero}:")
    for m in range(0, numero + 1, 2): #condicao crescente
        print(NumerosParesCrescentes(m))
        
        
        
        
        
        
        