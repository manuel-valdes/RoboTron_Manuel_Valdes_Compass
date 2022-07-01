# Exercício 8: abra o arquivo CSV com pandas e guarde em uma variável de sua escolha e printe o conteúdo no terminal.

'''
Solução: de maneira similar aos exercícios envolvendo arquivos .json, é necessário importar a biblioteca Pandas para poder manipular dados de acordo com seus métodos. A variável "pd"
é simplesmente uma maneira mais curta de chamar a biblioteca. A função ".read_csv" permite ler o arquivo e armazenas seus dados em uma variável, no caso, "filmes_df".
'''

import pandas as pd
import pprint

print("\nExercício 8:\n")

filmes_df = pd.read_csv('_movies.csv', encoding='UTF-8', sep=',')
pprint.pprint(filmes_df)

# Função criada simplesmente para separar os resultados no terminal, deixando a leitura dos dados mais acessível:

def separa_dados():
    separador = ("-------------"*14)
    print("\n", separador)

separa_dados()

# Exercício 9: usando Pandas, leia apenas os dados da coluna Age do CSV.

'''
Solução: para ler os dados de uma coluna específica, o comando seria indicar a coluna entre [[]]. Eu decidi armazenar esses valores dentro de uma variável própria e, em seguida,
imprimi-la.
'''

print("\nExercício 9:\n")

idade_atores = (filmes_df[['Age']])
print(idade_atores)

separa_dados()

# Exercício 10: usando Pandas, procure por um dado específico (da sua escolha) e printe somente o mesmo utilizando o CSV.

'''
Solução: escolhi armazenar todos os atores que venceram o Oscar com idade maior ou igual a 60 anos e armazená-los na variável "vencedores_idosos". Para isso, indiquei que queria
receber a coluna "Name" da base de dados filtrada por meio daqueles que tem "Age" maior ou igual a 60.
'''

print("\nExercício 10:\n")

vencedores_idosos = filmes_df["Name"][filmes_df["Age"] >= 60]
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
Solução: indiquei que queria receber a coluna "Name" das linhas da base de dados que tinham na coluna "Year" o valor 1993. Armazenei esses dados em uma variável e a printei.
'''

print("\nExercício 11:\n")

vencedor_1993 = filmes_df["Name"][filmes_df["Year"] == 1993]
print(vencedor_1993.to_string(index=True))

separa_dados()

# Exercício 12: printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016.

'''
Solução: neste caso, usei o indexador .iloc[] que permite encontrar linhas com base em seu id. Em seguida, no momento de printar, estabeleci que queria que apenas a coluna "Name"
fosse impressa.
'''

print("\nExercício 12:\n")

vencedores = filmes_df.iloc[[63, 88]]
print(vencedores["Name"].to_string(index=True))

separa_dados()

# Exercício 13: Crie mais uma coluna em tempo de execução juntando os dados movie e year.

'''
Solução: simples concatenação de colunas. Usei o método .apply(str) para mudar o tipo de dado da coluna "Year", caso contrário ela não realizaria a operação pelo fato do Python ser
uma linguagem de tipagem forte, ou seja, não realiza conversões de tipo automaticamente.
'''

print("\nExercício 13:\n")

filmes_df["Filme/Ano"] = filmes_df["Movie"] + "    " + filmes_df["Year"].apply(str)
pprint.pprint(filmes_df["Filme/Ano"])

separa_dados()

# Exercício 14: printe todos os nomes e as idades dos atores que ganharam o oscar de 1987 até 1999.

'''
Solução: novamente, aplicação do indexador .iloc[], porém desta vez estabelecendo um range de atuação por id's. Depois da vírgula, o : indica que todas as colunas devem ser levadas
em consideração.
'''

print("\nExercício 14:\n")

todos_vencedores = filmes_df.iloc[59:72, :]
print(todos_vencedores)

separa_dados()

# Exercício 15: mostre todos os filmes menos o “The Revenant”.

'''
Solução: a função .drop() serve para desconsiderar um dado da lista e, novamente, através do indexador .iloc[], consegui indicar qual seria a linha a ser desconsiderada. 
'''

print("\nExercício 15:\n")

no_revenant = filmes_df.drop(filmes_df.iloc[[88]].index)
print(no_revenant)

separa_dados()