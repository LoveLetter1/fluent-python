import array
import os

symbols = '$¢£¥€¤'

codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)
# 使用列表推导式 listcomps
codes = [ord(symbol) for symbol in symbols]
print(codes)
# := 赋值的变量在推导式或生成器表达式返回后依然可以访问
x = 'ABC'
codes = [ord(y) for y in x]
print(x)
print(codes)

codes = [last := ord(c) for c in x]
print(last)
print(x)
# 列表推导式涵盖 map 和 filter 两个函数的功能，写出的代码不像 Python的 lambda 表达式那样晦涩难懂
beyond_ascii = [ord(x) for x in symbols if ord(x) > 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)
# 列表推导式计算笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirt = [(color, size) for color in colors for size in sizes]
print(tshirt)
# 生成器表达式
print(tuple(ord(symbol) for symbol in symbols))
print(array.array('I', (ord(symbol) for symbol in symbols)))
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)
# 把元组当记录来使用
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country, _ in traveler_ids:
    print(country)
a, b = lax_coordinates
a, b = b, a
print(a, b)
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
_, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')
print(filename)


def unpack(a, b, c, *d):
    return a, b, c, d
print(*(2,3,*(2,4)))