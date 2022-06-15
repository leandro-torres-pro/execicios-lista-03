# Declarando variáveis:
idade = []
idade_inv = []
altura = []
altura_inv = []

# Declarando variáveis de controle:
n = 0
i = 0

# Solicitando dados:
for i in range(0, 5, 1):
    n += 1
    idade += input(f"Digite a idade da {n}º pessoa: ")
    altura += input(f"Digite a altura da {n} pessoa: ")

    # Reorganizando dados em ordem inversa:
while i >= 0:
    idade_inv += idade[i]
    altura_inv += altura[i]
    i -= 1

    # Imprimindo resultados:
print(f'Idade em ordem inversa: {idade_inv}'.replace(",", '').replace("[", '').replace("'", ''))
print(f'Altura em ordem inversa: {altura_inv}'.replace(",", '').replace("[", '').replace("'", ''))
