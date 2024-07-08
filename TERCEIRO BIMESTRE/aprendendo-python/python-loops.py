# For

qtd_alunos = 5

for i in range(qtd_alunos): # range(5) = [0, 1, 2, 3, 4]
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2

    print(f"A média do aluno {nome} é {media}")

# While

i = 0

while i < 5:
    print(i)
    i += 1
    
