# Ler a nota do estudante
nota = float(input("Digite a nota do estudante: "))

if nota >= 7:
    print("Estudante aprovado")
elif 4 <= nota < 7:
    print("Estudante em recuperação")
else:
    print("Estudante reprovado")
