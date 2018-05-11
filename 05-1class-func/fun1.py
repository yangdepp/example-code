def factorial(n):
    '''return n!'''
    if(n < 2):
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(42))
print(factorial.__doc__)
print(type(factorial))
print('-' * 50)
# 函数作为参数传递
# 首先认识一下range()函数，生成一个可迭代的序列对象，而不是列表。
fact = factorial
print(fact(5))
map(factorial, range(11))
print(map(factorial, range(11)))  # map函数将range(11)中可迭代的每一个item作用于factorial函数，
# 并返回一个Iterator，惰性序列，用list()函数让它把整个序列都计算出来并返回一个list
print('=' * 50)
# 迭代  Iteration    可以用collections模块的Iterable
# 这种可直接作用于for循环的对象统称为可迭代对象  Iterable
# 列表生成式
# 生成器   generator   把列表生成式的[]换成()，就创建了一个generator
# 迭代器    生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值。
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

# 创建押韵单词，可以把单词反过来然后排序


def reverse(word):
    return word[::-1]


fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=reverse))
print('/' * 50)

# 计算阶乘列表map和filter与列表推到比较


def fact1(n):
    if(n < 2):
        return 1
    else:
        return n * fact1(n - 1)


print(list(map(fact1, range(6))))
print([fact1(n) for n in range(6)])
print(list(map(fact1, filter(lambda n: n % 2, range(6)))))  # filter函数会进行过滤
print([fact1(n) for n in range(6) if n % 2])

# 在python3中，map和filter返回生成器（一种迭代器）

# reduce和sum函数，py2.3之后，最好使用内置sum函数，在可读和性能方面
from functools import reduce


def add(m, n):
    return m + n

print(reduce(add, range(100)))
print(sum(range(100)))
