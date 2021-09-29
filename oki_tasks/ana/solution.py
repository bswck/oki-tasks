k_word = input()
l_word = input()
print(('NIE', 'TAK')[all(l_word.count(ch) == k_word.count(ch) for ch in set(l_word))])
