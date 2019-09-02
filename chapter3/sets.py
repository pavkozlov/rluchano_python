# Множество - набор уникальных объектов
l1 = ['spam', 'eggs', 'spam', 'spam']
print(set(l1))
print(list(set(l1)))

# Элементы множества должны быть хешируемые (не изменяемые). Сам тип является изменяемым, но frozenset хешируемый,
# поэтому может быть элементом множества
needles = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
haystack = {2, 3, 4, 5, 88, 77, 99, 110}

# Пересечение. (элементы есть в обоих множествах)
print(len(needles & haystack))

# Эквивалент:
found = 0
for i in needles:
    if i in haystack:
        found += 1
print(found)

# Эквивалент
print(len(needles.intersection(haystack)))

# Проверка вхождения в множествах быстрая, благодаря хеш-таблицам

# Для создания пустого множества используется конструктор set() ({} создаст пустой словарь). Когда множество не
# пустое, лучше использовать {x,y,z} (быстрее, чем set([x,y,z])

f = frozenset(range(10))
print(f)

# set_comprehension
s = {i * 25 for i in range(10)}
print(s)
print(type(s))

# Объединение
print(needles | haystack)

# Разность
print(needles - haystack)

# Дополнение пересечения (симметрическая разность
print(needles ^ haystack)

# Пересечение
print(needles & haystack)

# Не пересекаются (вернет булево значение)
print(needles.isdisjoint(haystack))

# a является элементом b
print(needles in haystack)

needles.add(120)
b = needles.copy()
needles.clear()
# удалить элемент если он присутствует
b.discard(120)
# Удалить элмент. Если его нет, будет исключение KeyError
b.remove(2)

print(needles)
print(b)

