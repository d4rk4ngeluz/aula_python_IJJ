nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
mes = 'JANEIRO'
n1 = float(input('Digite o sua 1 nota: '))
n2 = float(input('Digite o sua 2 nota: '))
n3 = float(input('Digite o sua 3 nota: '))
n4 = float(input('Digite o sua 4 nota: '))
soma = n1 + n2 + n3 + n4
media = soma / 4
print(f" O nome é: {nome} {sobrenome} a primeira nota é {n1} a segunda é {n2} a terceira nota é {n3} a quarta nota é {n4} a minha nota geral é {soma}")
print(f" Sua média é: {media}")