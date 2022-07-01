'''
Letra A: crie uma “aplicação” em loop que tenha uma opção para listar todos os elementos da tabela, porém mostrando apenas uma propriedade do elemento. Ex: listar todos 
os nomes dos elementos na tabela.
'''

'''
Solução: criação de um menu dentro de um input através do qual o usuário escolhe qual dado ele quer receber. Em seguida, criação de uma estrutura condicional que associa cada 
input do usuário com a impressão de um dado específico, como indicado no menu. Por fim, todo esse código se encontra encorpado por um loop while, do qual o usuário consegue sair
no meu (ao digitar 7 no input) ou quando ele digita um valor inválido e responde "n" ao input "Você não digitou um valor válido. Deseja tentar novamente?".
'''

import pandas as pd
import pprint

tabela_periodica = pd.read_csv('_tab_periodica.csv', encoding='UTF-8', sep=',')

while True:
    escolha = input("""
        Observe as seguintes opções:

        [1] Imprimir os símbolos de todos os elementos
        [2] Imprimir os nomes de todos os elementos
        [3] Imprimir os números atômicos de todos os elementos
        [4] Imprimir a linha de todos os elementos
        [5] Imprimir a coluna de todos os elementos
        [6] Imprimir o estado físico de todos os elementos
        [7] Sair
        
        Digite sua escolha: """)

    if escolha == "1":
        print("\nSímbolo:\n\n"+tabela_periodica["Simbolo"].to_string(index=True))
    elif escolha == "2":
        print("\nNome:\n\n"+tabela_periodica["Nome"].to_string(index=True))
    elif escolha == "3":
        print("\nNúmero atômico:\n\n"+tabela_periodica["NumeroAtomico"].to_string(index=True))
    elif escolha == "4":
        print("\nLinha:\n\n"+tabela_periodica["Linha"].to_string(index=True))
    elif escolha == "5":
        print("\nColuna:\n\n"+tabela_periodica["Coluna"].to_string(index=True))
    elif escolha == "6":
        print("\nEstado físico:\n\n"+tabela_periodica["EstadoFisico"].to_string(index=True))
    elif escolha == "7":
        break
    else:
        if input("\nVocê não digitou um valor válido. Deseja tentar novamente? (s/n): ") == "s":
            continue
        else:
            break

# Função criada simplesmente para separar os resultados no terminal, deixando a leitura dos dados mais acessível:

def separa_dados():
    separador = ("-------------"*14)
    print("\n", separador)

separa_dados()

'''
Letra B: listar todos os dados de determinado elemento, buscando através do seu símbolo.
'''

'''
Solução: comparação da coluna "Simbolo" com a variável que armazena o input do usuário. Caso a comparação seja verdadeira, printa a linha inteira.
'''

simbolo_escolhido = input("\nDigite o símbolo do elemento que você deseja acessar: ")
print()
print(tabela_periodica[tabela_periodica["Simbolo"] == simbolo_escolhido])

separa_dados()

'''
Letra C: listar todos os dados de todos os elementos inseridos.
'''

'''
Solução: caso o input do usuário indique que ele quer acessar todos os dados da tabela, ela é printada em sua integridade através da função pprint, que mantém sua formatação.
'''

if input("\nDeseja acessar todos os dados de todos os elementos inseridos? (s/n): ") == "s" or "S":
    print()
    pprint.pprint(tabela_periodica)
else:
    print("\nAté a próxima! ")

separa_dados()
