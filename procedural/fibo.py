from time import process_time
from typing import Callable


def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


count = 0


def _func_rec_com_estado(n, penultimo=0, ultimo=1, i=1):
    global count
    count += 1
    print(count)
    if i == n:
        return ultimo
    return _func_rec_com_estado(n, ultimo, ultimo + penultimo, i + 1)


def fibo_rec(n: int) -> int:
    if n == 0:
        return 0
    return _func_rec_com_estado(n)


def soma(a: int, b: int) -> int:
    if b == 0:
        return a
    return soma(a + 1, b - 1)


if __name__ == '__main__':
    def contar_tempo(f: Callable, n: int) -> None:
        print(f'Função: {f.__name__}')
        comeco = process_time()
        print(f'valor:{f(n)}')
        fim = process_time()
        print(f'Tempo para n = {n}: {fim - comeco}')


    # for i in range(1, 40):
    #     for funcao in (fib, fib2, fibo_rec):
    #         contar_tempo(funcao, i)
    print(contar_tempo(fibo_rec, 30))
    print(contar_tempo(fib, 30))

    # print(soma(4, 3))
