import math
# Mètodos importantes em Python

# Métodos de strings
# capitalize() - Retorna a primeira letra da string em maiúscula
# lower() - Retorna a string em letras minúsculas
# upper() - Retorna a string em letras maiúsculas
# title() - Retorna a string com a primeira letra de cada palavra em maiúscula
# split() - Retorna uma lista de palavras da string
# replace() - Substitui um trecho da string por outro
# find() - Retorna a posição da primeira ocorrência da string
# count() - Retorna a quantidade de ocorrências da string
# startswith() - Verifica se a string começa com um determinado trecho
# endswith() - Verifica se a string termina com um determinado trecho
# isdigit() - Verifica se a string é um número

# Métodos de números
# round() - Arredonda um número
# pow() - Retorna um número elevado a potência de outro
# sqrt() - Retorna a raiz quadrada de um número
# ceil() - Arredonda um número para cima
# floor() - Arredonda um número para baixo

# Exemplos

nome_completo = "joão pedro silva"

print(nome_completo.capitalize()) # João pedro silva
print(nome_completo.lower()) # joão pedro silva
print(nome_completo.upper()) # JOÃO PEDRO SILVA
print(nome_completo.title()) # João Pedro Silva
print(nome_completo.split()) # ['joão', 'pedro', 'silva']
print(nome_completo.replace("joão", "maria")) # maria pedro silva
print(nome_completo.find("pedro")) # 5
print(nome_completo.count("a")) # 2
print(nome_completo.startswith("joão")) # True
print(nome_completo.endswith("silva")) # True
print(nome_completo.isdigit()) # False

# Strings "parecem" listas
# Podemos acessar os caracteres de uma string como se fosse uma lista
# Exemplo
print(nome_completo[0]) # j
print(nome_completo[1]) # o
print(nome_completo[2]) # ã
print(nome_completo[3]) # o

numero = 10.5

print(round(numero)) # 11
print(pow(numero, 2)) # 110.25
print(math.sqrt(numero)) # 3.24037034920393
print(math.ceil(numero)) # 11
print(math.floor(numero)) # 10
print(math.pi) # 3.141592653589793
