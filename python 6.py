# Solicitando dados:
primeira_frase = str(input('Digite uma frase qualquer: ').upper())
segunda_frase = str(input('Digite outra frase qualquer: ').upper())
resp = []
difer_n1 = []
difer_n2 = []

# Frases diferentes em tamanho:
if len(primeira_frase) != len(segunda_frase):
    print(f'Primeira frase: "{primeira_frase}"')
    print(f'Segunda frase: "{segunda_frase}"')
    print(f'{primeira_frase}: tamanho: {len(primeira_frase)} caractere')
    print(f'{segunda_frase}: tamanho: {len(segunda_frase)} caractere')
    print('As duas frases são diferentes em tamanho.')
    print('As duas frases possuem conteúdos diferentes')

# frases iguais em tamanho:
else:

    # Analisando a frase, em relação ao conteúdo:
    for i in range(len(primeira_frase)):
        resp.append(primeira_frase[i] in segunda_frase[i])

        # Armazenando diferenças:
        if False in resp:
            difer_n1.append(primeira_frase[i])
            difer_n2.append(segunda_frase[i])
            resp[i] = True

    # Imprimindo resultados:
    print(f'Primeira frase: {primeira_frase}')
    print(f'segunda frase: {segunda_frase}')
    print(f'{primeira_frase}: tamanho: {len(primeira_frase)} caractere')
    print(f'{segunda_frase}: tamanho: {len(segunda_frase)} caractere')
    print('As duas frases são igual em tamanho.')
    for i in range(len(primeira_frase)):
        resp.append(primeira_frase[i] in segunda_frase[i])
    if False in resp:
        print(f'As frases são diferentes em conteúdo:{difer_n1} != {difer_n2} '.replace("[", '').replace(']', '').replace("'", '').replace(
            "'", ''))
    else:
        print(f'As frases são iguais em conteúdo:')
