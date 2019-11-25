# Criado para meu ambiente de trabalho para fazer um sorteio.
#Sorteando grupo de pessoas aleatoriamente com Python !
import random
from time import sleep
matriz=[[0,0,0,0], [0,0,0,0], [0,0,0,0],[0,0,0,0]]
for l in range(0,4):
    for c in range (0,4):
                matriz[l][c]=str(input('Digite o Nome:'))
print(matriz)
print('Processando...')
sleep(2)#para dar tempo antes do programa responder
random.shuffle(matriz)
print (matriz)
