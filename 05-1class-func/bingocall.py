"""
# BEGIN BINGO_DEMO

>>> bingo = BingoCage(range(3))
>>> bingo.pick()
1
>>> bingo()
0
>>> callable(bingo)
True

# END BINGO_DEMO

"""

# BEGIN BINGO

import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)  # <1>
        random.shuffle(self._items)  # <2>

    def pick(self):  # <3>
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')  # <4>

    def __call__(self):  # <5>
        return self.pick()

#任何函数是真正的对象，任何python对象都可以表现得像函数，，只需要实现实例方法__call__
#实现__call__方法的类是创建函数类对象的简便方式
# END BINGO
bingo = BingoCage(range(3))
print(bingo._items)
print(bingo.pick())
print(bingo())
print(callable(bingo))