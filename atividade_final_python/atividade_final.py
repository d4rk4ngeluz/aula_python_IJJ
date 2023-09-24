import requests
import json

# URL da API
url1 = "http://apilivro.jogajuntoinstituto.org/authors/"
url2 = "http://apilivro.jogajuntoinstituto.org/genders/"
url3 = "http://apilivro.jogajuntoinstituto.org/books/"

# Dados dos autores para cadastro
autores = [
    {"name": "Renato Fabricio"},
    {"name": "Josie Guedes"},
    {"name": "Kate Batista"},
    {"name": "Ester Carvalho"}
]

# Dados dos gêneros para cadastro
generos = [
    {"name": "Ficção"},
    {"name": "Aventura"},
    {"name": "Romance"},
    {"name": "Comédia"}
]

# Dados dos livros para cadastro
livros = [
    {"title": "QAme of Thrones"},
    {"title": "Indiana Python"},
    {"title": "O python é das estrelas"},
    {"title": "Corram que o Python vem aí"}
]


# Cadastrando os autores
for authors in autores:
    response = requests.post(f'{url1}', data=authors)
    if response.status_code == 201:
        print(f"Autor {authors} cadastrado com sucesso!")
    else:
        print(f"Erro ao cadastrar o autor {authors}. Resposta: {response.text}")

# Cadastrando os gêneros
for genders in generos:
    response = requests.post(f'{url2}', data=genders)
    if response.status_code == 201:
        print(f"Gênero {genders} cadastrado com sucesso!")
    else:
        print(f"Erro ao cadastrar o gênero {genders}. Resposta: {response.text}")


# Cadastrando os livros
for books in livros:
    response = requests.post(f'{url3}', data=books)
    if response.status_code == 201:
        print(f"Livro {books['title']} cadastrado com sucesso!")
    else:
        print(f"Erro ao cadastrar o livro {books['title']}. Resposta: {response.text}")

#

# Fazendo uma requisição GET para verificar os livros cadastrados
response = requests.get(f'{url3}')
if response.status_code == 200:
    livros_cadastrados = response.text
    print(f"Resposta: {livros_cadastrados}")
    if livros_cadastrados:
        try:
            livros_cadastrados = json.loads(livros_cadastrados)
            for livro in livros_cadastrados:
                response2 = requests.get(f'{url1}'+ str(livro['author']))
                print(f"Título: {livro['title']}, Autor: {response2.json()['name']}, Gênero: {livro['gender']}")
        except json.JSONDecodeError:
            print("Erro ao decodificar a resposta em JSON.")
    else:
        print("A resposta está vazia.")
else:
    print(f"Erro ao buscar os livros cadastrados. Resposta: {response.text}")