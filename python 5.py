# Declarando variáveis:
primeira = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
segunda = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
terceira = []

#  Reorganizando os dados em alternância:
for i in range(len(primeira)):
    terceira.append(primeira[i])
    terceira.append(segunda[i])

# Imprimindo resultado:
print(f'O resultado da reorganização das duas lista é {terceira}'.replace('[', '').replace(',', ''))
