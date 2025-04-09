#Primeiro exercicio
# number = int(input("digite um número: "))
#
# if number > 0:
#     print("Seu número é positivo")
#
# elif number < 0:
#     print("Seu número é negativo")
#
# else:
#     print("Seu número é 0")

#Segundo exercício
# firstGrade = float(input("Digite a primeira nota do aluno: "))
# secondGrade = float(input("Digite o segundo nota do aluno: "))
# thirdGrade = float(input("Digite a terceira nota do aluno: "))
#
# average = (firstGrade + secondGrade + thirdGrade) / 3
#
# if average >= 7:
#     print("Aprovado")
#
# else:
#     print("Reprovado")

#terceiro exercício
# age = int(input("Digite sua idade: "))
#
# if age >= 18:
#     print("Maior de idade")
#
# else:
#     print("Menor de idade")

#Quarto exercício
# numbers = (1, 2, 3)
#
# if numbers[0] > numbers[1] and numbers[0] > numbers[2]:
#     print(numbers[0], "é o maior número")
#
# elif numbers[1] > numbers[0] and numbers[1] > numbers[2]:
#     print(numbers[1], "é o maior número")
#
# else:
#     print(numbers[2], "é o maior número")

#Quinto exercício

# number = int(input("Digite um número"))
#
# if number > 10 and number < 50:
#     print("Número está dentro do intervalo")
#
# elif number == 10:
#     print("O número é 10")
#
# elif number == 50:
#     print("O número é 50")
#
# else:
#     print("O número não está no intervalo")

#Sexto exercício

# stringList = ["Thomas", "Nibo", "Champao"]
#
# size1 = len(stringList[0])
# size2 = len(stringList[1])
# size3 = len(stringList[2])
#
# if size1 > size2 and size1 > size3:
#     print(stringList[0], "é o maior nome")
#
# elif size2 > size1 and size2 > size3:
#     print(stringList[1], "é o maior nome")
#
# else:
#     print(stringList[2], "é o maior nome")

#Sétimo exercício

# dayWeek = int(input("Digite um número de 1 a 7"))
#
# match dayWeek:
#     case 1:
#         print("Segunda")
#     case 2:
#         print("Terça")
#     case 3:
#         print("Quarta")
#     case 4:
#         print("Quinta")
#     case 5:
#         print("Sexta")
#     case 6:
#         print("Sábado")
#     case 7:
#         print("Doming")

#Oitavo exercício

# tupla = (1, 1, 1)
#
# if tupla[0] != tupla[1] and tupla[1] != tupla[2]:
#     print("Todos diferentes")
#
# elif tupla[0] == tupla[1] and tupla[1] == tupla[2]:
#     print("Todos iguais")
#
# elif tupla[0] == tupla[1] or tupla[0] == tupla[2] or tupla[1] == tupla[2]:
#     print("Dois valores são iguais")

#nono exercício

# list = [2, 2]
#
# if list[0] % list[1] == 0:
#     print("Os dois números são divisíveis")
#
# else:
#     print("Os dois números não são divisiveis")

#Décimo exercício

# month = input("Digite o mês que você quer")
#
# match month.lower():
#     case "janeiro":
#         print("31 dias")
#     case "fevereiro":
#         print("28 dias")
#     case "março":
#         print("31 dias")
#     case "abril":
#         print("30 dias")

#Décimo primeiro exercício

# triangle = [2, 2, 1]
#
# if triangle[0] + triangle[1] > triangle[2] and triangle[1] + triangle[2] > triangle[0] and triangle[2] + triangle[0] > triangle[1]:
#     print("Os valores são válidos")
#
# else:
#     print("Os valores não são válido")

#Décimo segundo exercício
#
# even = int(input("Digite um número para descobrir se é par ou impar: "))
#
# if even % 2 == 0:
#     print("O número é par")
#
# else:
#     print("O número é impar")

#Décimo terceiro exercício

# choosenFruit = input("Digite uma fruta para verificar se está no estoque: ")
# fruits = ["Banana", "Maça"]
#
# if choosenFruit.lower() == fruits[0]:
#     print(fruits[0], "está no estoque")
#
# elif choosenFruit.lower() == fruits[1]:
#     print(fruits[1], "está no estoque")
#
# else:
#     print(choosenFruit, "não tem no estoque")

#Décimo quarto exercício

# numbers = [1, 2]
#
# if numbers[0] > numbers[1]:
#     print(numbers[0], "é o maior número")
#
# elif numbers[1] > numbers[0]:
#     print(numbers[1], "é o maior número")
#
# elif numbers[0] == numbers[1]:
#     print("Os dois números são iguais")

#Décimo quinto exercício

# civilState = input("Digite seu estado civil")
#
# match civilState.lower():
#     case "solteiro":
#         print(1)
#     case "casado":
#         print(2)
#     case "divorciado":
#         print(3)
#     case _:
#         print(0)

#Décimo sexto exercício

# number = int(input("Digite um número: "))
#
# tupla = (1, 3, 5, 7, 9)
#
# if number == tupla[0] or number == tupla[1] or number == tupla[2] or number == tupla[3] or number == tupla[4]:
#     print("Número válido")
#
# else:
#     print("Número inválido")

#Décimo sétimo exercício
#
# season = input("Coloque um número de 1 a 12"):
#
# match season:
#     case 1:
#         print("Verão")
#     case 2:
#         print("Verão")
#     case 3:
#         print("Outono")
#     case 4:
#         print("Outono")
#     case 5:
#         print("Outono")
#     case 6:
#         print("Inverno")
#     case 7:
#         print("Inverno")
#     case 8:
#         print("Inverno")
#     case 9:
#         print(" Primavera")
#     case 10:
#         print(" Primavera")
#     case 11:
#         print(" Primavera")
#     case 12:
#         print("Verão")

#Décimo nono exercício
#
# tupla = ("Thomas", 18)
#
# if tupla[1] >= 18:
#     print("Pode dirigir")
#
# else:
#     print("Não pode dirigir")

#Vigésimo exercício

color = ["vermelho", "azul", "amarelo"]

if color[0] == "vermelho" and color[1] == "azul" and color[2] == "amarelo":
    print("São cores primárias")

else:
    print("Não são cores primárias")