def fatorial(n):
    if n < 2:
        return 1

    return n * fatorial(n - 1)


print(fatorial(5))

def multiplicacao(n, m):
    if n == 0 or m == 0:
        return 0
    if m == 1:
        return n

    return n + multiplicacao(n, m - 1)

print(multiplicacao(2, 5))

def regressiva(m):
    print(m)
    if m == 0:
        return 0
    return regressiva(m - 1)

regressiva(10)

def contar_vogais(string):
    if len(string) == 0:
        return 0
    if string[0] in 'aeiou':
        return 1 + contar_vogais(string[1:])

    return 0 + contar_vogais(string[1:])

print(contar_vogais('batata'))