#Utilizar uma função para calular o IMC

def calcular_imc(peso,altura):
    imc = peso / altura ** 2
    imc = round(imc,2)
    return imc

#Solicitar ao usuário seu peso:
peso = float(input("Informe seu peso em quelogramas: "))

#Solicitar ao usuário sua altura:
altura = float(input("Informe sua altura em metros: "))

print(f"O seu IMC é de {calcular_imc(peso, altura)}")