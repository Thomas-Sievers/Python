zeros = []

quantidade = int(input("Digite quando zeros você quer inserir: "))

for n in range(quantidade):
    zeros.append(0)

print(zeros)

#-----------------------------

numeros = [[0,1,2],
           [3,4,5],
           [6,7,8]]



for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        print(numeros[i][j])

#-------------========

matrix = []

colunas = int(input("Digite a quantidade de colunas: "))
linhas = int(input("Digite a quantidade de linhas: "))

for i in range(linhas):
    matrix.append([])
    for j in range(colunas):
        matrix[i].append(0)

for i in matrix:
    print(i)

#--------------

def criar_matriz_zeros(l, c):
    #inicia a matrix
    matriz = []

    #loop para criar linhas
    for i in range(l):
        linha = [] #Cria uma nova linha vazia
        # Loop para adicionar n zeros na linha
        for j in range(c):
            linha.append(0)
        #Adiciona a linha criada à matriz
        matriz.append(linha)

    return matriz

matriz = criar_matriz_zeros(9, 9)
print(matriz)