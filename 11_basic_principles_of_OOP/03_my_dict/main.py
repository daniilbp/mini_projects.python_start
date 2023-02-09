class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


dct_1 = {'a': 1, 'b': 2, 'c': 3}
dct_2 = {'d': 4}

dct_1 = MyDict(dct_1)

print(dct_1.get('a'), '\n')
print(dct_1.get('d'), '\n')
print(dct_1.keys(), '\n')
print(dct_1.values(), '\n')

dct_1.update(dct_2)
print(dct_1)

dct_1.pop('d')
print(dct_1)
