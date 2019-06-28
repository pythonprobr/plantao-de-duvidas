"""
Implementação do Crivo de Eratóstenes

https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes
"""


def crivo(n):
    primos = [2]
    numeros = list(range(3, n + 1, 2))
    while numeros:
        ultimo_primo = primos[-1]
        numeros = [i for i in numeros if i % ultimo_primo != 0]
        if numeros:
            primos.append(numeros[0])
    return primos


print(crivo(1000))
