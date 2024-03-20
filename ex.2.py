# Coeficientes da equação de segundo grau
a = int(input ("\nDigite um valor pra a:"))
b = int(input ("\nDigite um valor para b:"))
c = int(input ("\nDigite um valor para c:"))

# Calculando o discriminante
delta = b**2 - 4*a*c

# Verificando a natureza das soluções
if delta > 0:
    print("Existem duas raízes reais distintas.")
elif delta == 0:
    print("Existem duas raízes reais iguais.")
else:
    print("Existem duas raízes imaginárias conjugadas.")
