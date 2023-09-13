# Agora crie um script para com uma lista de frutas, 
# Outra lista com o nome alergias. Informação confusa!!!#

# Insira uma fruta da lista de frutas na lista de alergias. 
# Depois crie um for para cada item da lista passar por uma 
# verificação em uma estrutura condicional para verificar se está essa fruta está contida na lista de alergias.
# Caso a fruta esteja na lista, imprima na tela o nome dela. 

frutas = ["maçã", "uva","tangerina", "laranja", "morango"]
alergias = ["melancia","mamão", "manga", "laranja"]

# #Insersão da fruta na lista de alergias
# alergias.append(frutas[3])

for fruta in frutas:
    if fruta in alergias:
        print(fruta)