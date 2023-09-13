# import requests

# def checar_frete_gratis(cep):
#     response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
#     data = response.json()
#     if 'erro' in data:
#         return "CEP inválido"
#     else:
#         estado = data['uf']
#         if estado in ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO', 'AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']:
#             return (f'Frete grátis disponível para seu estado {estado}!')
#         else:
#             return (f'Frete grátis indisponível para seu estado {estado}!')

# cep = input("Insira seu CEP: ")
# print(checar_frete_gratis(cep))

import requests

def verifica_frete_gratis(cep):
    estados_frete_gratis = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO', 'AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = response.json()
    if 'erro' in data:
        return "CEP inválido"
    else:
        estado = data['uf']
        if estado in estados_frete_gratis:
            return (f'Frete grátis disponível para seu estado {estado}!')
        else:
            return (f'Frete grátis indisponível para seu estado {estado}!')

cep = input("Insira seu CEP: ")
print(verifica_frete_gratis(cep))