#Questão 01

#Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar),
#em reais, considerando o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.

#Ao usuário do programa serão solicitados o valor total do consumo, em reais, o número total de pessoas e o
#percentual do serviço prestado, entre 0 e 100.

#Fluxo de exceção: 

    #O programa deve verificar se o número total de pessoas é maior do que zero.
    #O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
    #Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e o programa deve ser interrompido.

valorTotalDoConsumo = 0
divisaoDaConta = 0

def contaDeConsumo(valorTotalDoConsumo, taxaDeServico):
    
    taxaDeServico = (valorTotalDoConsumo * taxaDeServico) / 100  #Conversão em % baseado no valor total de consumo
    valorTotalDoConsumo = valorTotalDoConsumo + taxaDeServico    #Valor do consumo adicionando a taxa de serviço
    
    return valorTotalDoConsumo

def divisaoFunction(divisaoDaConta):
    divisaoDaConta = contaDeConsumo(valorTotalDoConsumo, taxaDeServico)
    divisaoFinal = divisaoDaConta / numeroTotalDePessoas
    
    return divisaoFinal

#Solicitar ao cliente o valor total de consumo:
valorTotalDoConsumo = float(input("Informe o valor total do consumo: "))

#Validar se a variável valorTotalDoConsumo possui um valor maior que 0, dado que se for o caso não
#haverá sentido em continuar o cálculo.

if valorTotalDoConsumo <=0:
    print("Valor inválido")
    
    exit()

#Solicitar ao cliente a taxa de serviço:
taxaDeServico = float(input("Informe a taxa de serviço, entre 0 e 100: "))
taxaDeServico = round(taxaDeServico,2)

if taxaDeServico >= 0 and taxaDeServico<= 100:
    #Solicitar ao cliente a quantidade de pessoas que a conta será divida:
    numeroTotalDePessoas = int(input("Informe o total de pessoas: "))
    
    if numeroTotalDePessoas > 0:
        
        #Conversão de valores no retorno da função contaDeConsumo, para string. Dados armazenados na variável vtString
        vtString = str(contaDeConsumo(valorTotalDoConsumo, taxaDeServico))
        #Conversão de valores do retorno da função divisaoFunction, para string. Dados armazenados na variável txString
        txString = str(divisaoFunction(divisaoDaConta))

        print("O valor total da conta, inclusa a taxa de serviço é de R$", str.replace(vtString, ".", ","))
        print("Dividindo a conta por", numeroTotalDePessoas, "pessoa(s), cada um pagará R$", str.replace(txString, ".", ","))
    else:
        print("Valor inválido")
else:
    print("Valor inválido")
    
    

