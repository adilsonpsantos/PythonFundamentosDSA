# calculadora Python

print('###############  Calculadora em Python  ###################')

def soma(a, b):
    return a + b

def subtracao (a, b):
    return a - b

def multiplicacao (a, b):
    return a * b

def divisao (a, b):
    if b != 0:
        return a/b
    else:
        print('O segundo valor não pode ser nulo!')

op = 0

while op not in range(1, 5):
    print('Escolha a operação:')
    print('1 para Soma')
    print('2 para Subtração')
    print('3 para Multiplicação')
    print('4 para Divisão')

    op = int(input('Operação: '))

    if op not in range(1, 5):
        print('Escolha uma operação válida!')

a = int(input('Digite o primeiro valor: '))
b = 0
while b == 0:
    b = int(input('Digite o segundo valor: '))
    if b == 0 and op == 4:
        print('A divisão por ZERO não é permitida!')
        continue
    elif op == 1:
        res = soma(a, b)
    elif op == 2:
        res = subtracao(a, b)
    elif op == 3:
        res = multiplicacao(a, b)
    else:
        res = divisao(a, b)

    print('Resultado: ' + str(res))




