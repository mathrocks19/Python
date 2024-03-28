# Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci. Alguns números desta sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

def sequenciaDoFibonacci(n: int) -> int:
    if n < 1:
        return 0
    if n <= 2:
        return 1
    return sequenciaDoFibonacci(n - 1) + sequenciaDoFibonacci(n - 2)


if __name__ == "__main__":
    n = int(input("Informe um número pra escrever a sua sequência : "))
    for i in range(n):
        print(sequenciaDoFibonacci(i))