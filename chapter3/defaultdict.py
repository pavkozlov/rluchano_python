import re
import collections

res = 'Эдвард Хоппер (англ. Edward Hopper; 22 июля 1882, Найак, штат Нью-Йорк — 15 мая 1967, Нью-Йорк) — американский \
    живописец и гравёр, представитель американской жанровой живописи. Наиболее известен своими картинами повседневной \
    жизни, из которых самой известной стали «Полуночники» (1942). Творчество Хоппера оказало сильное влияние на мир \
    искусства в целом и поп-культуру XX века в частности. '

WORD_RE = re.compile('\w+')

# Если заданного ключа нет, создаётся default_factory.(в данном случае это конструктор list)
# Если default_factory не задан, будет исключение KeyError
# Это справедливо для dicr[key]. В случае dict.get(key), default_factory не сработает
index = collections.defaultdict(list)

for match in WORD_RE.finditer(res):
    word = match.group()
    index[word].append((match.start() + 1, match.start() + 1 + len(word),))

for word in sorted(index, key=str.upper):
    print(word, index[word])
