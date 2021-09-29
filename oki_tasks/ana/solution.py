word = input()
comp = input()
print(('NIE', 'TAK')[all(word.count(ch) == comp.count(ch) for ch in set(comp))])
