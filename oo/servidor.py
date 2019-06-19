"""
>>> servidor = Servidor()
>>> servidor.executar_ciclo()
[]
>>> servidor.acrescentar_tarefa(3, 2)  #6
>>> servidor.executar_ciclo()  # 5
[3]
>>> servidor.executar_ciclo()  # 4
[2]
>>> servidor.executar_ciclo() #3
[2]
>>> servidor.executar_ciclo() # 2
[1]
>>> servidor.acrescentar_tarefa(5, 1)
>>> servidor.executar_ciclo()  #1
[1, 4]
>>> servidor.executar_ciclo() # 0
[3]
>>> servidor.executar_ciclo()
[2]
>>> servidor.executar_ciclo()
[1]
>>> servidor.executar_ciclo()
[]
"""
from math import ceil


class Tarefa:
    """
    Gerenciar ciclo de vida de exeução de acordo com quantidade de ciclos e velocidade de consumo
    """

    def __init__(self, quantidade_de_ciclos, velocidade_de_consumo):
        self._velocidade_de_consumo = velocidade_de_consumo
        self._ciclos_para_finalizar = quantidade_de_ciclos * velocidade_de_consumo

    def consumir_ciclo(self) -> None:
        self._ciclos_para_finalizar -= 1

    def acabou(self) -> bool:
        return self._ciclos_para_finalizar == 0

    def __repr__(self):
        return repr(ceil(self._ciclos_para_finalizar / self._velocidade_de_consumo))


class Servidor:
    """
    Gerenciamento de tarefas por ciclo
    """

    def __init__(self):
        self._tarefas = []

    def executar_ciclo(self):
        for tarefa in self._tarefas:
            tarefa.consumir_ciclo()

        self._tarefas = [t for t in self._tarefas if not t.acabou()]

        return self._tarefas

    def acrescentar_tarefa(self, quantidade_de_ciclos=3, velocidade_de_consumo=1):
        self._tarefas.append(Tarefa(quantidade_de_ciclos, velocidade_de_consumo))



