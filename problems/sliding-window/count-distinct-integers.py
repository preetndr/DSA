import sys

data = list(map(int, sys.stdin.read().split()))
n, k, arr = data[0], data[1], data[2:]

result = []
count_map = {}

for i in range(k):
    e = arr[i]
    count_map[e] = count_map.get(e, 0) + 1

result.append(len(count_map))

for i in range(k, n):
    add_e = arr[i]
    remove_e = arr[i - k]

    count_map[add_e] = count_map.get(add_e, 0) + 1
    count_map[remove_e] -= 1

    if count_map[remove_e] == 0:
        count_map.pop(remove_e, None)

    result.append(len(count_map))

sys.stdout.write(" ".join(map(str, result)))
