# Ler idade do trabalhador
idade = int(input("Digite a idade do trabalhador: "))

# Ler tempo de serviço do trabalhador
tempo_servico = int(input("Digite o tempo de serviço do trabalhador: "))

# Verificar se o trabalhador pode se aposentar
if idade >= 65 or tempo_servico >= 30:
    print("Pode se aposentar")
elif idade >= 60 and tempo_servico >= 25:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")
