numero1 = float(input('Digite o primeiro valor: '))
numero2 = float(input('Digite o segundo valor: '))
if numero1 > numero2:
    print(f'O primeiro valor {numero1} é maior que o segundo {numero2}.')
elif numero1 == numero2:
    print(f'Os dois valores são iguais {numero1} = {numero2}.')
else:
    print(f'O segundo valor {numero2} é maior que o primeiro {numero1}.')
