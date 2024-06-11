# Diferença entre lists, dictionaries e tuples

# Listas
# Listas são coleções de itens ordenados e mutáveis.
# São representadas por colchetes [].
# Exemplo:
lista = ["João", "Maria", "José"]

# Dicionários
# Dicionários são coleções de itens não ordenados e mutáveis.
# São representados por chaves {}.
# Exemplo:
dicionario = {
    "nome": "João",
    "idade": 20,
    "altura": 1.75
}

# Tuplas
# Tuplas são coleções de itens ordenados e imutáveis.
# São representadas por parênteses ().
# Exemplo:
tupla = ("João", "Maria", "José")

# Acessando itens
print(lista[0]) # João
print(dicionario["nome"]) # João
print(tupla[0]) # João

# Métodos importantes

lista.append("Pedro") # Adiciona um item no final da lista
print(lista) # ['João', 'Maria', 'José', 'Pedro']

dicionario["sobrenome"] = "Silva" # Adiciona um item ao dicionário
print(dicionario) # {'nome': 'João', 'idade': 20, 'altura': 1.75, 'sobrenome': 'Silva'}

tupla.count("João") # Conta a quantidade de ocorrências do item na tupla
print(tupla) # ('João', 'Maria', 'José')

# Iterando

for item in lista:
    print(item)

for chave, valor in dicionario.items():
    print(chave, valor)

for item in tupla:
    print(item)
    
# Listas, dicionários e tuplas são estruturas de dados muito importantes em Python.
# Cada uma delas possui características específicas e é indicada para diferentes situações.
# É importante conhecer bem cada uma delas para saber quando utilizá-las da melhor forma.


# Listas em Python tem indices que começam em 0 e vão até n-1, onde n é o tamanho da lista.
# Além de terem indices positivos, as listas também tem indices negativos, que começam em -1 e vão até -n, onde n é o tamanho da lista.
# Exemplo:
lista = ["a", "b", "c", "d", "e"]

print(lista[0]) # a
print(lista[-1]) # e
print(lista[-2]) # d
print(lista[1]) # c
