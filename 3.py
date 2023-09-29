def sao_bicondicionais(conjunto1, conjunto2):
    return conjunto1 == conjunto2

entrada_conjunto1 = input("Digite os elementos do primeiro conjunto separados por vírgula: ")
entrada_conjunto2 = input("Digite os elementos do segundo conjunto separados por vírgula: ")

conjunto1 = set(entrada_conjunto1.split(','))
conjunto2 = set(entrada_conjunto2.split(','))

bicondicionais = sao_bicondicionais(conjunto1, conjunto2)

if bicondicionais:
    print("Os conjuntos são bicondicionais (têm os mesmos elementos).")
else:
    print("Os conjuntos não são bicondicionais (não têm os mesmos elementos).")
