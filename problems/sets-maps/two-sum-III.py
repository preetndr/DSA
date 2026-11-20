import sys

data = map(int, sys.stdin.read().split())

n, x = next(data), next(data)

first_index = {}
result = 0

for num in data:
    if (x - num) in first_index:
        result += first_index[x - num]
    first_index[num] = first_index.get(num, 0) + 1

sys.stdout.write(str(result))