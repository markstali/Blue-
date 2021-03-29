# Programa feito por Marcos Luis Mendes
# Aluno da Blue 11/03/2021

while True:
    aluno = input("Digite seu nome: ")

    listaDeNotas = []

    for i in range(1, 5):
        listaDeNotas.append(float(input(f"Entre com a {i}° nota: ")))

    print()

    mediaAluno = sum(listaDeNotas) / 4
    mediaGeral = 6

    if(mediaAluno >= mediaGeral):
        print(f"Parabéns, {aluno} você passou!!")
    elif(mediaAluno >= 4 and mediaAluno == 5):
       print(f"{aluno} ,você esta de recuperarção.")

    else:
        print(f"Que pena, {aluno} você não passou!!")
    
    print(f"Sua media foi: {mediaAluno}")
    continuar = input("Deseja continuar [S/N]: " )
    if continuar  in 'Nn':
        print("Obrigdo volte sempre")
        break
