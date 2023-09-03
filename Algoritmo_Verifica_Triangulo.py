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