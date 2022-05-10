def calcula_bin(etapa, matriz):
    colunas_preenchidas = []
    linhas_preenchidas = []
    rel_bin = []
    nova_matriz = matriz

    for valor_linha in range(len(matriz[etapa])):
        if matriz[etapa][valor_linha] == 1:
            linhas_preenchidas.append(valor_linha)
    
    for valor_coluna in range(len(matriz)):
        if matriz[valor_coluna][etapa] == 1:
            colunas_preenchidas.append(valor_coluna) 
        
    for coluna in colunas_preenchidas:
        for linha in linhas_preenchidas:
            rel_bin.append([linha, coluna])

    for value in rel_bin:
        nova_matriz[value[0]][value[1]] = 1

    return nova_matriz


print("Quantas linhas tem a sua matriz?")
linhas = int(input())

print("Quantas colunas tem a sua matriz?")
colunas = int(input())

matriz = []
for i in range(colunas):
    linha = []
    for j in range(linhas):
        print(f"Qual o valor da posição ({i + 1}, {j + 1})?")
        linha.append(int(input()))
    matriz.append(linha)

for i in range(colunas):
    matriz = calcula_bin(etapa=i, matriz=matriz)

for row in matriz:
    for value in row:
        print(value, end=" ")
    print("")