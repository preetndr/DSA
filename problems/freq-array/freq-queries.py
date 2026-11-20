import sys

data = map(int, sys.stdin.read().split())

it = lambda: next(data)

q = it()
# Using Hash Maps
# map = {}
# result = []

# for i in range(q):
#     query = it()
#     if query == 1:
#         num = it()
#         map[num] = map.get(num, 0) + 1
        
#     elif query == 2:
#         num = it()
#         if map.get(num, 0) > 0:
#             map[num] -= 1
#             if map.get(num) == 0:
#                 map.pop(num)
#     else:
#         a, b = it(), it()
#         result.append('YES' if map.get(a, 0) == map.get(b, 0) else 'NO')

# sys.stdout.write('\n'.join(result))


# Using Freq Array

K = int(1e5) + 1

freq_arr = [0] * K
count = 0
result = []

for i in range(q):
    query = it()
    
    if query == 1:
        num = it()
        if freq_arr[num] == 0:
            count += 1
        freq_arr[num] += 1

    elif query == 2:
        num = it()
        if freq_arr[num] > 0:
            freq_arr[num] -= 1
            if freq_arr[num] == 0:
                count -= 1
    else:
        a, b = it(), it()
        result.append('YES' if freq_arr[a] == freq_arr[b] else 'NO')

sys.stdout.write('\n'.join(result))
