nome = input('Digite o seu nome: ')
altura = float(input(f'Qual a sua altura {nome}? '))
peso = float(input(f'Qual o seu peso {nome}? '))
imc = peso / altura**2
print(f'Você tem um IMC de {imc:.2f} {nome}!')
