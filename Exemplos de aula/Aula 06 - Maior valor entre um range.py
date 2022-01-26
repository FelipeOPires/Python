#Verificar o maior valor entre determinado range (100)

maior = None

for x in range(100):
    if maior == None or x > maior:
        maior = x

print(f"O Maior valor é {maior}.")