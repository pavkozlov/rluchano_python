from types import MappingProxyType
# Любые изменения исходното отображения будут видны в MappingProxyType, но через него сделать изменения нельзя
d = {1: 'a'}
mpt = MappingProxyType(d)

print(mpt)
print(mpt[1])

# TypeError
# mpt[1] = 3

d[3] = 3
print(mpt)
print(mpt[3])
