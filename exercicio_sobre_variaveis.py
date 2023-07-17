nome = str(input('Digite o seu nome: '))
sobrenome = str(input('Digite o seu sobrenome: '))
idade = int(input('Qual a sua idade? '))
ano_nascimento = int(input('Em que ano você nasceu? '))
e_maior_de_idade = idade >= 18
altura = float(input('Digite a sua altura em metros: '))


print(f'Olá {nome}.Seja bem vindo!')
print(f'Seu sobrenome é: {sobrenome}.')
print(f'Você tem {idade} anos.')
print(f'Você nasceu no ano de {ano_nascimento}.')
if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')
print(f'Sua altura em metros é de : {altura}')
