# -*- coding:utf-8 -*-
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


print('Testing...')

beer_card = Card('7', 'diamonds')

Card('Q', 'hearts') in deck

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print('beyond_ascii:', beyond_ascii)
beyond_ascii_ = list(filter(lambda c : c > 127, map(ord, symbols)))
print('beyond_ascii_:', beyond_ascii_)

print('test end...')