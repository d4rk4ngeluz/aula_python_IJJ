import aula8at2

from aula8at2 import verificar_paridade

def verificar_paridade(numeros):
    for numero in numeros:
        if numero % 2 == 0:
            print(f'O número {numero} é par.')
        else:
            print(f'O número {numero} é ímpar.')

numeros_matricula = []
while len(numeros_matricula) < 5:
    numero = int(input('Insira um número de matrícula: '))
    numeros_matricula.append(numero)

verificar_paridade(numeros_matricula)