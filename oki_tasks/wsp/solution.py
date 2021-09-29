from itertools import islice

candidates = int(input())
print(*islice(sorted(map(int, input().split()[:candidates]), reverse=True), 10))
