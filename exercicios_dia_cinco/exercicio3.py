# Construa um programa que recebe dois valores, soma esses valores e apresenta se o resultado é par ou impar

primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

soma = primeiro_valor + segundo_valor

if soma % 2 == 0:
    print("A soma desses números gera um resultado par! ")
else:
    print("A soma desses números gera um resultado ímpar! ")