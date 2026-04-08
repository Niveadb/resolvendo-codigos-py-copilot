# Vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 

# Recebendo a string do usuário
string = input("Digite a string: ")

# Recebendo o número inteiro do usuário
num = int(input("Digite o número de vezes que deseja repetir a string: "))

# Repetindo a string o número de vezes informado
print("A string repetida é:", (string + ' ') * num)
