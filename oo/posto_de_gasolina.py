"""
>>> posto_ipiranga = Posto(preco_litro_gasolina=4.15)
>>> posto_ipiranga._preco_litro_gasolina
4.15
>>> bomba_gasolina = BombaDeGasolina()
>>> posto_ipiranga.adicionar_bomba_de_gasolina(bomba_gasolina)
>>> posto_ipiranga.adicionar_bomba_de_gasolina(BombaDeGasolina())
>>> posto_ipiranga.repor_reservatorio(1000)
>>> posto_ipiranga.gasolina_disponivel
1000
>>> posto_ipiranga.repor_reservatorio(1000)
>>> posto_ipiranga.gasolina_disponivel
2000
>>> posto_ipiranga.abastacer_com_gasolina(20)
83.0
>>> posto_ipiranga.gasolina_disponivel
1980
>>> posto_ipiranga.controlar_abastecimento()
['Bomba 1: 20 litros', 'Bomba 2: 0 litros']

"""
from typing import List


class SemBombaException(Exception):
    pass


class BombaDeGasolina:
    def __init__(self):
        self._volume_total_abastecido = 0
        self._preco_litro = None
        self._reservatorio = None

    def abastecer(self, volume):
        self._volume_total_abastecido += volume
        self._reservatorio.drenar(volume)
        return self._preco_litro * volume

    @property
    def volume_total(self):
        return self._volume_total_abastecido

    def alterar_preco(self, preco):
        self._preco_litro = preco

    def conectar_reservatorio(self, reservatorio):
        self._reservatorio = reservatorio


class ReservatorioGasolina:
    def __init__(self):
        self._volume_disponivel = 0

    def encher(self, volume):
        self._volume_disponivel += volume

    @property
    def volume_disponivel(self):
        return self._volume_disponivel

    def drenar(self, volume):
        self._volume_disponivel -= volume


class Posto:
    def __init__(self, preco_litro_gasolina):
        self._preco_litro_gasolina = preco_litro_gasolina
        self._bombas_de_gasolina: List[BombaDeGasolina] = []
        self._reservatorio_gasolina = ReservatorioGasolina()

    def abastacer_com_gasolina(self, volume: float) -> float:
        """
        Abstace com gasolina de acordo com volume em litros
        :param volume: volume em litros
        :return: float com preço em Real
        """
        if len(self._bombas_de_gasolina) == 0:
            raise SemBombaException()
        bomba = self._bombas_de_gasolina[0]
        return bomba.abastecer(volume)

    def adicionar_bomba_de_gasolina(self, bomba_gasolina: BombaDeGasolina):
        bomba_gasolina.alterar_preco(self._preco_litro_gasolina)
        bomba_gasolina.conectar_reservatorio(self._reservatorio_gasolina)
        self._bombas_de_gasolina.append(bomba_gasolina)

    def repor_reservatorio(self, volume: float):
        self._reservatorio_gasolina.encher(volume)

    @property
    def gasolina_disponivel(self):
        return self._reservatorio_gasolina.volume_disponivel

    def controlar_abastecimento(self):
        return [f'Bomba {n_bomba}: {bomba.volume_total} litros' for n_bomba, bomba in enumerate(
            self._bombas_de_gasolina, start=1)]


if __name__ == '__main__':
    posto_ipiranga = Posto(preco_litro_gasolina=4.15)
    posto_ipiranga._preco_litro_gasolina
    bomba_gasolina = BombaDeGasolina()
    posto_ipiranga.adicionar_bomba_de_gasolina(bomba_gasolina)
    posto_ipiranga.adicionar_bomba_de_gasolina(BombaDeGasolina())
    posto_ipiranga.repor_reservatorio(1000)
    posto_ipiranga.gasolina_disponivel
    posto_ipiranga.repor_reservatorio(1000)
    posto_ipiranga.gasolina_disponivel
    posto_ipiranga.abastacer_com_gasolina(20)
    posto_ipiranga.gasolina_disponivel
    posto_ipiranga.controlar_abastecimento()
