import random


escolhas = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(1, 3)

print('suas opções')

print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')

opp = int(input('digite a sua escolha: '))
print('JO\nKEN\nPO!!!')
print('-='*10)
print(f'o jogador jogou {opp}')
print(f'o computador jogou {computador}')
print('-='*10)
if computador == escolhas:
    print('empate')
if computador == 2 and opp == 1:
    print('computador ganhou')
if computador == 3 and opp == 2:
    print('computador ganhou')
if computador == 1 and opp == 3:
    print('computador ganhou')
if opp == 2 and computador == 1:
    print('o player ganhou')
if opp == 3 and computador == 2:
    print('player ganhou')
if opp == 1 and computador == 3:
    print('player ganhou')
