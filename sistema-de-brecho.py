# Created By Paulo Vitor Vieira

class Brecho:
    def __init__(self):
        self.cliente_atual = None
        self.vendas = []
        self.valor_por_fornecedor = {}
        self.valor_por_forma_pagamento = {}

    def iniciar_compra(self):
        self.cliente_atual = {
            'vendas': [],
            'valor_total_compra': 0
        }

    def realizar_venda(self, tipo_peca, valor, fornecedor, quantidade):
        valor_total = valor * quantidade
        self.cliente_atual['vendas'].append({
            'tipo_peca': tipo_peca,
            'valor_total': valor_total,
            'fornecedor': fornecedor,
            'quantidade': quantidade
        })

        self.cliente_atual['valor_total_compra'] += valor_total

        if fornecedor in self.valor_por_fornecedor:
            self.valor_por_fornecedor[fornecedor] += valor_total
        else:
            self.valor_por_fornecedor[fornecedor] = valor_total

    def finalizar_compra(self, forma_pagamento):
        if self.cliente_atual is None:
            print("Nenhuma venda registrada para esse cliente.")
            return

        forma_pagamento = forma_pagamento.lower()
        self.cliente_atual['forma_pagamento'] = forma_pagamento

        desconto_input = input("Digite o percentual de desconto (ou pressione Enter para 0%): ")
        try:
            desconto = float(desconto_input.replace(',', '.'))  # Substituir vírgula por ponto
        except ValueError:
            desconto = 0

        desconto /= 100
        valor_com_desconto = self.cliente_atual['valor_total_compra'] * (1 - desconto)
        self.cliente_atual['valor_total_compra'] = valor_com_desconto

        self.vendas.append(self.cliente_atual)

        if forma_pagamento in self.valor_por_forma_pagamento:
            self.valor_por_forma_pagamento[forma_pagamento] += valor_com_desconto
        else:
            self.valor_por_forma_pagamento[forma_pagamento] = valor_com_desconto

        self.cliente_atual = None

    def exibir_valores_por_fornecedor(self):
        print("Valores por fornecedor:")
        for fornecedor, valor in self.valor_por_fornecedor.items():
            print("{}: {:.2f}".format(fornecedor, valor))  # Modificação da formatação da string

    def exibir_valores_por_forma_pagamento(self):
        print("Valores por forma de pagamento:")
        for forma_pagamento, valor in self.valor_por_forma_pagamento.items():
            print("{}: {:.2f}".format(forma_pagamento, valor))  # Modificação da formatação da string


brecho = Brecho()

while True:
    opcao = input("Digite '1' para adicionar uma venda, '2' para finalizar compra desse cliente, ou '3' para finalizar brechó: ")

    if opcao == '1':
        if brecho.cliente_atual is None:
            brecho.iniciar_compra()

        tipo_peca = input("Digite o tipo da peça: ")
        valor_input = input("Digite o valor da peça: ")
        try:
            valor = float(valor_input.replace(',', '.'))  # Substituir vírgula por ponto
        except ValueError:
            print("Valor inválido. Certifique-se de inserir um número válido.")
            continue

        fornecedor = input("Digite o fornecedor: ")
        if not fornecedor.isalpha():
            print("Nome de fornecedor inválido. Certifique-se de usar apenas letras.")
            continue

        quantidade_input = input("Digite a quantidade de peças iguais (ou pressione Enter para 1 peça): ")
        quantidade = int(quantidade_input) if quantidade_input else 1

        brecho.realizar_venda(tipo_peca, valor, fornecedor, quantidade)

    elif opcao == '2':
        if brecho.cliente_atual is None:
            print("Nenhuma venda registrada para esse cliente.")
            continue

        forma_pagamento = input("Digite a forma de pagamento: ")
        brecho.finalizar_compra(forma_pagamento)
        print("Valor total da compra com desconto desse cliente: {:.2f}".format(brecho.vendas[-1]['valor_total_compra']))  # Modificação da formatação da string

    elif opcao == '3':
        brecho.exibir_valores_por_fornecedor()
        brecho.exibir_valores_por_forma_pagamento()
        break

    else:
        print("Opção inválida. Por favor, digite '1', '2' ou '3'.")
