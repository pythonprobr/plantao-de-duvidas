from typing import Callable


def contextmanager(chamavel: Callable):
    gerador = chamavel()

    class GerenciadorDeContexto:
        def __enter__(self):
            return next(gerador)

        def __exit__(self, exc_type, exc_val, exc_tb):
            next(gerador, None)

    return GerenciadorDeContexto


@contextmanager
def Arquivo():
    print(f'Enter: ')
    yield 'foo'
    print('Saida')


with Arquivo() as arquivo:
    # raise Exception()
    print(arquivo)
    print(id(arquivo))
