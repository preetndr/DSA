n = int(input().strip())

arr = [*map(int, input().strip().split())]

p_sum = [0] * (n + 1)

for i in range(n):
    p_sum[i] += p_sum[i - 1] + arr[i]
    
result = []    

for i in range(n):
    l = i
    sub_result = []
    for j in range(n):
        r = j
        sub_result.append(p_sum[r] - p_sum[l - 1] - p_sum[i - 1])
        l += 1
    result.append(sub_result)

print(result)
print('\n'.join(' '.join(map(str, row)) for row in result))