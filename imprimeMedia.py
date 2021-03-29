# Programa feito por Marcos Luis Mendes
# Aluno da Blue 11/03/2021

# vou criar 4 variaveis para notas do aluno
aluno = input("Aluno: ")
notaAluno = []
contador = 1

while contador < 5: 
    notaAluno.append(int(input(f"Digite a nota {contador}: ")))
    contador += 1

# o codigo abaixo calcula a media das notas 
media = sum(notaAluno) / 4

# imprime o valor da media calculada para o usuario
print("A media e :", media)

# A media para ser aprovado e 7 e para recuperacao 5
if media >= 7 :
    print(aluno,", foi Aprovado com media", media, ".")
elif media < 5:
    print(aluno,", foi reprovado, com media",media,"." )
    for i in range(1,5):
       print("Nunca desita, se é o seu sonho vale a pena tentar de novo!!")
else:
    print(aluno,", esta de recuperação com media",media,".")




