#Exceção
# numero = 10
# list = [1]
#
# try:
#     print(numero/0)
#     print(list[2])
#
# except ZeroDivisionError as e:
#     print("Excessão Lançada: ", e)
#
# except Exception as e:
#     print('Deu erro: ', e)
#
# finally:
#     print('Encerrando')

#----------------------------------------------------------------------

#Manipulação de arquivos

#Exemplo 1
# with open('exemplo.txt', 'w') as arquivo: #Se trocar o 'w' para 'a', vira append
#     arquivo.write('Olá, este é um exemplo de escrita em arquivos\n')
#     arquivo.write('Python é poderoso e versátil\n')
#     arquivo.write('Olá, este é um exemplo de escrita em arquivos\n')

#----------------------------------------------------------------------

#Exemplo 2
# import os
#
# directory_name = "my_new_directory"
# os.mkdir(directory_name)
#
# with open('exemplo.py', 'w') as arquivo:
#     print('Arquivo criado')

#----------------------------------------------------------------------

#Exemplo 3

# with open('exemplo.txt', 'r') as arquivo:
#     for linha in arquivo:
#         print(linha.strip())

#----------------------------------------------------------------------

#Exemplo 4
#
# import os
#
# caminho_arquivo = 'exemplo.txt'
#
# #Verifica se o arquivo existe
# if os.path.exists(caminho_arquivo):
#     os.remove(caminho_arquivo)
#     print(f"O arquivo {caminho_arquivo} foi excluido")
# else:
#     print(f'O arquivo {caminho_arquivo} não existe')

#-----------------------------------------------------------------------

#Exemplo 5

import logging

logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Isso é uma mensagem de depuração')
logging.info('Isso é uma mensagem informativa')
logging.warning('Isso é um alerta')
logging.error("Ocorreu um erro!")
logging.warning("Erro crítico!")

try:
    print(10/0)
    logging.info("Operação realizada")
except Exception as e:
    loggin.error(f'Ocorreu um erro ineseperado: {e}')
