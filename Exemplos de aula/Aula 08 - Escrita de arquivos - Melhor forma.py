import os

#Verificar qual é o diretório default utilizado
diretorio = os.getcwd()

def cadastrar_nomes(output):
    
    with open(output, 'w') as arquivo:
        arquivo.write('CONTATOS\r')
        for i in range(5):
            nome = input('Nome: ')
            arquivo.write(f"{nome}\r")
            
cadastrar_nomes('python.txt')


