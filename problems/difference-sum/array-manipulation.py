n, q = map(int, input().strip().split())

arr = [0] * (n + 2)

for _ in range(q):
    a, b, k = map(int, input().strip().split())
    
    arr[a] += k
    arr[b + 1] -= k

for i in range(1, n + 1):
    arr[i] += arr[i - 1]

print(max(arr))
        
    

    
