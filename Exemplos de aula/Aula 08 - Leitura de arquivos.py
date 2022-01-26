arquivo = open('python.txt', 'r')

conteudoDoArquivo = arquivo.read()

arquivo.close()

#Exemplo de como dar split nos dados com o separador (@)
#'Abacaxi@Abobora@Banana'.split('@')

#Transformar conteúdo em lista
conteudoDoArquivo = conteudoDoArquivo.splitlines()

for dados in conteudoDoArquivo:
    if(dados == 'Nágella'):
       print(f"{dados}: Amor da vida do Felipe Gustavo Oliveira quer Pênis!")
    elif(dados == 'Ronaldo'):
        print(f"{dados}: Brilha muito no CURINTHIA!")
       
print(conteudoDoArquivo)