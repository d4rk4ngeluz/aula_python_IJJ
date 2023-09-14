import pandas as pd

data = {
    'Nome': ["João", "Marta", "Ary", "Ester", "Josie", "Renato", "Katie",],
    'Idade': [51, 37, 23, 24, 33, 15, 23],
    'Cidade': ["Recife", "Recife", "Recife", "Salvador", "Salvador", "São Paulo", "Manaus"]
}

df = pd.DataFrame(data)

print(df[df['Cidade']=="Recife"])