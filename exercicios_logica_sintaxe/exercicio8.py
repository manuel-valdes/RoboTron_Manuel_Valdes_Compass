'''
Exercício: crie um programa que lê 1 valor inteiro para X. Se o valor for par, calcular o fatorial de x em uma função e apresentar o resultado fora da função. Se o valor for impar, 
apresentar em uma função a tabuada de 1 a 10 de X.
'''

'''
Solução: para criar a função que executa o fatorial do número recebido, segui a lógica de que uma operação de fatorial multiplica o número inicial pelo próximo inteiro menor e
segue executando esse caminho até chegar no multiplicador de 1. Assim, criei uma variável chamada "contador" que armazena o próximo número inteiro menor ao do resultado da operação
até aquele momento (que é armazenado pela variável "resultado"). Em seguida, um loop while executa a operação de multiplicação na estrutura do fatorial enquanto a variável "contador"
é maior que zero (finalizando ao alcançar o valor de 1). Por fim, a função "fatorial" imprime o resultado. 

Em relação à função de "tabuada", criada para apresentar a tabuada de 1 a 10 do número recebido caso ele seja par, um loop for com range entre 1 e 11 (uma vez que ele exclui da 
operação o número máximo indicado, portanto o loop vai até 10) armazena na variável "valor" o resultado da operação de cada multiplicador entre 1 e 10, imprimindo esse resultado
a cada iteração do loop.

Uma estrutura condicional é criada para chamar a função "fatorial" quando o input da variável "x" for ímpar e para chamar a função "tabuada" quando esse número for par. Para 
finalizar, toda a estrutura está envolvida num loop while True, que é encerrado quando o usuário responde que quer sair do programa, ao responder "n" ao input que pergunta se 
ele deseja realizar a operação novamente com outro número. 
'''


def fatorial(x):
    contador = (x - 1)
    resultado = x
    while contador > 0:
        resultado *= contador
        contador -= 1
    print(resultado)

def tabuada(x):
    for i in range(1,11):
        valor = x*i
        i += 1
        print(valor)

while True:
    x = int(input("\nDigite um número inteiro: "))

    if x % 2 != 0:
        print("\nEsse número é ímpar! O resultado de seu fatorial é: ")
        fatorial(x)
    else:
        print("\nEsse número é par! Segue sua tabuada: ")
        tabuada(x)

    if input("\nDeseja rodar outro número? (s/n) ") == "n":
        break