"""
>>> juros_simples(10, 20)
12.0
>>> juros_simples(20, 15 + 15)
26.0
"""


def juros_simples(valor: float, juros: float) -> float:
    return valor * (100 + juros) / 100


if __name__ == '__main__':
    print(juros_simples(100, 1))
