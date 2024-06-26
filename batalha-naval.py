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
game_over = False

print(navio1,navio2,navio3)

print('Tente afundar os três navios com números de 1 a 25! Você tem 10 vidas.')
jogadas = 0
chutes = []

while achou_navio1 == False or achou_navio2 == False or achou_navio3 == False:
    tentativa = int(input('Onde estão os navios? '))
    
    if tentativa in chutes:
        print('Tente um número diferente!')
        jogadas -= 1
    elif tentativa == navio1:
        print('Você acertou o Navio 1!')
        jogadas -= 1
        print(f'Você ganhou uma vida! Agora tem {10 - (jogadas + 1)}')
        achou_navio1 = True
    elif tentativa == navio2:
        print('Você acertou o Navio 2!')
        jogadas -= 1
        print(f'Você ganhou uma vida! Agora tem {10 - (jogadas + 1)}')
        achou_navio2 = True
    elif tentativa == navio3:
        print('Você acertou o Navio 3!')
        jogadas -= 1
        print(f'Você ganhou uma vida! Agora tem {10 - (jogadas + 1)}')
        achou_navio3 = True
    else:
        print('Não tem navios aqui! Tente novamente.')
        print(f'Você perdeu uma vida! Agora tem {10 - (jogadas + 1)}')
    
    chutes.append(tentativa)  
    
    jogadas += 1
    if jogadas == 10:
        game_over = True
        break

if game_over == True:
    print('Você não encontrou todos os navios.')
    print('-'*60)
    print('{:^60}'.format('\33[31mGAME OVER\33[m'))
    print('-'*60)
else: 
    print('Todos os navios foram afundados! Parabéns!')