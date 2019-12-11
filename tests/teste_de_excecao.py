import pytest


def divisao(numerador, denominador):
    return numerador / denominador


def testar_excecao():
    with pytest.raises(ZeroDivisionError):
        divisao(2, 0)


def soma(n, n2):
    return n+n2


@pytest.mark.parametrize(
    'x', [1, 2, 3]
)
@pytest.mark.parametrize(
    'y', [1, 2, 3]
)
def test_soma(x, y):
    resultado = soma(x, y)
    assert resultado - x == y
