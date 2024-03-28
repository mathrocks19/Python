# Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N. Por exemplo, o dígito 2 ocorre 3 vezes em 762021192.

def contandoNumeros(n, k):
    #caso de uso
    if n == 0:
        return 0
    #caso de repercusividade
    ultimoNumero = n % 10
    if ultimoNumero == k:
        return 1 + contandoNumeros(n // 10, k)
    else:
        return contandoNumeros(n // 10, k)

if __name__ == '__main__':
    x = int(input("Insira o numero: "))
    z = int(input("Informe qual número quer realizar a contagem:: "))

    print(contandoNumeros(x, z))
