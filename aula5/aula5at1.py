idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Parabéns você está apto para tirar sua habilitação")

elif idade >= 17 and idade < 18:
    print("Você ainda não está apto a dirigir")

else:
    print("Você não possuem idade mínima para dirigir")