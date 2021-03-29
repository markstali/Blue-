#Faça um programa que leia um nome de usuário e a sua senha e
# não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    usuario = input("Informe o usuario: ")
    senha = input("Informe sua senha: ")

    if senha == usuario:
        print(f"ERROR, Sua SENHA deve ser diferente do seu nome de USUARIO!")
    else:
        print(f"Bem vindo,{usuario}!")
        break

