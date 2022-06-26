# Exercício: construa um programa que receba uma valor inteiro maior que 2 em uma variavel x e apresenta os impares entre 0 e x.

'''
Solução: a variável "x" espera receber um valor inteiro. Enquanto o valor inserido pelo usuário for menor ou igual a 2, o loop while fará com que ele repita a ação.
Indicado um número válido, o programa vai para um loop for estabelecido no range do número indicado. A operação de modulação indica quais números no intervalo entre
0 e x são ímpares. Estes serão impressos.
'''

x = int(input("Digite um número maior que 2: "))

while not x > 2:
    print("\nO número precisa ser maior que 2! ")
    x = int(input("Digite um número maior que 2: "))

print(f"\nOs números ímpares entre 0 e {x} são: ")

for num in range(x):
    if num % 2 != 0:
        print(num)
