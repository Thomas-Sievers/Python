import random
import math

'''
#primero exercício
numbers = list(range(0,11))

for i in numbers:
    print(i)

#Segundo exercício
numbers1 = list(range(0,51))

for i in numbers1:
    if i%2 == 0:
        print(i)

#terceiro exercício
userChoise = input("Escolha um número para somar: ")

numbers2 = list(range(0, int(userChoise) + 1))
total = 0

for i in numbers2:
    total += i
    print(total)

#quarto exercício
userChoiseMultiplication = input("Escolha um número para ver a tabuada: ")
result = 0

for i in numbers:
    result = int(userChoiseMultiplication) * i
    print(result)

#Quinto exercício
contagem = 10

while contagem > 0:
    print(contagem)
    contagem -= 1

#sexto exercício
soma = []
contador = list(range(0,5))

for i in contador:
    soma.append(int((input("Digite um número para somar: "))))

total = sum(soma)
print(total)

#sétimo exercício
palavra = input("Digite uma palavra: ")
contadorVogal = 0;

for i in palavra:
    if i in "aeiou":
        contadorVogal += 1
        print(contadorVogal)


#Oitavo exercício
numero = int(input("Digite um número pra verificar se é primo: "))
contador = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1

if contador == 2:
    print("Número primo")
else:
    print("Número não primo")


#Décimo exercício
termoUsuario = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1

for i in range(1, termoUsuario + 1):
    fatorial *= i
print(fatorial)

#Décimo primeiro exercício
aleatorio = math.floor(random.uniform(0, 10))
i = 0

while i < 3:
    escolha = int(input("Tente adivinhar o número de 1 a 10: "))

    if(escolha == aleatorio):
        print("Você acertou!")
        break
    else:
        print("Tente de novo!")
        i += 1

#Décimo segundo exercício

palavra = input("Digite uma palavra para inver ela: ")
invertida = ""

for i in palavra:
    invertida = i + invertida
print(invertida)

#Décima terceiro exercício
numeros = int(input("Digite o tamanho da sua piramide: "))

for i in range(1, numeros + 1):
    i *= "*"
    print(i)
'''

#Décimo quarto exercício
contador = 0
i = 0
conta = 0

while contador < 3:
    if(i % conta == 0):
        