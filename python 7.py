# Solicitando dados:
nome = str(input("Digite seu nome: ").upper().replace(" ", ''))
nome_for = []

# Formatando formato:
for i in range(1, len(nome) + 1, 1):

    # Armazenando dados formatados:
    nome_for.append(nome[-i])

# imprimindo dados:
print(f"Nome em ordem inversa: {nome_for}".replace("['", '').replace("']", '').replace("', '", ''))
