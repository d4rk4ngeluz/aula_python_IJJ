# Filtre as pessoas levando em consideração os seguintes critérios:

#     com idade maior que 40 anos
#     com renda maior de 5 mil
#     com renda maior de 15 mil

import pandas as pd

# df2 = pd.read_csv("dados_ficticios.csv")
# print()
# print(df2)


df2 = pd.read_csv("dados_ficticios.csv")
print(df2[df2['idade'] > 40])
print("-"*30)
print(df2[df2['renda'] > 5000])
print("-"*30)
print(df2[df2['renda'] > 15000])