from collections import namedtuple

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

print('#'*50)
#
#                    |   lat.    |   long.
#    Mexico City     |   19.4333 |  -99.1333
#    New York-Newark |   40.8086 |  -74.0204
#    Sao Paulo       |  -23.5478 |  -46.6358
# #

# 定义和使用具名元组
City = namedtuple('City', 'name country population coordinates')
tokyo = City('tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
print('#'*50)

#具名元组的属性和方法
#_fields属性是一个包含这个类所有字段名称的元组
print(City._fields)   #('name', 'country', 'population', 'coordinates')

#用_make()通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟City(*delhi_data)是一样的
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
print(delhi_data)
delhi = City._make(delhi_data)
print(delhi)
print(delhi._asdict())    
#_asdict()把具名元组以collections.OrderedDict的形式返回。
#OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population', 21.935), ('coordinates', LatLong(lat=28.613889, long=77.208889))])

for key, value in delhi._asdict().items():
    print(key + ':', value)






######
#####
#知识点总结：
'''
    1、元组拆包
    2、具名元组
'''