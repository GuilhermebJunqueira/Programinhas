def uniao(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

def intersecao(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

def diferenca(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

entrada_conjunto1 = input("Digite os elementos do primeiro conjunto separados por vírgula: ")
entrada_conjunto2 = input("Digite os elementos do segundo conjunto separados por vírgula: ")

conjunto1 = set(entrada_conjunto1.split(','))
conjunto2 = set(entrada_conjunto2.split(','))

print(f"União dos conjuntos: {uniao(conjunto1, conjunto2)}")
print(f"Interseção dos conjuntos: {intersecao(conjunto1, conjunto2)}")
print(f"Diferença (conjunto1 - conjunto2): {diferenca(conjunto1, conjunto2)}")

elemento_verificacao = input("Digite um elemento para verificar se pertence ao conjunto1: ")

if elemento_verificacao in conjunto1:
    print(f"{elemento_verificacao} pertence ao conjunto1.")
else:
    print(f"{elemento_verificacao} não pertence ao conjunto1.")
