#Questão 02

 #Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:

    #Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
    #Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
    #Não tem direito a voto (menor de 16 anos).

#Fluxo de exceção: 

    #O programa deve verificar se a idade da pessoa é maior do que zero.

def validacaoVotacao():
    #Verificação de idade maior que 0
    if idade <=0:
        print('Idade inválida.')
        exit()
    #Verificação se a pessoa possui idade entre 18 e 70 anos
    elif idade >= 18 and idade < 70:
        return f'Tem obrigação de votar.'
    #Verificação se a pessoa possui entre 16 e 17 anos OU 70 anos ou mais
    elif idade >= 16 and idade < 18 or idade > 70:
        return f'Não tem obrigação de votar.'
    #Verificação se a pessoa não possui direito a voto, caso tenha 15 anos ou menos.
    elif idade < 16:
        return f'Não tem direito a voto.'
    
#Solicitar a idade ao usuário
idade = int(input("Informe a sua idade: "))

#Imprimir o resultado final na tela
print(validacaoVotacao())

