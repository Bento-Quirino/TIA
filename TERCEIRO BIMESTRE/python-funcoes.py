# Funções
# Funções são blocos de código que realizam uma tarefa específica.
# Em Python, uma função é definida pela palavra-chave def, seguida do nome da função, parênteses e dois pontos.

# Exemplo:
def saudacao():
    print("Olá, tudo bem?")
    
# Para chamar uma função, basta escrever o nome dela seguido de parênteses.
saudacao() # Olá, tudo bem?

# Funções podem receber parâmetros, que são valores que a função recebe para realizar a tarefa.
def somar(a, b):
    print(a + b)
    
somar(10, 5) # 15

# Funções podem retornar valores com a palavra-chave return.
def subtrair(a, b):
    return a - b

print(subtrair(10, 5)) # 5


# Parâmetros padrão
# É possível definir valores padrão para os parâmetros de uma função.
# Caso o valor não seja passado, a função utilizará o valor padrão.
def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2)) # 4
print(exponencial(2, 3)) # 8

# Parâmetros nomeados
# Ao chamar uma função, é possível passar os parâmetros pelo nome.
# Isso permite que os parâmetros sejam passados fora de ordem.

def dados_pessoais(nome, idade, cidade):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
    
dados_pessoais(idade=20, nome="João", cidade="São Paulo") # Nome: João, Idade: 20, Cidade: São Paulo

# Retornando múltiplos valores
# Uma função pode retornar múltiplos valores utilizando uma lista ou tupla.
def calcular(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    
    return [soma, subtracao, multiplicacao, divisao]

calculos = calcular(10, 5)
print(calculos) # [15, 5, 50, 2.0]

# Podemos pegar os parametros separadamente também

soma, subtracao, multiplicacao, divisao = calcular(10, 5)
print(soma) # 15
print(subtracao) # 5
print(multiplicacao) # 50
print(divisao) # 2.0
