import array
from collections import namedtuple

# Генераторы
symbols = 'Pavel Kozlov'
res = tuple(ord(symbol) for symbol in symbols)
print(res)

arr = array.array('I', (ord(symbol) for symbol in symbols))

# Распаковка кортежей
name, lastname = ('Pavel', 'Kozlov')
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# Трактация каждого элемента как отдельного поля
for passport in traveler_ids:
    print('%s %s' % passport)
# Распаковка с помощью фиктивной переменной
for country, _ in sorted(traveler_ids):
    print(country)

# 20 / 2 = 2 цел и 4 в остатке
print(divmod(20, 8))
t = (20, 8)
# Звездочка перед аргументом распаковывает кортеж
print(divmod(*t))

# Выборка лишних элементов
a, b, *c = range(10)
print(a, b, c)

# Распаковка вложенных кортежей
areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.953, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
]
for city, cc, pop, (lat, long) in areas:
    print(f'lat:{lat} & long:{long}')

# Именованный кортеж
City = namedtuple('City', 'name country population coordinates')
tokio = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokio)
print(tokio[0])
print(tokio.coordinates)

print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.953, LatLong(28.613889, 77.208889))
# позволяет экземпляр именнованного кортежа из интерпретируемого объекта. как City(*delhi_data)
delhi = City._make(delhi_data)

# превращает объект в collections.OrderedDict. Можно использовать для вывода
delhi = delhi._asdict()
for key, value in delhi.items():
    print(f'{key} : {value}')
