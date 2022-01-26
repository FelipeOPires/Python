#Questão 5

# Considere a projeção em anexo de PIBs feita pelo FMI em 2014:
# 
# Maiores Economias do Mundo (PIB em trilhões de US$ - 2013-2020 – ordem decrescente de 2014)*
# 
# *Dados de 2014; dados de 2015 em diante eram previsões do FMI em 2014.
# 
# A. Desenvolva um programa contendo uma função que permita ao usuário solicitar o PIB de um país para um determinado ano. 
# 
#     O programa solicita ao usuário o nome do país e o ano desejado.
#     Caso o país solicitado ou o ano não sejam válidos, o programa deve informar, na saída, a mensagem: 
# 
#     País não disponível.
# 
#     ou
# 
#     Ano não disponível.
# 
#     a depender do tipo de dado não encontrado. 

import pandas as pd

#Leitura do arquivo
def readFile():
    conteudo = pd.read_csv('Assessment_PIBs - modelo 1.csv')
    return conteudo

#Extração de dados
def extractData():
    
    #Autenticação de dados, se são válidos ou não
    autenticarDados = False
    
    while not autenticarDados:
        #Tente
        try:
            pais = input('Informe um país: ')
            
            #Autenticação se o valor inserido consta no conteúdo da tabela
            if (len(conteudo.loc[conteudo['País'] == pais]) != 0):
                #Caso afirmativo, o usuário deve inserir um ano
                ano = input('Informe um ano: ')
                #Caso o valor de ano não esteja contido no conteúdo da tabela, é informada a exceção.
                if not (ano in conteudo.columns):
                    print('Ano não disponível.\n')
                #Senão, os dados inseridos devem ser tidos como válidos
                else:
                    autenticarDados = True
            #Se nenhuma condição for satisfeita, imprima que o país não está disponível na tabela        
            else:    
                print('País não disponível.\n')
        #Exceção        
        except:
            pass
    
    #dados recebe um array e são inseridos os valores de pais e ano na lista
    dados = []
    dados.append(pais)
    dados.append(ano)
    
    return dados

#Função que demonstrará o valor do PIB
def showPIB(pais, ano):
    #Retorno com a posição do pais na lista
    paisIndex = conteudo.loc[conteudo['País'] == pais].index[0]
    #Retorno com a posição do ano na lista
    anoIndex = conteudo.columns.get_loc(ano)
    
    print('Análise de PIB')
    print(f'PIB {pais} em {ano}: US${conteudo.iloc[paisIndex][anoIndex]} trilhões.')   
    
conteudo = readFile()
dados = extractData()
showPIB(dados[0], dados[1])
       
    
    
    
    
    
    
    
    
    
    
    
    
    

                
