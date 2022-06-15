def somaImposto(taxaImposto, custo):
    custo = custo * (taxaImposto/100)
    return custo


venda = somaImposto(float(input('Digite a taxa de imposto: ')), float(input('Digite o custo: ')))
print(venda)

