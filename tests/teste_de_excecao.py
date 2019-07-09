import pytest


def divisao(numerador, denominador):
    return numerador / denominador


def testar_excecao():
    with pytest.raises(ZeroDivisionError):
        divisao(2, 0)
