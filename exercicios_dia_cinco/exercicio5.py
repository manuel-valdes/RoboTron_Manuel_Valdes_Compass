# Construa um programa que recebe 20 valores para X e no final apresenta a média aritmética dos valores pares digitados

lista_pares = []

for i in range(20):
    num = int(input("Digite o " + str(i+1) +  " número: "))
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        pass

media = sum(lista_pares) / len(lista_pares)

print(round(media, 2))