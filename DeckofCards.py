import itertools

vals = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

deck = list(itertools.product(vals, suits))

for suit, val in deck:
    print('The %s of %s' % (suit, val))
