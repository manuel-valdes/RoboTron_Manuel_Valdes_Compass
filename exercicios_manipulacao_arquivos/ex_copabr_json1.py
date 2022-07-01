# Exercício 1: baixe o arquivo do link JSON 1, abra ele no vsCode com Python nomeando-o como partida guarde em uma variável e printe o JSON inteiro no terminal.

'''
Solução: criação da função "retornar_json", armazenada na variável "chamar_json". Essa função será usada ao longo de todos os exercícios para interagir com o arquivo .json. A função
open() permite ler o conteúdo do arquivo em questão e a função load() de certa forma "traz" o conteúdo para a variável indicada. Para interagir com os arquivos .json é necessário
importar a biblioteca através do comando "import json". Decidi também importar a biblioteca pprint para printar os dados de maneira mais esteticamente agradável.
'''

import json
import pprint

print("\nExercício 1:\n")

def retornar_json():
    with open("_copa_do_brasil.json", encoding="UTF-8") as partida:
        dados_partida = json.load(partida)
        return dados_partida

chamar_json = retornar_json()
pprint.pprint(chamar_json)

# Função criada simplesmente para separar os resultados no terminal, deixando a leitura dos dados mais acessível:

def separa_dados():
    separador = ("-------------"*14)
    print("\n", separador)

separa_dados()

# Exercício 2: pegue o arquivo JSON 1 e printe apenas o nome do time vencedor no terminal.

'''
Solução: simples indicação do caminho a ser seguido para encontrar o nome do time vencedor. Como ele está localizado dentro do dicionário "time_mandante", que por sua vez se encontra
dentro da lista "copa-do-brasil", é necessário indicar a direção passo a passo.
'''

print("\nExercício 2:\n")

time_vencedor = chamar_json['copa-do-brasil'][0]['time_mandante']['nome_popular']
pprint.pprint(time_vencedor)

separa_dados()

# Exercício 3: do JSON 1 guarde apenas o Nome do Estádio, o Placar e o Status do jogo dentro de variáveis e mostre-as.

'''
Solução: resolvido da mesma forma que o exercício anterior, porém em mais de um caso.
'''

print("\nExercício 3:\n")

nome_estadio = chamar_json['copa-do-brasil'][0]['estadio']['nome_popular']
print("Nome do estádio:", nome_estadio)        

placar = chamar_json['copa-do-brasil'][0]['placar']
print("Placar:", placar)

status_jogo = chamar_json['copa-do-brasil'][0]['status']
print("Status:", status_jogo)

separa_dados()

# Exercício 4: no JSON 1 printe todas as chaves e valores do time visitante.

'''
Solução: neste caso, como o "time_visitante" é um dicionário, apenas é necessário indicar o caminho até ele e printar sua estrutura.
'''

print("\nExercício 4:\n")

dados_visitante = chamar_json['copa-do-brasil'][0]['time_visitante']
pprint.pprint(dados_visitante)

separa_dados()