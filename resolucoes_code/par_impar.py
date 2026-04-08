# Vamos fazer um código que, como entrada, receba um número inteiro e verifique se ele é par ou ímpar.

# Recebendo o número inteiro do usuário
num = int(input("Digite um número inteiro: "))

# Verificando se o número é par ou ímpar
if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")