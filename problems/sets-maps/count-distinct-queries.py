import sys

data = map(int, sys.stdin.read().split())

q = next(data)

hash_map = set()
result = []

for i in range(q):
    t = next(data)
    if t == 3:
        result.append(len(hash_map))
    else:
        x = next(data)
        if t == 1:
            hash_map.add(x)
        elif t == 2:
            hash_map.discard(x)
        else:
            result.append('YES' if x in hash_map else 'NO')

sys.stdout.write('\n'.join(map(str, result)))