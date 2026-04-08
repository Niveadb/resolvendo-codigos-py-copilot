# Vamos calcular a média de três notas fornecidas na entrada do usuário

# Recebendo as notas do usuário
nota1, nota2, nota3 = map(float, input("Digite as três notas: ").split())

# Calculando a média
media = (nota1 + nota2 + nota3) / 3

# Exibindo o resultado
print("A média das notas é:", media)
