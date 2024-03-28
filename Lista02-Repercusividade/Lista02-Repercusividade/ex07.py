#Crie um programa em python que receba um vetor de números reais com 100 elementos. Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor. 

def inverterVetor(vetor, comeco, fim):
    #caso de uso
    if comeco < fim:
        vetor[comeco], vetor[fim] = vetor[fim], vetor[comeco]
    #caso de repercusividade
        inverterVetor(vetor, comeco + 1, fim - 1)


if __name__ == '__main__':
    numeros = [m for m in range(1, 101)] #min 1, max 101
    print("Vetor 1 a 100:", numeros)
    inverterVetor(numeros, 0, 99)
    print("Vetor 1 a 100 (invertido):", numeros)
