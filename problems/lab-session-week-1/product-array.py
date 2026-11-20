n = int(input().strip())

arr = [*map(int, input().strip().split())]

product = 1
zeros = 0

for i in range(n):
    if arr[i] == 0:
        zeros += 1
    else:
        product = product * arr[i]

prod = []

for i in range(n):
    
    if zeros > 1:
        prod = [0] * n
        break
    elif zeros == 1:
        prod.append(product if arr[i] == 0 else 0)
    else:
        prod.append(product//arr[i])
    
print(' '.join(map(str, prod)))
    
