import numpy

# Создать массив
a = numpy.arange(12)

print(a)
print(type(a))
print(a.shape)

# Изменить форму массива, добавив ещё 1 измерение
a.shape = 3, 4
print(a)

# Получить строку и индексом 2
print(a[2])

# Получить элемент с индексами 2,1
print(a[2, 1])

# Получить столбец с индексом 1
print(a[:, 1])

# Создать новый массив, транспортировав старый (поменять местами строки и столбцы)
print(a.transpose())

# Умножить ВСЕ элементы на 6
a *= 6
print(a)

# Сохранить/Загрузить данные
numpy.save('integers', a)
a2 = numpy.load('integers.npy', 'r+')

# Умножить каждый элемент массива на 0,5
print(a2 * .5)
