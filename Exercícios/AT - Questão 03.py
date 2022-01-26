# Questão 3
# Considere o argumento abaixo:

# Você já deve ter ouvido algum especialista dizer que as pessoas precisam dedicar, no máximo, 30% da sua renda mensal à moradia, 20% à educação e 15% ao transporte. Esses valores não devem ser totalmente desprezados, mas não podem funcionar como um norte para o orçamento doméstico de todas as famílias.
# Fonte: BTG Pactual Digital

# Crie um programa contendo uma função que, dados um valor de renda mensal total, gastos totais com moradia, gastos totais com educação
#e gastos totais com transporte, faça um diagnóstico da saúde financeira do usuário,
#com base nos valores percentuais acima expostos,
#informando qual é o percentual da renda mensal total comprometido por cada custo.

# Se o gasto estiver dentro do percentual recomendado, informe ainda que 
# Seus gastos estão dentro da margem recomendada.
# Caso contrário, informe:
# 
# Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_max}
#   
# Onde tipo deve ser moradia, educação ou transportes e valor_max deve ser o valor equivalente ao percentual máximo de gasto
#com esse tipo de custo.

# Exemplo de saída do programa:

# Renda mensal total: R$ 5000
# Gastos totais com moradia: R$ 1760
# Gastos totais com educação: R$ 800
# Gastos totais com transporte: R$ 300

# Diagnóstico:

# Seus gastos totais com moradia comprometem 35.2% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ 1500.
# Seus gastos totais com educação comprometem 16% de sua renda total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.
# Seus gastos totais com transporte comprometem 6% de sua renda total. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.
gastoMoradiaIdeal = None
gastoTransporteIdeal = None
gastoEducacaoIdeal = None

def HealthCheck():
    
    #Verificação da porcentagem de gastos com moradia
    porcentagemMoradia = (gastoMoradia * 100) / rendaMensal
    gastoMoradiaIdeal = rendaMensal * 0.3
    porcentagemIdealMoradia = (gastoMoradiaIdeal * 100) / rendaMensal
    
    #Verificação da porcentagem de gastos com Educação
    porcentagemEducacao = (gastoEducacao * 100) / rendaMensal
    gastoEducacaoIdeal = rendaMensal * 0.2
    porcentagemIdealEducacao = (gastoEducacaoIdeal * 100) / rendaMensal
    
    #Verificação da porcentagem de gastos com Transporte
    porcentagemTransporte = (gastoTransporte * 100) / rendaMensal
    gastoTransporteIdeal = rendaMensal * 0.15
    porcentagemIdealTransporte = (gastoTransporteIdeal * 100) / rendaMensal    
    
    print("\n Diagnóstico: ")
    
    #Validação se o custo com moradia é maior que o gasto ideal proposto
    if porcentagemMoradia > porcentagemIdealMoradia:
        diagnosticoMoradia = (f"Seus gastos totais com moradia comprometem {porcentagemMoradia}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {gastoMoradiaIdeal:.2f}.")
    else:
        diagnosticoMoradia = (f"Seus gastos totais com moradia comprometem {porcentagemMoradia}% de sua renda total. O máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada.")
    
    #Validação se o custo com educação é maior que o gasto ideal proposto
    if porcentagemEducacao > porcentagemIdealEducacao:
        diagnosticoEducacao = (f"Seus gastos totais com educação comprometem {porcentagemEducacao}% de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {gastoEducacaoIdeal:.2f}.")
    else:
        diagnosticoEducacao = (f"Seus gastos totais com educação comprometem {porcentagemEducacao}% de sua renda total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.")    
    
    #Validação se o custo com transporte é maior que o gasto ideal proposto
    if porcentagemTransporte > porcentagemIdealTransporte:
        diagnosticoTransporte = (f"Seus gastos totais com transporte comprometem {porcentagemTransporte}% de sua renda total. O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {gastoTransporteIdeal:.2f}.")
    else:
        diagnosticoTransporte = (f"Seus gastos totais com transporte comprometem {porcentagemTransporte}% de sua renda total. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.")           
    
    #A função retorna um print com os valores de diagnóstico de moradia, educação e transporte
    return print(f" \n {diagnosticoMoradia} \n {diagnosticoEducacao} \n {diagnosticoTransporte}") 

#Solicitar valores ao usuário
rendaMensal = float(input("Informe sua renda mensal: "))
gastoMoradia = float(input("Informe o gasto total com moradia: "))
gastoEducacao = float(input("Informe o gasto total com Educação: "))
gastoTransporte = float(input("Informe o gasto total com transporte: "))

#Chamando a função HealthCheck() para que seja impresso o resultado.
HealthCheck()

     
 