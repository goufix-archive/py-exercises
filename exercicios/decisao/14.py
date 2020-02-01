# Faça um programa que lê as duas notas parciais obtidas
# por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento   Conceito
#   Entre 9.0 e 10.0          A
#   Entre 7.5 e 9.0           B
#   Entre 6.0 e 7.5           C
#   Entre 4.0 e 6.0           D
#   Entre 4.0 e zero          E

nota1 = float(input('Qual a nota parcial 1? '))
nota2 = float(input('Qual a nota parcial 2? '))

media = (nota1 + nota2) / 2

if (media < 4):
    print('Conceito E')
elif (media > 4 and media < 6):
    print('Conceito D')
elif (media > 6 and media < 7.5):
    print('Conceito C')
elif (media > 7.5 and media < 9):
    print('Conceito B')
elif (media > 9 and media < 10):
    print('Conceito A')
elif (media == 10):
    print('Conceito S')
