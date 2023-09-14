import pandas as pd

data = {
    'Nome': ["João", "Marta", "Ary", "Matheus", "Michelle"],
    'Idade': [51, 37, 23, 24, 33],
}

df = pd.DataFrame(data)

print(df[df['Idade']>30])