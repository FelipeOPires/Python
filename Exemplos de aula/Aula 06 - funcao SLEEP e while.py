#Exemplo de utilização da função Sleep

import time

num_flexoes = 0

while num_flexoes < 30:
    print(f"{num_flexoes + 1} flexões feitas!")
    
    if (num_flexoes +1) % 10 == 0: #Se o resto da divisão for igual a 0, imprima o texto abaixo 
        print("Pare 1 minuto e descanse.")
        time.sleep(5)
        #Função sleep, para a cada 5 segundos haver uma "pausa" no programa
    
    num_flexoes = num_flexoes + 1
    
    