# Exercício: construa um programa que recebe dois valores, soma esses valores e apresenta se o resultado é par ou impar.

'''
Solução: criação dos inputs que recebem os valores digitados pelo usuário e resultado da soma entre esses valores armazenado na variável "soma". Para responder
se a soma dos valores resulta num número par ou ímpar, aplicou-se o operador de modulação (%) numa estrutura condicional que imprimiria uma determinada mensagem
de acordo com seu resultado. O operador de modulação retorna o resto da divisão entre os valores indicados. No caso de um número par, o resultado de sua modulação
por 2 sempre é 0.
'''

primeiro_valor = int(input("\nDigite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

soma = primeiro_valor + segundo_valor

if soma % 2 == 0:
    print("\nA soma desses números gera um resultado par! \n")
else:
    print("\nA soma desses números gera um resultado ímpar! \n")