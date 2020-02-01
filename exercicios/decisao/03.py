# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

user_input = input('Digite um sexo [M/F]... ').lower()

if (user_input == 'm'):
    print('Masculino')
elif (user_input == 'f'):
    print('Feminino')
else:
    print('Sexo inválido!')
