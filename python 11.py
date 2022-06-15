# Declarando as matrizes:
matriz_a = [[1, 2], [3, 4]]
matriz_b = [[5, 6], [7, 8]]
matriz_c = [[0, 0], [0, 0]]

# Preenchendo as matrizes:
for i in range(0, 2):

    # Calculando dados:
    for j in range(0, 2):
        matriz_c[i][j] = matriz_a[i][j] + matriz_b[i][j]

# Imprimindo resultados:
for i in range(0, 2):
    for j in range(0, 2):
        print(f'{matriz_c[i][j]:^5}', end='')
    print()
