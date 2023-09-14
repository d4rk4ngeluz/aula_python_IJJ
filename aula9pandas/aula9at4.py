import pandas as pd

df = pd.read_csv("dados_ficticios.csv")

for i, linha in df.iterrows():
    print(linha["nome"], linha ["renda"])