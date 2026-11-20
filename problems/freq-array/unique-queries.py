import sys

data = iter(sys.stdin.read().split())
it = lambda: next(data)

q = int(it())

# Using Hash Maps

map = {}
result = []

for i in range(q):
    query = it()
    
    if query == '+':
        num = int(it())
        map[num] = map.get(num, 0) + 1
        
    elif query == '-':
        num = int(it())
        if map.get(num, 0) > 0:
            map[num] -= 1
            if map.get(num) == 0:
                map.pop(num)
    else:
        result.append(str(len(map)))

sys.stdout.write('\n'.join(result))


# Using Freq Array

# K = int(1e5) + 1

# freq_arr = [0] * K
# count = 0
# result = []

# for i in range(q):
#     query = it()
    
#     if query == '+':
#         num = int(it())
#         if freq_arr[num] == 0:
#             count += 1
#         freq_arr[num] += 1

#     elif query == '-':
#         num = int(it())
#         if freq_arr[num] > 0:
#             freq_arr[num] -= 1
#             if freq_arr[num] == 0:
#                 count -= 1
#     else:
#         result.append(str(count))

# sys.stdout.write('\n'.join(result))
