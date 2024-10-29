import random

points = {
    'player': 0,
    'comp': 0
}


def is_odd(number: int):
    if number % 2 == 0:
        return False
    else:
        return True


while True:
    a = random.randint(10, 110)
    if is_odd(a):
        continue
    b = random.randint(10, 120)
    if is_odd(b):
        continue
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
        points['comp'] += 2
        print('Повезёт в следующий раз')
    print(f'Счёт {points['player']}:{points['comp']}')

