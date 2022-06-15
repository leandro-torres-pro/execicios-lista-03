# Solicitando dados:
nome = str(input("Digite seu nome: ").upper().replace(" ", ''))
nome_for = []

# Formatando formato:
for i in range(len(nome)):

    # Armazenando dados formatados:
    nome_for.append(nome[i])

    # Imprimindo dodos:
    print(f'{nome_for}'.replace("['", '').replace("']", '').replace("', '", ''))