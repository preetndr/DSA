n = int(input().strip())
arr = [*map(int, input().strip().split())]

# using sum

# sum = 0
# eq = 'NO'

# for i in range(n):
#     sum += arr[i]

# lhs = 0    
# rhs = sum


# for i in range(n - 1):
#     lhs += arr[i]
#     rhs -= arr[i]
    
#     if lhs == rhs:
#         eq = 'YES'

# using prefix sum

p_sum = [0] * n
sum = 0
eq = 'NO'

for i in range(n):
    sum += arr[i]
    p_sum[i] = sum
    
for i in range(n - 1):
    lhs = p_sum[i]
    rhs = p_sum[n - 1] - p_sum[i]

    if lhs == rhs:
        eq = 'YES'
        break    

print(eq)