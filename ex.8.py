# Ler idade da pessoa
idade = int(input("Digite a idade da pessoa: "))

# Verificar a situação eleitoral com base na idade
if idade < 16:
    print("Não eleitor")
elif idade < 18 or idade >= 65:
    print("Eleitor facultativo")
else:
    print("Eleitor obrigatório")
