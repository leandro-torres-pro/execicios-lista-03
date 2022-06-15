# Declarando função:
def dataExtensa(dia, mes, ano):

    # Preenchendo dados dos meses:
    mes_ext = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", 'Setembro', "Outubro",
               'Novembro', 'Dezembro']

    # Formatando resposta:
    if mes or dia > 12 or dia or mes < 1:
        return print("NULL")
    else:
        return print(f'Data: Dia {dia}, de {mes_ext[mes]} de {ano} ')

# Imprimindo resultado:
print(dataExtensa(int(input('Dia: ')), int(input('Mês: ')), int(input('Ano: '))), end='')
