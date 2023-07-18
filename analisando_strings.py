nome = str(input('Digite o seu nome: '))
idade = input('Qual a sua idade: ')
ultima = len(nome)


if nome:
    print(f'Olá {nome}!')
    if ' ' in nome:
        print('Seu nome possue espaços.')
    else:
        print('Seu nome não possue espaços.')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome possue {len(nome)} letras.')
    print(f'A primeira letra do seu nome é: "{nome[0]}"')
    print(f'A última letra do seu nome é: "{nome[ultima - 1]}"')
else:
    print('Você deixou o campo nome vazio!')
if idade:
    print(f'Você possue {idade} anos!')
else:
    print('Você deixou o campo idade vazio!')
