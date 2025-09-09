#Ex 01

# try:
#     with open('exemplo.txt', 'r') as arquivo:
#         for linha in arquivo:
#             print(linha.strip())

# except Exception as e:
#     print('Ocorreu um erro: ', e)

#Ex 02

# soma = 0
# try:
#     with open('exemplo.txt', 'r') as arquivo:
#         for linha in arquivo:
#             soma = int(linha) + soma
        
# except Exception as e:
#     print("Ocorreu um erro: ", e)
# print(soma)

#Ex 03

# while True:
#     print("-----------------------------")
#     print("1 - Inserir um nome")
#     print("2 - Sair")
#     escolha = int(input("Digite sua općão: "))
#     print("-----------------------------")

#     match escolha:
#         case 1:
#             nome = input("Digite o nome que quer adicionar: ")
#             with open('exemplo.txt', 'a') as arquivo:
#                 arquivo.write(f"{nome}\n")
        
#         case 2:
#             break

#Ex 04

# try:
#     with open("alunos.txt", 'r') as arquivo_aluno:
#         for linha in arquivo_aluno:
#             nome, nota = linha.strip().split(',')
#             nota = float(nota)
            
#             if nota < 6:
#                 with open('reprovados.txt', 'a') as arquivo_rec:
#                     arquivo_rec.write(f'{nome}\n');
# except Exception as e:
#     print('Ocorreu um erro: ', e)
        
#Ex 05

# try:
#     copiar = input('Digite o nome do arquivo que quer copiar: ')
#     with open(copiar, 'r') as arquivo_original:
#         for linha in arquivo_original:
#             with open('copia.txt', 'a') as arquivo_copia:
#                 arquivo_copia.write(f'{linha}')

# except FileNotFoundError as file_not_found:
#     print('Arquivo não econtrado - ')

# except PermissionError as permission_denied:
#     print('Permissão para editar/criar arquivo negada')

#Ex 06

# try:
#     while True:
#         print('--------------------------')
#         print('1 - Adicionar produto na lista')
#         print('2 - Ver a lista')
#         print('3 - Sair')
#         print('--------------------------')
#         escolha = int(input('Escolha sua općão: '))

#         match escolha:
#             case 1:
#                 produto = input("Digite o produto novo: ")
#                 with open('compras.txt', 'a') as arquivo:
#                     arquivo.write(f'{produto}\n')
            
#             case 2:
#                 with open('compras.txt', 'r') as arquivo:
#                     for linha in arquivo:
#                         print(linha)

#             case 3:
#                 break

# except FileNotFoundError as file_not_found:
#     print('Arquivo não encontrado!')

# except PermissionError as permission_denied:
#     print('Você não tem permissão para alterar/criar arquivos!')

# except Exception as e:
#     print('Ocorreu um erro: ', e)

#Ex 07

