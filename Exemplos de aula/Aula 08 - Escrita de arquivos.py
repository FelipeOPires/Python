import os
# Exemplo de abertura de arquivos em Python:

# Criamos uma variável chamada arquivo
# A ela, atribuímos o resultado da chamada de open()
# open() recebe, como primeiro parâmetro, o nome de um arquivo.
# Aqui, usamos dados.txt. A extensão não precisa se limitar a txt, mas é importante que contenha texto.
# Caso o caminho completo do arquivo não seja especificado, será assumida a pasta onde está o código
# O segundo parâmetro é o modo de abertura do arquivo.
# Use w para abrir o arquivo para escrita. Isso sobrescreverá o arquivo anterior
# Use r para abrir o arquivo para leitura.
# Use a para abrir o arquivo para edição, mantendo o arquivo original e escrevendo ao fim dele.

diretorio = os.getcwd()
arquivo = open("python.txt", "w", encoding='utf-8')

# Agora, já temos o arquivo aberto para escrita e armazenado na variável arquivo.
# Vamos escrever no arquivo:
for contador in range(10):
  # Escrevemos uma linha no arquivo com a função write. 
  # O conteúdo escrito é o parâmetro da função.
  # O caractere \r, ao final, é um retorno, uma quebra de linha.
  arquivo.write(f"Esta é a linha {contador + 1}.\r")

# O último passo é fechar o arquivo, com a função close():
arquivo.close()