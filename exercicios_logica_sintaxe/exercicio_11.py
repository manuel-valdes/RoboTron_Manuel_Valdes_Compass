'''
Exercício: crie um programa que leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, 
tendo uma duração mínima de 1 hora e máxima de 24 horas. Entrada: a entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo. Saída: apresente a 
duração do jogo.
'''

'''
Solução: criação de uma função (duracao_jogo) que recebe dois parâmetros inteiros: "hora_inical" e "hora_final". Caso o input da hora inicial seja maior que o da final, subtrai-se
24 da subtração entre esses dois valores (serve para calcular horários que passam da meia noite). Caso o oposto seja verdade, simplesmente calcula-se a subtração entre o horário
final e o inicial (neste caso, o jogo acaba no mesmo dia). Por fim, se os horários não encaixarem em nenhum dos dois casos citados acima, a estrutura condicional cai no "else", que
determina que o jogo durou 24h (tempo limite). 
'''

def duracao_jogo(hora_inicial, hora_final):
    if hora_inicial > hora_final:
        print(f"\nO jogo durou {24 - (hora_inicial - hora_final)} horas. \n")
    elif hora_final > hora_inicial:
        print(f"\nO jogo durou {hora_final - hora_inicial} horas. \n")
    else:
        print("\nO jogo durou 24 horas. \n")

'''
Um loop while permite que o programa rode quantas vezes o usuário quiser, até responder ao input "Deseja calcular a duração de outro jogo? (s/n) " com a string "n". Dentro do loop,
encontram-se as variáveis que armazenam o horário inicial e final do jogo, além da chamada da função de acordo com esses parâmetros.
'''

while True:
    hora_inicial = int(input("\nDigite a hora de início do jogo: "))
    hora_final = int(input("Digite sua hora de saída: "))
    duracao_jogo(hora_inicial, hora_final)
    if input("Deseja calcular a duração de outro jogo? (s/n) ") == "n":
        break

'''
Tive algumas dificuldades com a lógica deste exercício, portanto procurei programas similares para ter uma noção melhor de como estruturá-lo. O seguinte arquivo do GitHub, programado
em Java, foi usado como referência: https://github.com/eduardo-mior/URI-Online-Judge-Solutions/blob/master/Iniciante/URI%201046.java  
'''