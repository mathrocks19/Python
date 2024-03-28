#O máximo divisor comum dos inteiros x e y é o maior inteiro que é divisível por x e y. Escreva uma função recursiva mdc em python, que retorna o máximo divisor comum de x e y. O mdc de x e y é definido como segue: se y é igual a 0, então mdc(x,y) é x; caso contrário, mdc(x,y) é mdc (y, x%y), onde % é o operador resto. 

def mdc(x, y):
    if y == 0:
        return x
    return mdc(y, x % y)

if __name__ == '__main__':
    numero1 = int(input("Informe o primeiro numero para calcular o mdc: "))
    numero2 = int(input("Informe o segundo numero para calcular o mdc: "))

    print(mdc(numero1, numero2))