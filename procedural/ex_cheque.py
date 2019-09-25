# http://dojopuzzles.com/problemas/exibe/lendo-um-cheque/
"""
>>> transformar_real('um centavo')
'0,01'
>>> transformar_real('dois centavos')
'0,02'
>>> transformar_real('três centavos')
'0,03'
>>> transformar_real('quatro centavos')
'0,04'
>>> transformar_real('cinco centavos')
'0,05'
>>> transformar_real('seis centavos')
'0,06'
>>> transformar_real('sete centavos')
'0,07'
>>> transformar_real('oito centavos')
'0,08'
>>> transformar_real('nove centavos')
'0,09'
>>> transformar_real('dez centavos')
'0,10'
>>> transformar_real('onze centavos')
'0,11'
>>> transformar_real('doze centavos')
'0,12'
>>> transformar_real('treze centavos')
'0,13'
>>> transformar_real('quatorze centavos')
'0,14'
>>> transformar_real('quinze centavos')
'0,15'
>>> transformar_real('dezesseis centavos')
'0,16'
>>> transformar_real('dezessete centavos')
'0,17'
>>> transformar_real('dezoito centavos')
'0,18'
>>> transformar_real('dezenove centavos')
'0,19'
>>> transformar_real('vinte centavos')
'0,20'
>>> transformar_real('vinte e um centavos')
'0,21'
>>> transformar_real('vinte e dois centavos')
'0,22'
>>> transformar_real('vinte e nove centavos')
'0,29'
>>> transformar_real('trinta centavos')
'0,30'
>>> transformar_real('trinta e um centavos')
'0,31'
>>> transformar_real('quarenta e um centavos')
'0,41'
>>> transformar_real('cinquenta e um centavos')
'0,51'
>>> transformar_real('sessenta e um centavos')
'0,61'
>>> transformar_real('setenta e um centavos')
'0,71'
>>> transformar_real('oitenta e um centavos')
'0,81'
>>> transformar_real('noventa e um centavos')
'0,91'
>>> transformar_real('um real e noventa e um centavos')
'1,91'
>>> transformar_real('onze real e noventa e um centavos')
'11,91'
>>> transformar_real('vinte e um reais e noventa e um centavos')
'21,91'
>>> transformar_real('noventa e nove reais e noventa e um centavos')
'99,91'
>>> transformar_real('cem reais e noventa e um centavos')
'100,91'
>>> transformar_real('cento e um reais e noventa e um centavos')
'101,91'
>>> transformar_real('cento e trinta e um reais e noventa e um centavos')
'131,91'
>>> transformar_real('cento e noventa e nove reais e noventa e um centavos')
'199,91'
>>> transformar_real('duzentos e noventa e nove reais e noventa e um centavos')
'299,91'
>>> transformar_real('novecentos e noventa e nove reais e noventa e um centavos')
'999,91'
>>> transformar_real('novecentos e noventa e nove reais')
'999,00'
>>> transformar_real('novecentos e noventa e nove mil reais')
'999.000,00'
>>> transformar_real('duzentos e quarenta e cinco milhões novecentos e noventa e nove mil reais')
'245.999.000,00'

"""
from collections import deque

dct_extenso_para_numerico = {
    'zero': 0,
    'um': 1,
    'dois': 2,
    'três': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9,
    'dez': 10,
    'onze': 11,
    'doze': 12,
    'treze': 13,
    'quatorze': 14,
    'quinze': 15,
    'dezesseis': 16,
    'dezessete': 17,
    'dezoito': 18,
    'dezenove': 19,
    'vinte': 20,
    'trinta': 30,
    'quarenta': 40,
    'cinquenta': 50,
    'sessenta': 60,
    'setenta': 70,
    'oitenta': 80,
    'noventa': 90,
    'cem': 100,
    'cento': 100,
    'duzentos': 200,
    'trezentos': 300,
    'quatrocentos': 400,
    'quinhentos': 500,
    'seiscentos': 600,
    'setecentos': 700,
    'oitocentos': 800,
    'novecentos': 900,
}

multiplicadores_extenso_para_float = {
    'centavos': 0.01,
    'centavo': 0.01,
    'real': 1.0,
    'reais': 1.0,
    'mil': 1_000,
    'milhões': 1_000_000,
    'milhão': 1_000_000,
}


def tranformar_em_inteiro(numeros):
    acumulador = 0
    for numero in numeros:
        acumulador += dct_extenso_para_numerico[numero]
    return acumulador


def transformar_real(real_por_extenso: str) -> str:
    acumulador = 0
    numeros = []
    multiplicador = 1
    for palavra in reversed([palavra for palavra in real_por_extenso.split() if palavra != 'e']):
        if palavra in multiplicadores_extenso_para_float:
            inteiro = tranformar_em_inteiro(numeros)
            acumulador += inteiro * multiplicador
            multiplicador = multiplicadores_extenso_para_float[palavra]
            numeros = []
        else:
            numeros.append(palavra)
    inteiro = tranformar_em_inteiro(numeros)
    acumulador += inteiro * multiplicador
    centavos = f'{acumulador:,.2f}'.replace(',', '_').replace('.', ',').replace('_', '.')
    return centavos
