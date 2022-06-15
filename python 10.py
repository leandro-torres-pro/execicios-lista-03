# Declarando matriz, variável de controle:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
k = 2

# Preenchendo matriz:
for i in range(0, 3):
    for j in range(0, 3):

        # Solicitando dados:
        matriz[i][j] = int(input(f'Digite um valor para [{i}] [{j}]: '))

# Calculando valores da matriz:
for i in range(0, 3):
    matriz[i][i] = matriz[i][i] * k

    # Imprimindo dados da matriz em forma correta:
    for j in range(0, 3):
        print(f'{matriz[i][j]:^5}', end='')
    print()
