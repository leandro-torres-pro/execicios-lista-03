# Solicitando dados:
numero = int(input("digite um numero: "))
numero_for = []

# Formatando formato:
for i in range(numero):

    # Armazenando dados formatados:
    numero_for.append(i + 1)

    # Imprimindo dodos:
    print(f'{numero_for}'.replace("[", '').replace("]", '').replace(",", ' '))