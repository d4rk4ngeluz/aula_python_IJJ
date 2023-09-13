# def soma(n1, n2):
#     resultado = n1 + n2
#     # print(resultado)
#     return resultado   

# def transformar_maiusculo(palavra):
#     return palavra.upper()

# resultado1 = soma(1,2)

# print(resultado1)

# cidade = 'salvador'
# print(cidade)
# palavra_maiuscula = transformar_maiusculo(cidade)
# print(palavra_maiuscula)

import requests


def descobrir_bairro(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    
    data = response.json()
    bairro = data['bairro']

    return bairro


squad = {
    "Ester": "03881170",
    "Renato": "40325390",
    "Katie": "54310250",
    "Josie": "58078375"

}
for nome, cep in squad.items():
    #print(f'{nome} e {cep}')
    bairro = descobrir_bairro(cep)
    print(f'{nome} mora em {bairro}')