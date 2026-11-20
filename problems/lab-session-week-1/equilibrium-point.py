n = int(input().strip())
arr = [*map(int, input().strip().split())]

# using prefix sum

# p_sum = [0] * (n + 1) 

# eq = -1

# for i in range(1, n + 1):
#     p_sum[i] += arr[i - 1] + p_sum[i - 1]

# for i in range(1, n + 1):
#     lhs = p_sum[i - 1]
#     rhs = p_sum[n] - p_sum[i]
    
#     if lhs == rhs:
#         eq = i - 1
#         break   

# using sum

sum = 0

for i in range(n):
    sum += arr[i]
    
rhs = sum
lhs = 0
eq = -1

for i in range(n):
    rhs -= arr[i]
    
    if lhs == rhs:
        eq = i
        break
    
    lhs += arr[i]
    
print(eq)
