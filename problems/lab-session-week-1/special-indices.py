n = int(input().strip())

arr = [*map(int, input().strip().split())]

#using prefix sum

odd_p_sum = [0] * (n + 1)
even_p_sum = [0] * (n + 1) 

for i in range(n):
    if i % 2 == 0:
        even_p_sum[i] += even_p_sum[i - 1] + arr[i]
        odd_p_sum[i] = odd_p_sum[i - 1]
    else:
        odd_p_sum[i] += odd_p_sum[i - 1] + arr[i]
        even_p_sum[i] = even_p_sum[i - 1]

count = 0

for i in range(n):
    even_sum = even_p_sum[i - 1] + (odd_p_sum[n - 1] - odd_p_sum[i])
    odd_sum = odd_p_sum[i - 1] +  (even_p_sum[n - 1] - even_p_sum[i])

    if even_sum == odd_sum:
        count += 1

#using sum

# odd_total = 0
# even_total = 0

# for i in range(n):
#     if i % 2 == 0:
#         even_total += arr[i]
#     else:
#         odd_total += arr[i]
        
# l_even = 0
# l_odd = 0

# count = 0

# for i in range(n):
#     if i % 2 == 0:
#         l_even += arr[i]
#     else:
#         l_odd += arr[i]
    
#     even_sum = l_even + (odd_total - l_odd) - (arr[i] * (1 if i % 2 == 0 else 0))
#     odd_sum = l_odd + (even_total - l_even) - (arr[i] * (1 if i % 2 != 0 else 0)) 

#     if even_sum == odd_sum:
#         count += 1
        
print(count)