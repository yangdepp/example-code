import collections
from random import choice

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
  ranks = [str(n) for n in range(2,11)] + list('JQKA')   #['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  suits = 'spades diamonds clubs hearts'.split()    #['spades', 'diamonds', 'clubs', 'hearts']

  def __init__(self):
    self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

  def __len__(self):
    return len(self._cards)
  
  def __getitem__(self,position):
    return self._cards[position]

deck = FrenchDeck()
print(deck._cards)
print('#'*50)
print(deck[0])
print(len(deck))
print(choice(deck))
print('#'*50)

#排序，用点数来判定扑克牌的大小，2最小、A最大；同时要加上对花色的判定。黑桃最大、红桃次之、方块再次，梅花最小。
#梅花2大小是0，黑桃A是51
suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)  #通过关键字参数创建dict  {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}

def spades_high(card):
  rank_value = FrenchDeck.ranks.index(card.rank)
  return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
  print(card)


  #本节心得及知识点
  #collections.namedtuple创建一个tuple，可用属性访问
  #list可以用相加拼起来 ['1,','2'] + ['a','b'] = ['1,','2','a','b']
  #设计类的时候，可以把__len__和__getitem__的具体实现代理给self._cards
  #类实例用索引访问单个元素以及和迭代切片的实现都依赖__getitem__
  #random.choice随机选取list中的元素
  #用空格分割字符串's s x x'.split() =>['s','s','x','x']
  #列表生成器[Card(rank,suit) for rank in self.ranks for suit in self.suits]
  #def __getitem__(self,position):这个内置函数的实现，可以实现deck[0]选择，0就是position
  #关键字创建dict:dict(x=1,y=2) =>{'x':1,'y':2}
  #list.index(item)实现已知元素，求元素对应的索引
  #sorted函数接收一个key函数，根据函数返回值进行排序
  #sorted(dect, key=spades_high)，将deck中的元素，传入函数spades_high,根据返回值映射位置排序
  #sorted()函数按照传入的key函数返回值进行返回值的排序，每一个返回值又对应相应的元素，按照对应关系返回排序后的dect