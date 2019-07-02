from typing import List


class Eletrodomestico:
    def ligar(self):
        raise NotImplementedError()


class Liquificador(Eletrodomestico):

    def ligar(self):
        """
        Este método liga um liquidificador retorna uma string
        :return: str
        """
        return 'Ligando Liquidificador'


class Aspirador(Eletrodomestico):
    def ligar(self):
        """
        Este método liga um aspirador retorna uma string
        :return: str
        """
        return 'Ligando Aspirador'


class Casa:
    def __init__(self):
        self._eletrodomesticos: List[Eletrodomestico] = []

    def adicionar_eletrodomestico(self, eletrodomestico: Eletrodomestico):
        self._eletrodomesticos.append(eletrodomestico)

    def ligar_todos_eletrodomesticos(self) -> str:
        return ', '.join(eletro.ligar() for eletro in self._eletrodomesticos)


if __name__ == '__main__':
    liquifificador = Liquificador()
    resultado_liquidificador_ligado = liquifificador.ligar()

    casa = Casa()

    casa.adicionar_eletrodomestico(liquifificador)
    casa.adicionar_eletrodomestico(Aspirador())
    print(casa.ligar_todos_eletrodomesticos)
    print(casa.ligar_todos_eletrodomesticos())
