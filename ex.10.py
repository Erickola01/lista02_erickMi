# Ler primeira nota bimestral
nota1 = float(input("Digite a primeira nota bimestral: "))

# Ler segunda nota bimestral
nota2 = float(input("Digite a segunda nota bimestral: "))

# Ler código da Universidade
codigo_universidade = int(input("Digite o código da Universidade (PUCPR ou UNICAMP): "))

# Calcular média das notas
media = (nota1 + nota2) / 2

# Verificar a situação do estudante com base na média e no código da Universidade
if codigo_universidade == 1:
    if media >= 7.0:
        print("Aprovado")
    elif media >= 4.0:
        print("Em exame")
    else:
        print("Reprovado")
elif codigo_universidade == 2:
    if media >= 5.0:
        print("Aprovado")
    else:
        print("Em exame")
else:
    print("Código da Universidade inválido.")

