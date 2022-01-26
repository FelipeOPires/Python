#B. Desenvolva um programa contendo uma função que liste, por país, a estimativa de variação do PIB, em percentual,
# entre 2013 e 2020.

import pandas as pd

#Abrir arquivo para leitura
def readFile():
    conteudo = pd.read_csv('Assessment_PIBs - modelo 1.csv')
    return conteudo

#Calcular a variação do PIB dos países
def valueVariation():    
    paises = []
    variacoes = []
    retornoVariacao = []
    
    for i in range(len(conteudo)):
        #Retorno dos valores de PIB referentes ao primeiro e último anos
        ultimoano = conteudo.iloc[i][len(conteudo.columns)-1]
        primeiroano = conteudo.iloc[i][1]
        #Cálculo de variação de PIB
        variacao = round(((ultimoano/primeiroano)-1)*100, 2) 
        
        #Texto com o resultado da variação do PIB
        strVariacao = (f'Variação de {variacao}% entre {conteudo.columns[1]} e {conteudo.columns[len(conteudo.columns)-1]}')
        
        #Inserção de conteúdo na lista de paises, variações e retornoVariacao
        paises.append(conteudo.iloc[i][0])
        variacoes.append(variacao)    
        retornoVariacao.append(strVariacao)
        
    imprimir['Países'] = paises
    imprimir['Variações'] = variacoes 
    imprimir['MensagensVariações'] = retornoVariacao
    
#Imprimir resultado
def showResult(): 
    dados = pd.DataFrame(imprimir)
    
    conteudo_var = dados[['Países','MensagensVariações']]
    conteudo_var = conteudo_var.rename(columns={'MensagensVariações': 'Variações'})
    
    print(conteudo_var)

#Definindo a variável imprimir
imprimir = {}

conteudo = readFile()
valueVariation()
showResult() 