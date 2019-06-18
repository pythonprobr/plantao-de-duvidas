class ColeiraComGps:
    def calcular_posicao(self):
        return 'Calculando posição junto ao satélite'


class Cachorro:
    """
    Manter o cadastro do cachorro e latir de acordo
    """

    def __init__(self, nome):
        self.nome = nome
        self.coleira = ColeiraComGps()

    def latir(self):
        return f'Cachorro {self.nome}: Au Au'

    def ir_para_casa(self):
        return f'calcular rota: {self.coleira.calcular_posicao()}'


def teste_latir_cachorro():
    rex = Cachorro('Rex')
    assert 'Cachorro Rex: Au Au' == rex.latir()


class ColeiraMock:
    def calcular_posicao(self):
        return 'Calculando posição junto ao satélite fake'


def testar_ir_para_casa():
    rex = Cachorro('Rex')
    rex.coleira = ColeiraMock()
    assert 'calcular rota: Calculando posição junto ao satélite fake' == rex.ir_para_casa()
