# Ler idade do visitante
idade = int(input("Digite a idade do visitante: "))

# Ler peso do visitante
peso = float(input("Digite o peso do visitante em kg: "))

# Verificar se o visitante está liberado ou proibido de andar na montanha russa
if idade >= 15 and peso <= 120:
    print("Liberado para andar na montanha russa!")
else:
    print("Proibido de andar na montanha russa.")
