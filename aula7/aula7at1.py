import requests

squad = {
    "Ester": "03881170",
    "Renato": "40325390",
    "Katie": "54310250",
    "Josie": "58078375"

}
for nome, cep in squad.items():
    #print(f'{nome} e {cep}')

    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    
    data = response.json()
    cidade = data['localidade']
    print(f'{nome} mora em {cidade}')

response = requests.get('https://viacep.com.br/ws/01001000/json/')
data = response.json()

print()