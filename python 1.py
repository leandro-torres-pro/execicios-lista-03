# Declarando variáveis:
num_alunos = 10
nome = []
nota = []
n1 = media = n_e = notat = 0

# Solicitando os nomes e as notas:
for i in range(num_alunos):
    n1 += 1
    media = notat = 0

    # Solicitando os nomes dos alunos:
    nome1 = str(input(f'Digite o nome do {n1}º aluno: '))
    nome_vari = nome1

    # Solicitando as quatro notas de cada aluno:
    for e in range(0, 4, 1):
        n_e += 1
        nota1 = float(input(f'Digite a {n_e}º nota do aluno(a) {nome_vari}: '))

        # Calculando e armazenado a media:
        notat = notat + nota1
    media = notat / 4

    # Separando alunos, segundo a media:
    if media >= 7:
        nome.append(nome1)
        nota.append(media)

# Imprimindo os nomes e notas dos alunos que ficaram acima ou igual a media:
for a in range(len(nome)):
    print(f"{nome[a], nota[a]}".replace("'", '').replace("'", '')
          .replace("[", '').replace("]", '').replace("(", '')
          .replace(")", '').replace(",", ':').replace(",", ':'))
