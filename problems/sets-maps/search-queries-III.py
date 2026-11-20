import sys

data = map(int, sys.stdin.read().split())

it = lambda: next(data)

n, q = it(), it()

hash_map = {}

for i in range(n):
    hash_map[it()] = i + 1

result = []

for _ in range(q):
    query = it()
    if query in hash_map:
        result.append(hash_map.get(query))
    else:
        result.append(-1)
        
sys.stdout.write('\n'.join(map(str, result)))