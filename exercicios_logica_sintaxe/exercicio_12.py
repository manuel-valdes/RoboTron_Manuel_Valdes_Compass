'''
Exercício: crie um programa que leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias. Obs.: apenas para facilitar o cálculo, 
considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. 
'''

'''
Solução: a partir do input "numero_dias", que fornece ao usuário a possibilidade de inserir sua idade em dias, criaram-se três variáveis. A variável "anos" aplica o operador de
divisão inteira (//), que retorna o menor número inteiro mais próximo (arredonda para baixo). Assim, esta variável revela quantos anos inteiros se encaixam no número fornecido no
input. Uma lógica similar é aplicada na variável "meses", em que se subtrai o número total de dias indicado pelo usuário da quantidade de dias presentes no número armazenado na
variável "anos". Aplica-se novamente uma divisão inteira. Por fim, a quantidade de dias que sobram é calculada na variável "dias" através da subtração entre o total de dias e os 
dias representados em meses e anos completos. A função print faz uso de uma f-string para simplificar a impressão dos dados.
'''

numero_dias = int(input("\nDigite sua idade em dias: "))

anos = numero_dias // 365
meses = (numero_dias - (anos*365)) // 30
dias = numero_dias - (anos*365 + meses*30)

print(f"\nVocê está vivo há {anos} anos, {meses} meses e {dias} dias.\n")