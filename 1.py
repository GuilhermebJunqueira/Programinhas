def uniao_conjuntos(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

entrada_conjunto1 = input("Digite os elementos do primeiro conjunto separados por vírgula: ")
entrada_conjunto2 = input("Digite os elementos do segundo conjunto separados por vírgula: ")

conjunto1 = set(entrada_conjunto1.split(','))
conjunto2 = set(entrada_conjunto2.split(','))

resultado_uniao = uniao_conjuntos(conjunto1, conjunto2)

print(f"A união dos conjuntos é: {resultado_uniao}")
