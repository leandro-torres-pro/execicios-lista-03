# Declarando as variáveis:
numeros = [2, 4, 6, 8, 10]
soma = produto = 0

# Somando e multiplicando os valores:
for i in range(len(numeros)):
    if i < 1:
        soma += numeros[i]
        produto += numeros[i]
    elif i >= 1:
        soma += numeros[i]
        produto *= numeros[i]

# imprimindo os resultados:
print(f'Os cinco valores são: {numeros}'.replace("[", '').replace("]", ""))
print(f'A soma dos cinco valores são: {soma}')
print(f'O produto dos cinco valores são: {produto}')

