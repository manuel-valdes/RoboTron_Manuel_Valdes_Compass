# Exercício: crie um programa que contém uma função que receba dois parâmetros inteiros e retorna a média dos dois valores.

'''
Solução: a função "calcula_media" tem dois parâmetros. Quando chamada, ela realiza a média entre os valores indicados pelo usuário no momento em que ele executa 
a função. Esse valor então é retornado pela função.
'''

def calcula_media(primeiro_num, segundo_num):
    media = (primeiro_num + segundo_num) / 2
    return media 

'''
Para visualizar o resultado dessa operação, o usuário poderia realizar um comando parecido este:

print(calcula_media(10, 20))

Nesse caso, o console imprimiria a média entre os parâmetros (10 e 20) indicados pelo usuário.
'''