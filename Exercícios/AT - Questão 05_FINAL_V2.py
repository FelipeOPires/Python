import pandas

def readFile():
    conteudo = pandas.read_csv('Assessment_PIBs - modelo 1.csv')
    return conteudo

def extrairDados():
    
    validarDados = False
    
    while not validarDados:
        try:
            pais = input('Informe um país: ')
            ano = input('Informe um ano: ')
            
            if (len(conteudo.loc[conteudo['País'] == pais]) == 0):
                print('País não disponível.')
                    
            elif not (ano in conteudo.columns):
                print('Ano não disponível.')
                
            else:
                validarDados = True
        except:
            print('Valores Inválidos.')
            
            
    dados = []
    dados.append(pais)
    dados.append(ano)
    
    return dados

def showPIB(pais, ano):
    paisIndex = conteudo.loc[conteudo['País'] == pais].index[0]
    anoIndex = conteudo.columns.get_loc(ano)
    
    print('Análise de PIB')
    print(f'{pais} em {ano}: US$ {conteudo.iloc[paisIndex][anoIndex]} trilhões.')   
    
conteudo = readFile()
dados = extrairDados()
showPIB(dados[0], dados[1])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

                