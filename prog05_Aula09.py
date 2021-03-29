'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

while True:
    pop_A = int(input("PopA: "))
    pop_B= int(input("PopB: "))
    cres1 = float(input("Taxa de Crescinento PopA: "))
    cres2 = float(input("Taxa de Crescimento PopB: "))
    
    if pop_A == pop_B:
        print("Por favor os valores das populações devem ser diferentes.")
    
    elif pop_A > pop_B:
       anos = 0
       
       while pop_A > pop_B:
           anos+=1
           pop_A = pop_A + (pop_A * cres1 )
           pop_B = pop_B + (pop_B * cres2 )
    
       if pop_A < pop_B:        
          print (f"A População 'B'[{pop_B}] levou {anos} anos, para ultrapassar a População 'A'{pop_A}!")
       print("A taxa de crescimento da POPULAÇÃO MENOR deve ser a MAIOR!")
       continuar = input("Deseja continuar?[S/N] ")  
       if continuar in 'Nn':
            break

    else:
       anos = 0
       
       while pop_A < pop_B:
           anos+=1
           pop_A = pop_A + (pop_A * cres1 )
           pop_B = pop_B + (pop_B * cres2 )
    
       if pop_A > pop_B:        
          print (f"A População 'A'[{pop_A}] levou {anos} anos, para ultrapassar a População 'B'{pop_B}!")
       print("A taxa de crescimento da POPULAÇÃO MENOR deve ser a MAIOR!")
       continuar = input("Deseja continuar?[S/N] ")  
       if continuar in 'Nn':
            break
            
     
     
           
       
        

