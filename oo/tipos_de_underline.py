from typing import List


class EnviadorDeEmail:
    def __init__(self, lista_de_emails: List[str]):
        print(lista_de_emails)


EnviadorDeEmail(['renzo@python.pro.br'])
EnviadorDeEmail(['renzo@python.pro.br', 'moacir@python.pro,br'])


class Vetor:
    def __init__(self, x=0, y=0):  # método especiais do protocolo do Python
        self._y = y  # protegido
        self.__x = x  # name mangling

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        if valor >= 0:
            self.__x = valor
        else:
            print(f'valor negativo não utilizado: {valor}')

    @property
    def y(self):
        return self._y

    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y)

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return f'Vetor({self.x}, {self.y})'


vetor_1 = Vetor(1, 1)
vetor_2 = Vetor(1, 2)
print(vetor_1.x)
# vetor_1.x = 3
# vetor_1.x = -3
# vetor_1.__x = -3
print(vetor_1._Vetor__x)
print(vetor_1 + vetor_2)
print((vetor_1 + vetor_2).__str__())
print(vetor_1.__dict__)
