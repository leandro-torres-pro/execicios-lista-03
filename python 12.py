# Declarando matriz:
matriz_a = [[1, 2], [3, 4]]
matriz_b = [[5, 6], [7, 8]]
matriz_c = [[0, 0], [0, 0]]

# preenchendo matrizes e Formatando:
for i in range(len(matriz_a)):

    # Calculando matrizes:
    for j in range(len(matriz_a)):
        matriz_c[i][j] = matriz_a[i][j] * matriz_b[i][j]

# Imprimindo matrizes e formatação:
for i in range(0, 2):
    if i == 0:
        print(" Matriz A")
        print("=-"*5)
    for j in range(0, 2):
        print(f'{matriz_a[i][j]:^5}', end='')
    print()
for i in range(0, 2):
    if i == 0:
        print(" Matriz B")
        print("=-" * 5)
    for j in range(0, 2):
        print(f'{matriz_b[i][j]:^5}', end='')
    print()
for i in range(0, 2):
    if i == 0:
        print(" Produto entre Matriz A e B - Matriz C")
        print("=-" * 20)
    for j in range(0, 2):
        print(f'{matriz_c[i][j]:^5}', end='')
    print()
 
