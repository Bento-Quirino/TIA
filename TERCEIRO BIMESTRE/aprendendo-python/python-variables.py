# Como declarar variáveis em Python

# Variáveis são espaços de memória que armazenam valores.
# Em Python não temos a necessidade de especificar o tipo de dado 
# Para declarar uma variável, basta atribuir um valor a ela. Veja o exemplo:
nome = "João Pedro Silva" # String
idade = 20 # Inteiro
altura = 1.75 # Float
peso = 70.5 # Float
matriculado = True # Booleano


# Mostrando os valores das variáveis
print(nome)
print(idade)
print(altura)
print(peso)
print(matriculado)


# Concatenando variáveis
# Precisa de cast para concatenar variáveis de tipos diferentes
print("Nome: " + nome)
print("Idade: " + str(idade))
print("Altura: " + str(altura))
print("Peso: " + str(peso))
print("Matriculado: " + str(matriculado))


# Interpolação de strings
print(f"Meu nome é {nome}, tenho {idade} anos, {altura} de altura e peso {peso} kg. Matriculado: {matriculado}")