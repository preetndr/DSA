n, q = map(int, input().strip().split())

arr = [*map(int, input().strip().split())]

c_arr = []

for i in range(n - 1):
    if arr[i] == arr[i + 1]:
        c_arr += [1]
    else:
        c_arr += [0]
        
p_arr = [0]
sum = 0

for i in c_arr:
    sum += i
    p_arr += [sum]

def check(l, r):
    return p_arr[r - 1] - p_arr[l - 1] 

result = []

for _ in range(q):
    l, r = map(int, input().strip().split())
    
    result += [check(l, r)]
    
print('\n'.join(map(str, result)))