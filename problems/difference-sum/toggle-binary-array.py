n, q = map(int, input().strip().split())

arr = [*map(int, input().strip().split())]

c_arr = [0] * (n + 1)

for _ in range(q):
    l, r = map(int, input().strip().split())
    
    c_arr[l - 1] += 1
    c_arr[r] -= 1
    
for i in range(1, n):
    c_arr[i] += c_arr[i - 1]

flipped_arr = []

for i in range(n):
    if c_arr[i] % 2 != 0:
        flipped_arr.append(1 if arr[i] == 0 else 0)
    else:
        flipped_arr.append(arr[i])    

print(' '.join(map(str, flipped_arr)))
        