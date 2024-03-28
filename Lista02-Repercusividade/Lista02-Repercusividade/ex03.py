#Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 - 321 


def inverter_inteiro(numero):
    # Caso de Uso
    if numero < 10:
        return numero
        # Caso de Recursividade# Caso de Recursividade
    restanteDoNumero = numero // 10
    ultimoNumero = numero % 10
    numero_invertido = inverter_inteiro(restanteDoNumero)
    return int(str(ultimoNumero) + str(numero_invertido))

if __name__ == '__main__':
    print(inverter_inteiro(123))
