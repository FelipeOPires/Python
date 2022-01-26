#Crie um algoritmo que leia uma sequência de n números inteiros
#e mostre a soma, média, o maior número e o menor número da sequência.

soma = 0
media = 0
maior = None
menor = None

for i in range(5):
    numero = int(input(f"Digite o {i+1}º Número: "))
    
    if i == 0:
        maior = numero
        menor = numero
        
    elif numero > maior:
        maior = numero
        
    elif numero < menor:
        menor = numero
               
    #Calculo da soma
    soma += numero
    
    
#Calcular a média
media = soma / (i + 1)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A soma dos números é: {soma}")
print(f"A média é: {media}")    
    