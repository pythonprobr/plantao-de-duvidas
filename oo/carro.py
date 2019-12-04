#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incremetar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
1) Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
2) Método girar_a_esquerda

  N
O   L
  S

    Exemplo:
    >>> # Testando _motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar_com_fio()
    >>> motor.velocidade
    1
    >>> motor.acelerar_com_fio()
    >>> motor.velocidade
    2
    >>> motor.acelerar_com_fio()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> luz_de_freio = LuzDeFreio()
    >>> carro = Carro(direcao, motor, luz_de_freio)
    >>> carro.velocidade
    0
    >>> carro.acelerar()
    >>> carro.velocidade
    1
    >>> carro.acelerar()
    >>> carro.velocidade
    2
    >>> carro.luz_de_freio
    'Desligada'
    >>> carro.frear()
    >>> carro.luz_de_freio
    'Ligada'
    >>> carro.velocidade
    0
    >>> carro.direcao.valor
    'Norte'
    >>> carro.direcao.girar_a_direita()
    >>> carro.direcao.valor
    'Leste'
    >>> carro.direcao.girar_a_esquerda()
    >>> carro.direcao.valor
    'Norte'
    >>> carro.direcao.girar_a_esquerda()
    >>> carro.direcao.valor
    'Oeste'
    >>> motor_de_ferrari = MotorDeFerrari()
    >>> ferrari = Carro(direcao, motor_de_ferrari, luz_de_freio)
    >>> ferrari.velocidade
    0
    >>> ferrari.acelerar()
    >>> ferrari.velocidade
    10
"""


class LuzDeFreio:
    def __init__(self):
        self.status = 'Desligada'

    def ligar(self):
        self.status = 'Ligada'


class Carro:
    def __init__(self, direcao, motor, luz_de_freio: LuzDeFreio):
        self._luz_de_freio: LuzDeFreio = luz_de_freio
        self._motor = motor
        self.direcao = direcao

    def acelerar(self):
        self._motor.acelerar_com_fio()

    @property
    def velocidade(self):
        return self._motor.velocidade

    @property
    def luz_de_freio(self):
        return self._luz_de_freio.status

    def frear(self):
        self._luz_de_freio.ligar()
        return self._motor.frear()


class Motor:
    _taxa_de_aceleracao = 1

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def velocidade(self):
        return self.velocidade

    def acelerar_com_fio(self):
        self.velocidade += self._taxa_de_aceleracao

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0


class MotorDeFerrari(Motor):
    _taxa_de_aceleracao = 10


class Direcao:
    def __init__(self, valor='Norte'):
        self.valor = valor

    def valor(self):
        return self.valor

    def girar_a_direita(self):
        if (self.valor == 'Norte'):
            self.valor = 'Leste'
        elif (self.valor == 'Leste'):
            self.valor = 'Sul'
        elif (self.valor == 'Sul'):
            self.valor = 'Oeste'
        elif (self.valor == 'Oeste'):
            self.valor = 'Norte'

    def girar_a_esquerda(self):
        if (self.valor == 'Norte'):
            self.valor = 'Oeste'
        elif (self.valor == 'Oeste'):
            self.valor = 'Sul'
        elif (self.valor == 'Sul'):
            self.valor = 'Leste'
        elif (self.valor == 'Leste'):
            self.valor = 'Norte'
