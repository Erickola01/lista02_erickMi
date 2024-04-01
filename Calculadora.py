# Inicializa as variáveis
operador = ''
num1 = 0
num2 = 0

# Solicita ao usuário a operação desejada
while operador not in ['+', '-', '*', '/']:
    operador = input("\nEscolha a operação: \n1 - Soma (+)\n2 - Subtração (-)\n3 - Multiplicação (*)\n4 - Divisão (/)\nDigite o número da operação desejada: ")
    break

# Solicita os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a operação escolhida
if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero!")
        resultado = None


