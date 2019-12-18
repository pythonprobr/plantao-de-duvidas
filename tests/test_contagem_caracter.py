from collections import Counter


def conta_letra(s):
    return Counter(s)


def test_conta_letras():
    assert {'a': 3, 'r': 2} == conta_letra('arara')
