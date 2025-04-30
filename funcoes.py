def saudacao(nome):
    '''
    Essa função serve para cumprimentar um aluno nóia!
    '''
    return f'Olá {nome}, seu nóia!'

mensagem = saudacao("Felipe")
print(mensagem)

def media_tres_notas(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

resultado = media_tres_notas(10, 9, 8)

print(resultado)

def somar(a, b):
    return a + b

args = [3, 5]
resultado = somar(*args) #Use * para desempacotar a lista
print(resultado)

kwargs = {'a': 3, 'b': 5}
resultado = somar(**kwargs)
print(resultado)

def somar(a = 2, b = 3):
    return a + b

resultado = somar()
print(resultado)

def alterar_a(a):
    a = a + 1
    print(a)

a = 2
alterar_a(a)

print(a);

def alterar_lista(lista):
    lista.append(2)
    lista.append(5)

    print(lista)

lista = [1, 7, 8, 3]
alterar_lista(lista[:])

print(lista)

def soma_total(*numeros):
    '''
    Esta função aceita um núnero arbitrário de argumentos e retorna a soma de todos.
    '''

    return sum(numero)

print(soma_total(1,2,3))
print(soma_total(10,20,30, 40))
print(soma_total())

def exibir_informacoes(**informacoes):
    '''
    Esta funcao aceita um numero arbitrário de argumentos nomeados  e os exibr
    '''

    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

exibir_informacoes(nome = "Ana", idade = 25, cidade = "São Paulo")
exibir_informacoes(produto = "Notebook", preco = 2500, marca = "Dell")