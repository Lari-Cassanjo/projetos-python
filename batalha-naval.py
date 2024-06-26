import random
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

navio1 = random.randint(1,25)
navio2 = random.randint(1,25)
if navio2 == navio1:
    navio2 -= 1
navio3 = random.randint(1,25)
if navio3 == navio1 or navio3 == navio2:
    navio3 += 1

print(navio1, navio2, navio3)
