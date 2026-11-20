n, q = map(int, input().strip().split())

arr = [*map(int, input().strip().split())]
diff_arr = [0] * (n + 2)

for _ in range(q):
    a, b, k = map(int, input().strip().split())
    
    diff_arr[a] += k
    diff_arr[b + 1] -= k

for i in range(1, n + 1):
    diff_arr[i] += diff_arr[i - 1]

print(max(j + k for j, k in zip(arr, diff_arr[1:n+1])))
        
    

    