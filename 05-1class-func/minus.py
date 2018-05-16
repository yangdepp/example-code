class C:
  pass

obj = C()
def func():
  pass

print(dir(func))
print('-'*100)
print(dir(obj))
print('-'*100)
print(sorted(set(dir(func)) - set(dir(obj))))
#['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
###
# '__annotations__'类型是dict，参数和返回值的注解
# 
# 
# 
# ###