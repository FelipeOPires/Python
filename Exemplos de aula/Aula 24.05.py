#Laço for com condicional IF na estrutura

num_participantes = int(input("Informe o número de participantes: "))

for i in range(num_participantes):
    participante = input(f"Informe o nome do {i +1}º participante: ")
    nota = float(input(f"Informe a nota do {i +1}º participante: "))
    
    if i == 0 or nota > nota_vencedor:  
        #É o primeiro participante
        participante_vencedor = participante
        nota_vencedor = nota
        
print(f"O vencedor é {participante_vencedor} com a nota {nota_vencedor}.")