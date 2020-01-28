from typing import List, Tuple

import pytest


def bisect_left(lista_ordenada, procurado):
    inicio = 0
    fim = len(lista_ordenada)
    while inicio < fim:
        meio = (inicio + fim) // 2
        elemento_do_meio = lista_ordenada[meio]
        if elemento_do_meio < procurado:
            inicio = meio + 1
        else:
            fim = meio
    return inicio


def bisect_right(lista_ordenada, procurado):
    inicio = 0
    fim = len(lista_ordenada)
    while inicio < fim:
        meio = (inicio + fim) // 2
        elemento_do_meio = lista_ordenada[meio]
        if elemento_do_meio > procurado:
            fim = meio
        else:
            inicio = meio + 1
    return inicio


def buscar_indices_re_repeticao(lista_ordenada: List[int], procurado: int) -> Tuple[int, int]:
    """
    ###### Solução 1
    inicio = lista_ordenada.index(procurado)  # O(1)
    lista_revertida = lista_ordenada[::-1]  # O(n)
    fim = len(lista_ordenada) - lista_revertida.index(procurado) - 1 # O(1)
    return (inicio, fim)


    Análise de Tempo de Exeução
    O(3n)  == O(n)

    Análise de Memória:
    O(n + 2) ==O(n(1 + 2/n)) == O(n)


    ###### Solução 2
    inicio = bisect_left(lista_ordenada, procurado)
    fim = bisect_right(lista_ordenada, procurado)
    if fim == inicio:
        raise ValueError(f'O elmento {procurado} não está presente na lista ')
    return (inicio, fim - 1)

    Análise de Tempo de Exeução
    O(2log(n))  == O(log(n))

    Análise de Memória:
    O(1)



    :param lista_ordenada:
    :param procurado:
    :return:
    """
    inicio = bisect_left(lista_ordenada, procurado)
    fim = bisect_right(lista_ordenada, procurado)
    if fim == inicio:
        raise ValueError(f'O elmento {procurado} não está presente na lista ')
    return (inicio, fim - 1)


def test_elemento_ocorre_uma_vez():
    assert buscar_indices_re_repeticao([1, 2, 3, 4, 5, 6, 7, 8], 7) == (6, 6)


def test_elemento_ocorre_duas_vez():
    assert buscar_indices_re_repeticao([1, 2, 3, 4, 5, 6, 7, 7, 8], 7) == (6, 7)


def test_elemento_nao_esta_na_lista():
    with pytest.raises(ValueError):
        buscar_indices_re_repeticao([1, 2, 3, 4, 5, 6, 7, 7, 8], -1)


def test_elemento_nao_esta_na_lista():
    with pytest.raises(ValueError):
        buscar_indices_re_repeticao([1, 2, 3, 4, 5, 6, 7, 7, 8], 9)


if __name__ == '__main__':
    buscar_indices_re_repeticao([1, 2, 3, 4, 5, 6, 7, 8], 7)
