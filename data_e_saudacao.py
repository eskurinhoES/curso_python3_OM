hora = float(input('Digite a hora usando como separador dos minutos um ponto".": '))
if hora >= 0 and hora <= 11.59:
    print('Bom dia!')
elif hora >= 12.00 and hora <= 17.59:
    print('Boa tarde!')
elif hora >= 18.00 and hora <= 23.59:
    print('Boa noite!')
else:
    print('Digite uma hora válida!')
