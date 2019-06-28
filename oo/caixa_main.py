from oo.caixa import Caixa, PagamentoEmCartaoDeCredito, PagamentoEmCartaoDeDebito, PagamentoEmDinheiro

if __name__ == '__main__':
    caixa = Caixa()
    tipos_pagamento = {
        '1': (PagamentoEmDinheiro, caixa.pagar_em_dinheiro),
        '2': (PagamentoEmCartaoDeCredito,caixa.pagar_em_cc),
        '3': (PagamentoEmCartaoDeDebito,caixa.pagar_em_cd)}
    while True:
        codigo_tipo_pagamento = input('Escolha uma opção de pagamento: (1 - Dinheiro, 2 - CC, 3 - CD): ')
        pagamento_classe, metodo_pgto = tipos_pagamento[codigo_tipo_pagamento]
        dados_pagamento = pagamento_classe.obter_dados()
        metodo_pgto(*dados_pagamento)
        print(caixa.ultimo_pagamento())
        print(caixa.consultar_fita())

