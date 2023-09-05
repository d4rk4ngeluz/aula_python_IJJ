valor_compra = float(input("Informe o valor da compra: R$ "))

# Verificar 30% de Desconto
if valor_compra >= 500:
    print("PARABÉNS!!! VOCÊ GANHOU SUPER DESCONTO DE 30% NA FASHIONSTYLE!")
# Verificar 10% de Desconto
elif valor_compra >= 250 and valor_compra < 500:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")
# Verificar não tem Desconto
else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA")