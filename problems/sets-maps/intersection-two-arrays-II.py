import sys

# from collections import Counter

data = map(int, sys.stdin.read().split())
it = lambda: next(data)

def get_freq_dict(iterable):
    d = {}
    for i in iterable:
        d[i] = d.get(i, 0) + 1
    return d

n = it()
A = get_freq_dict(it() for _ in range(n))
# A = Counter(it() for _ in range(n))

m = it()
B = get_freq_dict(it() for _ in range(m))
# B = Counter(it() for _ in range(m))

pair = sorted([A, B], key= len)

result = []

for i in sorted(pair[0]):
    if i in pair[1]:
        result.extend([i] * min(pair[0][i], pair[1][i]))


sys.stdout.write(str(len(result)) + '\n'+ ' '.join(map(str, result)))
