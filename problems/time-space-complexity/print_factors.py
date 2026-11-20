n = int(input().strip())
index = 0
output = []

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        output[index:index] = [i, n//i] if i * i != n else [i]
        index += 1
print(' '.join(map(str, output)))