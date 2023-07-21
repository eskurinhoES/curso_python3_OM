while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite o operador(+, -, / ou *): ')
    num_1_float = 0
    num_2_float = 0
    numeros_validos = None

    try:
        num_1_float = float(num1)
        num_2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue


    print('Realizando sua conta.Confira o resultado abaixo:')
    soma = num_1_float + num_2_float
    subtracao = num_1_float - num_2_float
    divisao = num_1_float / num_2_float
    multiplicacao = num_1_float * num_2_float

    if operador == '+':
        print(f'A soma entre {num_1_float} e {num_2_float} é: {soma:.3f}')
    elif operador == '-':
        print(f'A diferença entre {num_1_float} e {num_2_float} é: {subtracao:.3f}')
    elif operador == '/':
        print(f'A divisão entre {num_1_float} e {num_2_float} é: {divisao:.3f}')
    elif operador == '*':
        print(f'A multiplicação entre {num_1_float} e {num_2_float} é: {multiplicacao}')
    
    

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
