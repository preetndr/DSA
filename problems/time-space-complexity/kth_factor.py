def kth_factor(input):
    n, k = input
    factors = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n//i:
                factors.append(n//i)
    factors.sort()
    if k <= len(factors):
        return factors[k - 1]
    else:
        return -1
    
print(kth_factor(map(int, input().strip().split())))