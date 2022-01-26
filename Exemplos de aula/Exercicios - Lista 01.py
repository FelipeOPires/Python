# 3. Crie um algoritmo que recebe o valor da altura e do peso de uma pessoa e retorna seu IMC. 
# IMC = peso / altura² 

print("Olá! Por favor, insira a sua altura utilizando . como por exemplo: 1.80")

# Solicitar ao usuário o peso 
peso = float(input("Informe o peso em quilogramas: "))

# Solicitar ao usuário a altura
altura = float(input("Informe a altura em metros: "))

# Cálculo do IMC
imc = peso / altura ** 2 # NOTA: A operação de potência tem precedência sobre divisão e multiplicação

print("Seu IMC é:", round(imc,2))    

#Outra forma de demonstrar o resultado com 2 casas decimais
#print(f"Seu IMC é de: {imc:.2f}")

