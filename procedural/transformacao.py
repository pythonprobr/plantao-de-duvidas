from typing import List


def para_listas_em_dicionario(chaves: List[int], produtos: List[str]):
    dct = {}
    for chave, produto in zip(chaves, produtos):
        lista_produtos = dct.get(chave, [])
        lista_produtos.append(produto)
        dct[chave] = lista_produtos

    return dct


if __name__ == '__main__':
    print(para_listas_em_dicionario([1, 1, 2], ['creme de galinha', 'mugunzá', 'creme de galinha']))
