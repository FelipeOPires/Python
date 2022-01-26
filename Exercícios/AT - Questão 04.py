#Questão 4
#Seja a seguinte citação:
#Os juros compostos são a força mais poderosa do universo e a maior invenção da humanidade, porque permitem uma confiável e sistemática acumulação de riqueza 
#A frase, curiosamente, é de Albert Einstein, não de algum banqueiro ou gestor de fundos de capitais. 
#Assim, suponha que você possui R$10.000 iniciais, consegue aportar R$1.000 por mês e obtém um rendimento de 0,54% ao mês. Por simplicidade, suponha que você faz o aporte após o rendimento no período acontecer.
#No primeiro mês, terá R$10.000 + 0,54% deste valor = R$10.054,00. E, com o novo aporte, R$11.054,00.
#No segundo mês, o valor inicial é de R$11.054,00. Ele rende 0,54%, totalizando R$11.113,69. Com o novo aporte, R$12.113,69, e assim sucessivamente.
#Ao final de 120 meses, você terá o montante final de R$187.303,05.
#a.	Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, como entrada, um montante financeiro inicial, um percentual de rendimento por período, um valor de aporte para cada período e uma quantidade de períodos.
#Exemplo de saída do programa:

#Valor inicial: R$ 10000
#Rendimento por período (%): 0.54
#Aporte a cada período: R$ 1000
#Total de períodos: 120 

#Após 1 períodos(s), o montante será de R$11054.00.
#Após 2 períodos(s), o montante será de R$12113.69.
#Após 3 períodos(s), o montante será de R$13179.11.
#Após 4 períodos(s), o montante será de R$14250.27.
#Após 5 períodos(s), o montante será de R$15327.22.
#(...)
#Após 115 períodos(s), o montante será de R$177406.76.
#Após 116 períodos(s), o montante será de R$179364.76.
#Após 117 períodos(s), o montante será de R$181333.33.
#Após 118 períodos(s), o montante será de R$183312.53.
#Após 119 períodos(s), o montante será de R$185302.42.
#Após 120 períodos(s), o montante será de R$187303.05.
  
#b.	Crie uma função que exiba um gráfico da evolução do valor acumulado, tendo como eixo das abscissas (horizontal) o número de períodos e, no eixo das ordenadas (vertical), o valor acumulado, em reais.

import matplotlib.pyplot as plt

listaRendimento = []
contador = []

def montantePorPeriodo(montanteInicial, rendimentoPorPeriodo, aportePorPeriodo):
    
    #Percorrer de i até qtdePeriodos
    for i in range(qtdePeriodos):
        #Inserção do valor de montanteInicial na listaRendimento
        listaRendimento.append(montanteInicial)
        #Inserção da posição atual percorrida no contador
        contador.append(i)
        #Cálculo do montante inicial + o valor sob a porcentagem do rendimento
        montanteInicial += montanteInicial * (rendimentoPorPeriodo / 100)
        #O valor do aporte é somado a variavel montanteInicial
        montanteInicial += aportePorPeriodo
        
        #Impressão
        print(f"Após {i+1} período(s), o montante será de R${montanteInicial:.2f}")

def exibirGrafico():

    plt.plot(contador, listaRendimento, color='blue')
    plt.title('Gráfico da evolução do valor acumulado')
    
    plt.xlabel('Períodos')
    plt.ylabel('Rendimento por período')
    
    plt.show()
        
montanteInicial = float(input("Valor inicial: R$ "))
rendimentoPorPeriodo = float(input("Rendimento por período: R$ "))
aportePorPeriodo = float(input("Aporte a cada período: R$ "))
qtdePeriodos = int(input("Total de períodos: "))

montantePorPeriodo(montanteInicial, rendimentoPorPeriodo, aportePorPeriodo)
exibirGrafico()