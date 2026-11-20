import sys

data = map(int, sys.stdin.read().split())

n, x = next(data), next(data)

first_index = {}
result = []

for i in range(1, n + 1):
    num = next(data)
    if (x - num) in first_index:
        result += [first_index[x - num], i]
        break
    if num not in first_index:
        first_index[num] = i

sys.stdout.write(' '.join(map(str, result)) if result else '-1')