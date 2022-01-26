#Validação de voto obrigatório (True ou False)

def voto_obrigatorio(idade):
    return idade >= 18 and idade < 70


idade = int(input("Qual é a sua idade: "))
print(voto_obrigatorio(idade))