#------------------------------------------------------------------------------------------------------ Contador de Células --------------------------------------------------------------
print(" ")
print("---------- Calculadora de células viáveis ---------")
print(" ")
n_cells = int(input("Digite quantas células foram contadas"));
diluição = int(input("Digite o valor da diluição"));
Fator_multipl = 10**4;
N_quadrante = int(input("Digite quantos quadrantes foram contados"));
Celulas_mortas = int(input("Digite quantas células mortas foram contadas"))

print(" ")
print("--------------------RESULTADOS-----------------------")
print(" ")

Total_de_células =  ((n_cells * diluição * Fator_multipl)/N_quadrante);
print(">>> Existem", Total_de_células, "células no meio" );

Celulas_vivas=(((n_cells-Celulas_mortas) * diluição * Fator_multipl)/N_quadrante);
print(">>> Existem", Celulas_vivas, "vivas no meio" );

Celulas_viáveis = Celulas_vivas/Total_de_células
print(">>> Existem", Celulas_viáveis, " células viáveis no meio")



input()
