# Cálculo de meio de cultura Kirk
''' Esse código faz o cálculo para a quantidade necessária de regeagentes no preparo do meio de cultura com base na quantidade de meio desejada em litros.'''

Reagentes= {"Dextrose":"5","Extr.Levedura":"2","KH2PO4":"0.2","MgSO4":"0.05","CaCl2":"0.013","MnSO4":"0.016", "CuSO4":"0.0499" } #Quantidade padrão para 2L de meio

Quant = input("Digite quanto você precisa de meio em L")
print( )
print("--------------")
List = []
indexx = 0
for i in Reagentes:
    List.append(float(Reagentes[i])*float(Quant)); # Cada reagente é adicionado à lista "List" e multiplicado pelo valor necessário,
for i in Reagentes: # Essa repetição apresenta na tela uma mensagem para cada reagente e quanto vai ser necessário para o preparo da quantidade desejada. 
    print("Para o reagente {} é necessário {} gramas".format(i,List[indexx]))
    print("--------------")
    indexx+=1


input()
