# frequencia = 0
# dias_consecutivos = 0

# while True:
#     input("Pressione Enter para simular a passagem na catraca (ou 'q' para sair): ")
#     frequencia += 1
#     dias_consecutivos += 1

#     mensagem = "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"

#     if frequencia == 21:
#         mensagem = "UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ."
#         dias_consecutivos = 21
#     elif dias_consecutivos > 1:
#         mensagem = "QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO."
#         dias_consecutivos = 0

#     print(mensagem)

#     if input("Deseja sair? (Digite 'sair' para sair, Enter para continuar): ").lower() == 'sair':
#         break

# dias_consecutivos = 0

# while True:
#     input("Pressione Enter para simular a passagem na catraca (ou 'q' para sair): ")
#     dias_consecutivos += 1

#     mensagem = "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"

#     if dias_consecutivos == 21:
#         mensagem = "UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ."
#         dias_consecutivos = 0
#     elif dias_consecutivos > 1:
#         mensagem = "QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO."
#         dias_consecutivos = 0

#     print(mensagem)

#     if input("Deseja sair? (Digite 'sair' para sair, Enter para continuar): ").lower() == 'sair':
#         break

dias_consecutivos = 0

while dias_consecutivos < 21:
    input("Pressione Enter para simular a passagem na catraca (ou 'q' para sair): ")
    dias_consecutivos += 1

    if dias_consecutivos == 21:
        print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ.")
    else:
        print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")

    if input("Deseja sair? (Digite 'q' para sair, Enter para continuar): ").lower() == 'q':
        break

    # Reinicie a contagem se o aluno perder um dia
    if input("Você perdeu um dia? (Digite 's' para sim, Enter para não): ").lower() == 's':
        dias_consecutivos = 0
