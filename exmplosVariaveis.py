nome = "Marcos"

# A. Variável Booleana.
booleano = True

# B. Variável List , Set e Dict
dicionario = {
    "nome": "Talita",
    "idade": 25,
    "sexo": "Feminino"
}
_set = {1, 2, 'Marcos'}
lista = ["A", "B", "C", "D", "E"]

# C. Variável Tupla
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(dicionario, _set, lista, tupla, booleano)

print("Exemplo de dic: \n", dicionario, type(dicionario))

print("Exemplo de set: \n", _set, type(_set))

print("Exemplo de lista: \n ", lista, type(lista))

print("Exemplo de tupla: \n", tupla, type(tupla))

print("Exemplo de booleano: \n", booleano, type(booleano))

print("Exemplo de string: \n", nome, type(nome))

# D. Imprima dados de uma posição da List e Tupla
for i in range(0, 3):
    print(f"Parte da Lista{i}: {lista[i]}")
    print(f"Parte da Tupla{i}: {tupla[i]}")

# E. Tenha uma condição IF com AND e OR
if booleano:
    print(f"Booleano era True agora é: {not booleano}")
if len(dicionario) == 3 and len(_set) == 3:
    print("Dicionario e Set tem o mesmo tamanho de indices")

# F. Que imprima a primeira Posicão de uma String.
print(f"A primeira posição da string {nome} é '{nome[0]}'")
