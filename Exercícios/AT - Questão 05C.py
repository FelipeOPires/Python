#C. Desenvolva uma função que, para um país, exiba o gráfico da evolução do PIB ao longo dos anos.
# 
#    A função deve receber, como entrada, o nome de um país, e exibir o gráfico para todo o período listado na tabela.
#    O gráfico deve conter os valores do PIB no eixo das ordenadas (vertical) e os anos no eixo das abscissas (horizontal)

import pandas as pd
import matplotlib.pyplot as plt

#Abrir arquivo para leitura
def readFile():
    conteudo = pd.read_csv('Assessment_PIBs - modelo 1.csv')
    return conteudo

#Extração de dados
def extractData():
    autenticarDados = False

    while not autenticarDados:
        try:
            pais = input('Informe um país: ')

            if (len(conteudo.loc[conteudo['País'] == pais]) == 0):
                print('País não disponível.\n')
            else:                                
                autenticarDados = True
        except:
            print('\nValor Incorreto\n')
            
    return pais

def graphData():
    #Inserção de valores do contepudo da tabela na variável conteudoGd 
    conteudoGd = conteudo.loc[conteudo['País'] == pais]
    conteudoGd = conteudoGd.iloc[:,1:len(conteudo.columns)]         
    
    #Montagem do PIB com valores e colunas referentes ao conteúdo da tabela
    PIB['Colunas'] = list(conteudo.columns[1:])
    PIB['Valores'] = conteudoGd.values[0]
    
    return PIB

def showResult(): 
    plt.bar(PIB['Colunas'], PIB['Valores'])
    #Rótulos do Eixo X e Y
    plt.xlabel('Ano')
    plt.ylabel('Valores em Trilhões US$')
    #Título do gráfico
    plt.title(f'Evolução PIB {pais}')
    #Exibir o gráfico
    plt.show() 
    
PIB = {}
conteudo = readFile()
pais = extractData()
graphData()
showResult()

    

