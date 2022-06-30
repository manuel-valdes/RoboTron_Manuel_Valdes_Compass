# Exercício 5: guarde o arquivo JSON 2 nomeando-o como campeonato em uma variável e printe todos os seus dados.

'''
Solução: 
'''

import json
import pprint

print("\nExercício 5:\n")

def campeonato_json():
    with open("_brasileirao.json", encoding="UTF-8") as campeonato:
        dados_campeonato = json.load(campeonato)
        return dados_campeonato

brasileirao_json = campeonato_json()
pprint.pprint(brasileirao_json)

# Função criada simplesmente para separar os resultados no terminal, deixando a leitura dos dados mais acessível:

def separa_dados():
    separador = ("-------------"*14)
    print("\n", separador)

separa_dados()

# Exercício 6: faça com que o programa printe apenas os primeiros dados dentro de edicao_atual, fase_atual, rodada_atual usando o JSON 2.

'''
Solução: 
'''

print("\nExercício 6:\n")

id_edicao_atual = (brasileirao_json['edicao_atual']['edicao_id'])
link_fase_atual = (brasileirao_json['fase_atual']['_link'])
nome_rodada_atual = (brasileirao_json['rodada_atual']['nome'])

print("ID da edição atual:", id_edicao_atual, "\nLink da fase atual:", link_fase_atual, "\nNome da rodada atual:", nome_rodada_atual)

separa_dados()

# Exercício 7: percorra o JSON 2, utilizando o loop FOR e printe suas chaves principais.

'''
Solução: 
'''

print("\nExercício 7:\n")

for i in brasileirao_json:
    print(f"'{i}':")

separa_dados()