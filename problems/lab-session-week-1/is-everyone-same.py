
n, q= map(int, input().strip().split())

arr = [*map(int, input().strip().split())]

c_arr = [] #lenght is 1 less than arr

for i in range(n - 1):
    if arr[i] == arr[i+1]:
        c_arr += [1]
    else:
        c_arr += [0] 


p_arr = [0] * n
sum = 0

for i, num in enumerate(c_arr, start= 1):
    sum += num
    p_arr[i] += sum

    
def check(l, r):
    
    count = p_arr[r - 1] - p_arr[l - 1]
        
    return 'YES' if count == r - l else 'NO'
        
    
result = []
for _ in range(q):
    l, r = map(int, input().strip().split())
    result += [check(l ,r)]
    
print('\n'.join(result))
    
