def matriz_identidade(l, c):
    matriz = []

    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(0)
            if i == j:
                linha[i] = 1
        matriz.append(linha)
    return matriz

matriz1 = matriz_identidade(3, 3);
print(matriz1)

#--------------------

def matriz_contra_identidade(l, c):
    matriz = []

    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(0)

        linha[j - i] = 1
        matriz.append(linha)

    return matriz

matriz2 = matriz_contra_identidade(3, 3)
print(matriz2)