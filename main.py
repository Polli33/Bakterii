import random

points = {
    'player': 0,
    'comp': 0
}

while True:
    a = random.randint(8, 90)
    b = random.randint(8, 90)
    op = random.choice(('+', '-'))
    if op == '+':
        ans = a + b
        user = input(f'{a} + {b} = ')
    else:
        ans = a - b
        user = input(f'{a} - {b} = ')
    if user == str(ans):
        points['player'] += 2
        print('Верно')
    else:
        points['computer'] += 1
        print('Повезёт в следующий раз')
    print(f'Счёт {points['player']}:{points['computer']}')

