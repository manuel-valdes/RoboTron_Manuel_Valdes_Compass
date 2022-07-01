# Exercício: crie um programa que recebe uma lista com três frutas e compare com uma lista com os valores ["maça", "banana", "pera"].

'''
Solução: criação da lista inicial indicada (["maça", "banana", "pera"]) e criação de uma lista vazia à qual serão adicionadas as frutas indicadas pelo usuário através da função 
append() no primeiro loop for. No segundo loop, uma estrutura condicional compara se as frutas inseridas pelo usuário já estavam na lista inicial. Se for o caso, a mensagem 
"A fruta x já está na lista inicial! " é impressa. Caso contrário, o programa indica que a fruta "x" é uma nova adição. Para imprimir essas mensagens, utilizaram-se "f-strings",
que permitem adicionar diferentes tipos e variáveis em uma string de maneira mais simplificada. 
'''

lista_inicial = ["maça", "banana", "pera"]

lista_frutas = []

print()

for i in range(3):
    fruta = input("Digite o nome da " +str(i+1)+ "a fruta: ")
    lista_frutas.append(fruta)

print("-------------------------------------------------")

for fruta in lista_frutas:
    if fruta in lista_inicial:
        print(f"A fruta {fruta} já está na lista inicial! ")
    else:
        print(f"A fruta {fruta} foi adicionada à lista de novas frutas. ")

print()