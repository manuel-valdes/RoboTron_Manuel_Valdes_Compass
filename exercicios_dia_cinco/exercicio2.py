#Construa um programa que armazena em duas variáveis duas notas e apresenta a média entre as duas

primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))

media = round(((primeira_nota + segunda_nota)/2), 2)

print("A média é ", media)