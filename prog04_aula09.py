'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''
pop_A = 80000
pop_B = 200000
cres1 = 0.03
cres2 = 0.015

anos = 0

while pop_B >= pop_A:
    anos+=1
    pop_A = pop_A + (pop_A * cres1 )
    pop_B = pop_B + (pop_B * cres2 )

print ("A População 'A' levou ",anos,"anos, para ultrapassar a População 'B'!")

    
    



