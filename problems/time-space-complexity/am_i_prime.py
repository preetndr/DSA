n = int(input().strip())
print('YES' if sum(1 + (i * i != n) if n % i == 0 else 0 for i in range(1, int(n ** 0.5) + 1)) == 2 else 'NO')