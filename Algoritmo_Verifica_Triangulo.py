#Função para verificar se os valores formam um triângulo
def eh_triangulo(L1, L2, L3):
    return (L1 + L2 >= L3) and (L1 + L3 >= L2) and (L2 + L3 >= L1) and (L1 != 0) and (L2 != 0) and (L3 != 0)

# Linha divisória para melhorar a legibilidade da saída
divisoria_linha = "\n------------------------------------------------------------\n"

# Quantidade de triângulos para verificar
numero_de_triangulos = int(input("Quantos triângulos você deseja verificar? "))
print(divisoria_linha)

# Loop para verificar cada triângulo
for i in range(1, numero_de_triangulos + 1):
    lado1 = float(input(f"Digite o valor do primeiro lado do triângulo {i}: "))
    lado2 = float(input(f"Digite o valor do segundo lado do triângulo {i}: "))
    lado3 = float(input(f"Digite o valor do terceiro lado do triângulo {i}: "))

    #Verifica se os valores formam um triângulo
    if eh_triangulo(lado1, lado2, lado3):
        tipo = tipo_triangulo(lado1, lado2, lado3)
        print(f"\n\nTriângulo {i}: É um triângulo do tipo {tipo}\n")
        print(divisoria_linha)
    else:
        print(f"\n\nTriângulo {i}: Não é um triângulo!\n")
        print(divisoria_linha)