'''Faça um programa que peça o tamanho de um arquivo para download (em MB)
 e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
  aproximado de download do arquivo usando este link (em minutos).'''

from datetime import datetime, timedelta

fileSize = float(input("Qual o tamanho do arquivo em MB?"))
linkSpeed = float(input("Qual a velocidade do lixo da sua internet MBps?"))
totalTime = timedelta(seconds=int(fileSize / linkSpeed))
d = datetime(1, 1, 1) + totalTime
print("Vai levar %d minutos e %d segundos para concluir o download" %
      (d.minute, d.second))

'''

def GetTime():
    sec = timedelta(seconds=int(input('Enter the number of seconds: ')))
    d = datetime(1,1,1) + sec

    print("DAYS:HOURS:MIN:SEC")
    print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))
    '''
