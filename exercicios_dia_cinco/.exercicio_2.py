# Exercício: construa um programa que armazena em duas variáveis duas notas e apresenta a média entre as duas.

'''
Solução: criação das duas variáveis e atribuição do tipo float aos seus inputs, uma vez que notas podem conter valores decimais. Por fim, criação da variável
"media", que executa a soma das notas e sua divisão por 2 (número de elementos considerados no cálculo desta média). Também optei pela aplicação da função round()
para facilitar a leitura do resultado. Embora o exercício pedisse para armazenar as notas nas variáveis, preferi criá-las como inputs para deixar o programa
um pouco mais dinâmico.

'''

primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))

media = round(((primeira_nota + segunda_nota)/2), 2)

print("A média é", media)