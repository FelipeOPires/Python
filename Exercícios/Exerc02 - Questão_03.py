#Questão 03

#Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas respectivas notas,
#variando de 0 até 10. Crie uma função que leia os nomes dos participantes e, ao final, apresente apenas o nome e a nota do vencedor.

 #Fluxo de exceção: 

    #O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.

dataContestNome = []
dataContestNota = []

maiorNota = 0
    
for i in range(2):
        
    nomeDoParticipante = input("Nome do participante: ")
    dataContestNome.append(nomeDoParticipante)
        
    notaDoJuri = int(input("Nota do Juri: "))
    
    if notaDoJuri < 0 or notaDoJuri > 10:
        print('Insira uma nota de 0 a 10')
        
        exit()
             
    elif notaDoJuri > 0 and notaDoJuri <= 10:
            dataContestNota.append(notaDoJuri)
        
    if maiorNota < dataContestNota[i]:
        maiorNota = dataContestNota[i]
        maiorNome = dataContestNome[i]
           
print('A maior nota foi', maiorNota, ', atribuida ao participante', maiorNome,'.')
        