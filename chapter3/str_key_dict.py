class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    # метод get делигирует свою работу методу __getitem__, благодаря self[key] запускается __missing__
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'Two'), ('4', 'four')])
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
