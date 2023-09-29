def diferenca_simetrica(conjunto1, conjunto2):
    return conjunto1.symmetric_difference(conjunto2)

def reverter_diferenca_simetrica(diferenca_simetrica, conjunto_original):
    return diferenca_simetrica.symmetric_difference(conjunto_original)

entrada_conjunto1 = input("Digite os elementos do primeiro conjunto separados por vírgula: ")
entrada_conjunto2 = input("Digite os elementos do segundo conjunto separados por vírgula: ")

conjunto1 = set(entrada_conjunto1.split(','))
conjunto2 = set(entrada_conjunto2.split(','))

diferenca = diferenca_simetrica(conjunto1, conjunto2)

print(f"Diferença Simétrica entre os conjuntos: {diferenca}")

conjunto_original = reverter_diferenca_simetrica(diferenca, conjunto1)

print(f"Conjunto original após a reversão: {conjunto_original}")
