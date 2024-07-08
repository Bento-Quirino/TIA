# Condicionais em Python

# Variáveis de teste
idade = 20
altura = 1.75
email = "email.teste@email.com"
senha = "123456"
matriculado = False

# Criando um if simples
if idade >= 18:
    print("Maior de idade")
    
# Criando um if com else
if altura >= 1.80:
    print("Alto")
else:
    print("Baixo")
    
# Criando um if com elif
if idade >= 18:
    print("Maior de idade")
elif idade < 18:
    print("Menor de idade")

# Criando um if com elif e else
if email == "email.teste@email.com":
    print("Email válido")
elif email == "":
    print("Email não pode ser vazio")
else:
    print("Email inválido")
