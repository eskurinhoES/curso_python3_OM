nome = str(input('Digite seu primeiro nome: '))
if len(nome) <= 4:
    print('Seu nome é curto!')
elif len(nome) >= 5 and len(nome) <=6:
    print('Seu nome é normal!')
else:
    print('Seu nome é grande!')