import collections

wild_cards = ['X','+','B','R']
numbers_cards = [*range(10)].__mul__(2)
color_deck = numbers_cards.__iadd__(wild_cards.__mul__(2))
colors = 'red blue pink yellow'.split()

uno = collections.namedtuple('Card',['rank','color'])

uno_deck = [ uno(rank,color) for color in colors for rank in color_deck]
print(uno_deck)

a = [1,4,9,16,25,36,42,64,81,100]

def is_even(b):
    return b%2==0

even_numbers = [b for b in a if is_even(b)]
print(even_numbers)