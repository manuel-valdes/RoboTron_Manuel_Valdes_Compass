'''
Exercício: construa um programa que armazena uma idade em uma váriavel e compara, se a idade for maior que 18, apresenta "Maior de idade", se a idade for menor 
que 12, apresenta "Você é uma criança" e se for maior que 12 e menor que 18, apresenta "Você é um adolescente".
'''

'''
Solução: criação de um input que recebe a idade indicada pelo usuário. Essa idade passa por uma estrutura condicional que imprime mensagens diferentes de acordo
com seu valor. No caso, escolhi considerar que idades maiores ou IGUAIS a 18 imprimiriam o texto "Maior de idade", uma vez que a partir dos 18 anos a pessoa já é
considerada adulta. A mesma lógica foi aplicada em relação a pessoas com idade a partir de 12 anos.
'''

idade = int(input("\nDigite sua idade: "))

if idade >= 18:
    print("\nMaior de idade\n")
elif idade >= 12 and idade < 18:
    print("\nVocê é um adolescente\n")
else:
    print("\nVocê é uma criança\n")