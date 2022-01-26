#Questão 03

#Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas respectivas notas,
#variando de 0 até 10. Crie uma função que leia os nomes dos participantes e, ao final, apresente apenas o nome e a nota do vencedor.

 #Fluxo de exceção: 

    #O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.

#Inicialização dos arrays
dataContestNome = []
dataContestNota = []

#Inicialização das variáveis maiorNota e maiorNome
maiorNota = 0
maiorNome = ''
    
#Função de validação da maior nota inserida    
def contestResultNota(maiorNota):
    
    #Verificar se a nota inserida é menor que 0 ou maior que 10
    if notaDoJuri < 0 or notaDoJuri > 10:
        print('Insira uma nota de 0 a 10')
        #Em caso afirmativo, é uma nota inválida que deve ser desconsiderada e o programa encerrado.
        exit()
    #Caso contrário, se a nota for maior que 0 e menor ou igual a 10, insira o valor de notaDoJuri no array dataContestNota    
    if notaDoJuri > 0 and notaDoJuri <= 10:
            dataContestNota.append(notaDoJuri)
     #Se a maior nota for menor que a posição [atual] do array dataContestNota[i], então a maior nota receberá o valor dessa posição do array
    if maiorNota < dataContestNota[i]:
        maiorNota = dataContestNota[i]
        
    return maiorNota   

#Função de validação do nome atrelado a maior nota
def contestResultNome(maiorNome):
    
    #Se a maior nota for menor ou igual a posição [atual] do array dataContestNota[i], então o maior nome receberá o valor da posição dataContestNome[i]
    if maiorNota <= dataContestNota[i]:
        maiorNome = dataContestNome[i]
        
    return maiorNome     
     
#Laço de repetição for que será executado dentro do range pré-definido (5)     
for i in range(5):
      
    #Solicitar o nome do participante  
    nomeDoParticipante = input(f"Informe o nome do {i + 1}º participante: ")
    #É inserido o valor da variável nomeDoParticipante no array dataContestNome.
    dataContestNome.append(nomeDoParticipante)
     
    #Solicitar a nota do participante
    notaDoJuri = int(input(f"Informe a nota do {i + 1}º participante: "))
    
    #Chamando a função contestResultNota
    contestResultNota(maiorNota)
    
    #Validação se o valor da maiorNota é menor que no array dataContestNota[i],
    #e caso afirmativo, a maiorNota receberá este valor.
    #Assim como o valor de dataContestNome[i] será guardado na variável maiorNome.
    if maiorNota < dataContestNota[i]:
        maiorNota = dataContestNota[i]
        maiorNome = dataContestNome[i]
    
    #Chamando a função contestResultNome
    contestResultNome(maiorNome)
    
    #Sei que o código está redundante, mas ainda não compreendi como fazê-lo de uma forma mais eficiente.
                          
print('A maior nota foi', contestResultNota(maiorNota), ', atribuida ao participante', contestResultNome(maiorNome),'.')

