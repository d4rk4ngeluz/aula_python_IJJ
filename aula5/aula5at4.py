# Solicitar o valor da compra ao cliente
valor_compra = float(
    input("Por favor, digite o valor total da sua compra: R$ "))

# Verificar se o cliente se qualifica para o vale-compras
if valor_compra >= 100:
    # Cliente qualificado
    print("SUA SAÚDE É O QUE IMPORTA. APRESENTE ESSE CUPOM EM SUA PRÓXIMA COMPRA E GANHE R$10 REAIS DE DESCONTO.")
else:
    # Cliente não qualificado
    print("OBRIGADO POR ESCOLHER A MINHA FARMA. VOCÊ SABIA QUE COMPRAS ACIMA DE R$100 REAIS GERAM UM VOUCHER DE R$10 REAIS DE DESCONTO PARA A PRÓXIMA COMPRA?")