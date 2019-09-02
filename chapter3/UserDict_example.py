import collections


# UserDict хранит внутри себя экземпляр dict в атрибуте data (он не наследует dict)
class StrKeyDict(collections.UserDict):
    # Мето get унаследован от mapping и нет смысла его реализовывать
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        else:
            return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


d = StrKeyDict([('2', 'Two'), ('4', 'four')])
print(d['2'])
print(d[2])
print(d['4'])
print(d[4])

print(d.get(2))
print(d.get('2'))
print(d.get(4))
print(d.get('4'))

print(2 in d)
print(4 in d)
print('2' in d)
print('4' in d)
