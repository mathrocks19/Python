 #Faça uma função recursiva que permita somar os elementos de um vetor de inteirosF
 
def somarVetor(lista):
    #Caso de uso
    if not lista:
        return 0
    return lista[0] + somarVetor(lista[1:])
    #Caso repercusivo
if __name__ == '__main__':
    lis = []
    while True:
        try:
            numero = int(input("Insira um inteiro para adicionar à lista (obs: escreva 7 para encerrar): "))
            if numero == 7:
                break
            else:
                lis.append(numero)
        except ValueError:
            print("Caracter inválido.")

    if not lis:
        print("Lista vazia")
    else:
        resultado = somarVetor(lis)
        print(f"A soma dos elementos da lista é: {resultado}")