# Primeiro, criar uma função que determine se um número é par ou ímpar.
def verificar_paridade(numero):
    if numero % 2 == 0:
        return "VOCÊ ESTÁ NO TIME AZUL"
    else:
        return "VOCÊ ESTÁ NO TIME AMARELO"


# Segundo, solicita que o usuário insira o número da matrícula
numero_matricula = int(input("Digite o número da matrícula: "))

# Terceiro, chama a função para verificar a paridade e imprime a mensagem
mensagem = verificar_paridade(numero_matricula)
print(mensagem)