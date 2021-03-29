#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


nome = input(f"Digite seu nome: ")

if len(nome) <= 3:
    print(f"Nome com menos de 3 caracteres.")
    print(f"Programa encerrado")
    quit()


idade = int(input(f"Qual a sua idade? "))

if idade < 0 or idade > 150:
    print(f"Por favor {nome}, digite uma idade valida.")
    print(f"Programa encerrado")
    quit()


salário = int(input(f"Qual o seu salario? "))

if salário < 0:
    print(f"Salario negativo não é valido.")
    print(f"Programa encerrado")
    quit()

sexo = str(input("Qual o seu sexo ['f'] para Feminino ou ['m'] para Masculino: "))

if sexo == "f" or sexo == "m":
    print()
else:
    print(f"Sexo não identificado.")
    print(f"Programa encerrado")
    quit()




#estado_civil: 's', 'c', 'v', 'd'




