temperatura = float(input("Digite a temperatura do dia de hoje (em ºC): "))

# Verificando a faixa de temperatura e exibindo a mensagem correspondente
if temperatura < 15:
    print("Está frio!!")
elif temperatura > 25:
    print("Está calor!")
else:
    print("Temperatura agradável!")