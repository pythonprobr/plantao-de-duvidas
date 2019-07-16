try:

    for linha in arquivo:
        raise Exception()
        print(linha)
finally:
    print('Fechado')
    arquivo.close()
