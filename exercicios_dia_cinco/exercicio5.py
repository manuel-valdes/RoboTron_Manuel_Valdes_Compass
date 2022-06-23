# Exercício: construa um programa que recebe 20 valores para X e no final apresenta a média aritmética dos valores pares digitados.

'''
Solução: criação de uma lista vazia (lista_pares) que receberá (através do método append) os valores pares encontrados nos inputs do usuário realizados no alcance do loop for. 
Neste, estabeleceu-se o limite indicado de 20 valores através da função range. Por fim, a média foi calculada através da soma de todos os números na lista (por meio da função
sum()) dividida pelo comprimento da lista (por meio da função len()). Novamente aplicou-se a função round() para facilitar a leitura do resultado.
'''

lista_pares = []

for i in range(20):
    num = int(input("Digite o " + str(i+1) +  " número: "))
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        pass

media = sum(lista_pares) / len(lista_pares)

print(round(media, 2))