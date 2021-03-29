a = 0

while True:
    print(a)
    a = a + 1
    if a == 5:
       break
print("Fim")

marcas = ["Adidas","Nike","Topper"]
for i in marcas:
    print(i)

    if i == "Nike":
        print("Achei o Nike")
        break

a = int(input("Digite um numero"))

if a == 9:
    print("Aqui 9")
elif a == 8:
    print("Aqui 9")   
elif a == 7:
    print("Aqui 7") 
else :
    print("não tem essa condicinal ")   


a = "Marcos"

contador = 0
for i in a:
    print(i)
    contador += 1
    if i == "a":
        print("Achei o a") 
        break  
print("passei pelo for", contador, "vezes")       