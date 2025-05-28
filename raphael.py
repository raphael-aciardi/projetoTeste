op_validos = ['+', '-', '*', '/']

while True:
    try:
        e = float(input('Digite o valor à esquerda do operador: '))
        op = input(f'Digite o operador. Opções: {op_validos}: ')
        d = float(input('Digite o valor à direita do operador: '))

        if op in op_validos:
            if op == '/' and d == 0:
                print('Divisão por zero! Tente novamente.')
                continue

            expressao = f'{e} {op} {d}'
            resultado = eval(expressao)
            print(f'{e} {op} {d} = {resultado}')
            break
        else:
            print("Operador incorreto! Tente novamente.")
    except ValueError:
        print("Valores numéricos inválidos! Tente novamente.")
