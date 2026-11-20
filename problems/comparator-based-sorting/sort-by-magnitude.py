import sys

data = map(int, sys.stdin.read().split())

n = next(data)

sys.stdout.write(' '.join(map(str, sorted(data, key= lambda x: (abs(x), x)))))
