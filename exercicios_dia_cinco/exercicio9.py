# Exercício: crie um programa que recebe 15 valores e armazena em uma lista, e no final da execução mostre os valores da lista do último para o primeiro.

'''
Solução: existem diversas formas de fazer este exercício. Há algum tempo, fiz um curso de Python na Udemy ("The Modern Python 3 Bootcamp", do instrutor Colt Steele). Decidi
consultar minhas notas do curso para ver se existem métodos mais diretos de realizar uma operação como esta e, naturalmente, me deparei com duas formas simples: através da operação
de slicing (lista[start, end, step]) ou da função reverse(). Porém, decidi deixar essas opções comentadas no final do arquivo e desenvolver o exercício com base em dois loops for.
O primeiro pede que o usuário insira 15 valores que serão armazenados na lista "lista_valores" através da função append() (todos os valores serão armazenados em formato de string, 
portanto podem ser palavras, frases, números, etc.). 

Em seguida, a variável "contador" é criada com o valor inicial de -1 (uma vez que o último valor de uma lista se encontra na posição -1). Outro loop for é criado para adicionar 
os valores da "lista_valores" à "lista_contrario", porém de forma que esses valores são passados do último para o primeiro através de uma iteração com índices negativos 
(-1, -2, -3,..., 0). 
'''

lista_valores = []

for i in range(15):
    num = input("Insira o " + str(i+1) + "o valor na lista: ")
    lista_valores.append(num)

lista_contrario = []
contador = -1

for valor in lista_valores:
    lista_contrario.append(lista_valores[contador])
    contador -= 1

print(lista_contrario)    

'''
Possível solução através da operação de slicing:
print(lista_valores[-1:0:-1])
'''

'''
Possível solução através da função reverse():
lista_valores.reverse()
print(lista_valores)
'''