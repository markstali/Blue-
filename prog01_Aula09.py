#Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.
while True:
    nota = int(input("Digite uma nota de 0 a 10: "))

    if nota < 0 or nota > 10:
        print(f"Por favor digite uma nota valida de 0 a 10, o {nota} é invalido!!")
    else:
        print(f"Obrigado!! ")
        break

