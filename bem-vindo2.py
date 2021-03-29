from calculoMedia import calculaMedia, calculaMediaMEC
#import calculoMedia
import validasenha

nota1 = int(input("Digite sua nota1: "))
nota2 = int(input("Digite sua nota2: "))
nota3 = int(input("Digite sua nota3: "))
nota4 = int(input("Digite sua nota4: "))

# Esta função caçcula media
mediacalculada = calculaMedia(nota1,nota2,nota3,nota4)
print("A media da Nota é ", mediacalculada)    

calculaMediaMEC(nota1,nota2,nota3,nota4) 