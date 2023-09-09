# Solicitar o valor ao usuário
valor_original = float(input("Digite o valor original: "))

# Calcular o valor com 30% de desconto
desconto = valor_original * 0.3
valor_com_desconto = valor_original - desconto

# Exibir o valor com desconto
print(f"Valor com 30% de desconto: R${valor_com_desconto:.2f}")
