while True:
    resposta = input("Pediu desculpas pela merda que fez? (S/N): ")
    if resposta.lower() == "s":
        print("Teve humildade de assumir o erro, siga em frente!")
        break
    elif resposta.lower() == "n":
        print("Não se arrependeu, volte para o início e tente novamente!")
    else:
        print("Resposta inválida. Por favor, responda com  's' para 'sim' ou 'n' para 'não'.")