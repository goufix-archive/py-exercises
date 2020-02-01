cachoDeUva = 10

while cachoDeUva > 0:
    cachoDeUva = (cachoDeUva - 1)
    print('Ainda restam: %d uvas' % cachoDeUva)

resposta = 'sim'
numero = 0

while resposta == 'sim':
    pergunta = input('você quer digitar um número?')
    if pergunta == 's' or pergunta == 'S':
        numero = numero + 1
    else:
        print('Você digitou %d números' % numero)
        resposta = 'nao'
