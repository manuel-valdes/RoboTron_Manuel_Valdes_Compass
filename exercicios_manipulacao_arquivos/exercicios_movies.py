# Exercício 8: abra o arquivo CSV com pandas e guarde em uma variável de sua escolha e printe o conteúdo no terminal.

'''
Solução: 
'''

import pandas as pd
import pprint

print("\nExercício 8:\n")

filmes = pd.read_csv('exercicios_manipulacao_arquivos/_movies.csv', encoding='UTF-8', sep=',')
pprint.pprint(filmes)

# Função criada simplesmente para separar os resultados no terminal, deixando a leitura dos dados mais acessível:

def separa_dados():
    separador = ("-------------"*14)
    print("\n", separador)

separa_dados()

# Exercício 9: usando Pandas, leia apenas os dados da coluna Age do CSV.

'''
Solução: 
'''

print("\nExercício 9:\n")

idade_atores = (filmes[['Age']])
print(idade_atores)

separa_dados()

# Exercício 10: usando Pandas, procure por um dado específico (da sua escolha) e printe somente o mesmo utilizando o CSV.

'''
Solução: 
'''

print("\nExercício 10:\n")

vencedores_idosos = filmes["Name"][filmes["Age"] >= 60]
print(vencedores_idosos.to_string(index=True))

separa_dados()

'''
Usei a função .to_string(index=True) porque, ao printar, aparecia a seguinte mensagem logo ao final da lista: "Name: Name, dtype: object". Pesquisei o que ela significava e me deparei
com um post do StackOverflow que explicava como era possível fazer com que ela não printasse junto com os resultados, no caso, era através da aplicação dessa função. Decidi aplicá-la
em -quase- todos os casos em que isso acontecia deste exercício para a frente, com a exceção de um em que a função acabava atrapalhando a formatação dos resultados. A ideia é de 
simplesmente facilitar a leitura dos dados através de uma apresentação visualmente mais limpa.

Link para a postagem do StackOverflow: https://stackoverflow.com/questions/29645153/remove-name-dtype-from-pandas-output-of-dataframe-or-series
'''

# Exercício 11: printe o nome do Ator que ganhou o Oscar em 1993.

'''
Solução:
'''

print("\nExercício 11:\n")

vencedor_1993 = filmes["Name"][filmes["Year"] == 1993]
print(vencedor_1993.to_string(index=True))

separa_dados()

# Exercício 12: printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016.

'''
Solução:
'''

print("\nExercício 12:\n")

vencedores = filmes.iloc[[63, 88]]
print(vencedores["Name"].to_string(index=True))

separa_dados()

# Exercício 13: Crie mais uma coluna em tempo de execução juntando os dados movie e year.

'''
Solução:
'''

print("\nExercício 13:\n")

filmes["Ano/Filme"] = filmes["Movie"] + "    " + filmes["Year"].apply(str)
pprint.pprint(filmes["Ano/Filme"])

separa_dados()

# Exercício 14: printe todos os nomes e as idades dos atores que ganharam o oscar de 1987 até 1999.

'''
Solução: 
'''

print("\nExercício 14:\n")

todos_vencedores = filmes.iloc[59:72, :]
print(todos_vencedores)

separa_dados()

# Exercício 15: mostre todos os filmes menos o “The Revenant”.

'''
Solução: 
'''

print("\nExercício 15:\n")

no_revenant = filmes.drop(filmes.iloc[[88]].index)
print(no_revenant)

separa_dados()