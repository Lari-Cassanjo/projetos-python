from random import randint
import os
os.system('cls')


print('~'*60)
print('{:^60}'.format('BATALHA NAVAL'))
print('~'*60)

# print('|-----'*5 + '|')
# print('|     '*5 + '|')
# print('|-----'*5 + '|')
# print('|     '*5 + '|')
# print('|-----'*5 + '|')
# print('|     '*5 + '|')
# print('|-----'*5 + '|')
# print('|     '*5 + '|')
# print('|-----'*5 + '|')
# print('|     '*5 + '|')
# print('|-----'*5 + '|')

navio1 = randint(1,25)
navio2 = randint(1,25)
if navio2 == navio1:
    navio2 -= 1
navio3 = randint(1,25)
if navio3 == navio1 or navio3 == navio2:
    navio3 += 1

achou_navio1 = False
achou_navio2 = False
achou_navio3 = False

print(navio1,navio2,navio3)

print('Tente afundar os três navios com números de 1 a 25! Você tem 10 tentativas.')
jogadas = 0

while achou_navio1 == False or achou_navio2 == False or achou_navio3 == False:
    tentativa = int(input('Onde estão os navios? '))
    if tentativa == navio1:
        print('Você acertou o Navio 1!')
        achou_navio1 = True
    elif tentativa == navio2:
        print('Você acertou o Navio 2!')
        achou_navio2 = True
    elif tentativa == navio3:
        print('Você acertou o Navio 3!')
        achou_navio3 = True
    else:
        print('Não tem navios aqui! Tente novamente.')
    
    jogadas += 1
    if jogadas == 10:
        game_over = True
        break

if game_over == True:
    print('Você não encontrou todos os navios.')
    print('-'*60)
    print('{:^60}'.format('GAME OVER'))
    print('-'*60)
else: 
    print('Todos os navios foram afundados! Parabéns!')