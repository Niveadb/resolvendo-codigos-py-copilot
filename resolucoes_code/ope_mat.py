# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Recebendo os números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))   

# Recebendo a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realizando a operação escolhida
if operacao == "+": #soma
    resultado = num1 + num2

elif operacao == "-": #subtração
    resultado = abs(num1 - num2)

elif operacao == "*": #multiplicação
    resultado = num1 * num2

elif operacao == "/": #divisão
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero não é permitida." 
else:
    resultado = "Operação inválida."

# Exibindo o resultado
print("O resultado da operação é:", resultado)