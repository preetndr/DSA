import sys

data = map(int, sys.stdin.read().split())

q = next(data)

hash_map = {}
result = []

for i in range(q):
    t = next(data)
    if t == 3:
        result.append(len(hash_map))
    else:
        x = next(data)
        if t == 1:
            hash_map[x] = hash_map.get(x, 0) + 1
        elif t == 2:
            current_val = hash_map.get(x, 0)
            if (current_val > 1):
                hash_map[x] = current_val - 1
            else:
                hash_map.pop(x, None)
        else:
            result.append('YES' if x in hash_map else 'NO')

sys.stdout.write('\n'.join(map(str, result)))