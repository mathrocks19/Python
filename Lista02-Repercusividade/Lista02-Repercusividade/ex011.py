#A multiplicação de dois números inteiros pode ser feita através de somas sucessivas. Proponha um algoritmo recursivo Multip_Rec(n1,n2) que calcule a multiplicação de dois inteiros. 

def multiploDeNumero(n1: int, n2: int) -> int: #recebendo n1, n2 e devolvendo
    #caso de uso
    if n2 == 0:
        return 0
    if n2 == 1:
        return n1
    #caso de repercusividade
    return n1 + multiploDeNumero(n1, n2 - 1)


if __name__ == '__main__':
    primeironumero = int(input("Insira o primeiro fator: "))
    segundonumero = int(input("Insira o segundo fator: "))

    print(f"{primeironumero} x {segundonumero} = {multiploDeNumero(primeironumero, segundonumero)}")