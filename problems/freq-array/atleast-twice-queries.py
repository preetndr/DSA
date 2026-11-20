import sys

data = map(int, sys.stdin.read().split())

it = lambda: next(data)

q = it()
# Using Hash Maps
# map = {}
# count = 0
# result = []

# for i in range(q):
#     query = it()
#     if query == 1:
#         num = it()
#         new_val = map.get(num, 0) + 1
#         map[num] = new_val
#         if new_val == 2:
#             count += 1
        
#     elif query == 2:
#         num = it()
#         prev_val = map.get(num, 0)
#         if prev_val > 0:
#             if prev_val == 2:
#                 count -= 1
#             new_val = prev_val - 1
#             map[num] = new_val
#     else:
#         result.append(str(count))

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
        freq_arr[num] += 1
        if freq_arr[num] == 2:
            count += 1

    elif query == 2:
        num = it()
        if freq_arr[num] > 0:
            if freq_arr[num] == 2:
                count -= 1
            freq_arr[num] -= 1
    else:
        result.append(str(count))

sys.stdout.write('\n'.join(result))
