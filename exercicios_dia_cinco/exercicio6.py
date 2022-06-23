# Construa um programa que receba uma valor inteiro maior que 2 em uma variavel x e apresenta os impares entre 0 e x

x = int(input("Digite um número maior que 2: "))

while not x > 2:
    print("\nO número precisa ser maior que 2! ")
    x = int(input("Digite um número: "))

print(f"\nOs números ímpares entre 0 e {x} são: ")

for num in range(x):
    if num % 2 != 0:
        print(num)
