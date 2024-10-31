import random

points = {
    'player': 0,
    'comp': 0
}

words = ['валенок', 'горчица', 'овсянка', 'дом', 'капуста', 'снег', 'гидроэлектростанция', 'кот', 'ток', 'ёлка', 'носок',
         'сон', 'камень', 'рюкзак', 'суперпупермега', 'гречка', 'речка', 'уста', 'ген', 'термобельё', 'термос', 'конь']


while True:
    a = random.choice(words)
    b = random.choice(words)
    ans = str(a) + str(b)
    user = input(f'{a} + {b} = ')
    if user == str(ans):
        points['player'] += 2
        print('Верно')
    else:
        points['comp'] += 2
        print('Повезёт в следующий раз')
    print(f'Счёт {points['player']}:{points['comp']}')

