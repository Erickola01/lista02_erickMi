# Ler altura da pessoa
altura = float(input("Digite a altura da pessoa em metros: "))

# Ler sexo da pessoa
sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ")

# Verificar o sexo e calcular o peso ideal
if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"Peso ideal para um homem de {altura} metros é {peso_ideal} kg.")
elif sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Peso ideal para uma mulher de {altura} metros é {peso_ideal} kg.")
else:
    print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")
