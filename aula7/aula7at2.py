# import os

# # Criando uma lista de dados
# dados = ['Renato', 'Josie', 'Ester', 'Katie', 'Python', 'OS']

# # Criando uma nova pasta
# pasta = "~/D:/AulaPython"
# os.makedirs(pasta, exist_ok=True)

# # Criando e escrevendo em um arquivo .txt
# with open(os.path.join(pasta, 'arquivo.txt'), 'w') as f:
#     for dado in dados:
#         f.write(f'{dado}\n')

# TODO

# DESAFIO DO CAIQUE

# Vamos explorar o poder da biblioteca OS! Prepare-se para mergulhar no mundo da interação entre o Python e o seu sistema operacional. Vamos aprender a usar a biblioteca OS em conjunto com funções nativas do Python para criar algo.

# O desafio é o seguinte: você vai criar uma lista de dados e, usando a biblioteca OS, interagir com o seu sistema operacional. Além disso, também criará uma nova pasta para salvar o arquivo de texto txt.

# O que é a biblioteca OS?

# A biblioteca OS (Operating System) em Python é como um conjunto de ferramentas que ajuda o seu programa a interagir com o sistema operacional do computador, como o Windows, o macOS ou o Linux. Ela permite que você faça coisas como criar, copiar, mover ou apagar arquivos e pastas, além de muitas outras tarefas relacionadas ao sistema.

# Passo 1: Importar a biblioteca OS
# import os

# # Passo 2: Criar uma lista de dados
# dados = ["Maçã", "Banana", "Laranja", "Morango", "Uva"]

# # Passo 3: Criar uma nova pasta

# # Caminho para a pasta na área de trabalho
# pasta_jogajunto = os.path.expanduser("~/documentos/dados")
# os.mkdir(pasta_jogajunto)

# # Passo 4: Criar e salvar o arquivo de texto (.txt)

# # Caminho completo para o arquivo
# # caminho_arquivo = os.path.join(pasta_jogajunto, "lista_de_dados.txt")
# # with open(caminho_arquivo, "w") as arquivo:
# #     for item in dados:
# #         arquivo.write(item + "\n")

import os

# Passo 2: Criar uma lista de dados
dados = ["Maçã", "Banana", "Laranja", "Morango", "Uva"]

# Passo 3: Definir o caminho da pasta
# Caminho para a pasta na área de trabalho
pasta_destino = os.path.expanduser("~/Desktop/dados")

# Verificar se a pasta já existe
if not os.path.exists(pasta_destino):
    os.mkdir(pasta_destino)  # Criar a pasta se ela não existir

# Passo 4: Criar e salvar o arquivo de texto (.txt)
# Caminho completo para o arquivo
caminho_arquivo = os.path.join(pasta_destino, "lista_de_dados.txt")
with open(caminho_arquivo, "w") as arquivo:
    for item in dados:
        arquivo.write(item + "\n")

print(dados)