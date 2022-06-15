# Determinando função:
def calcula_situ(termo_n1):
    if termo_n1 <= 0:
        resp = "N"
    else:
        resp = 'P'
    return resp


# Calculando:
s = calcula_situ(int(input('Digite um argumento numérico: ')))

# Imprimindo resultado:
print(s)
