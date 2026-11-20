import sys


# Implement only this function.
# Return "Perfect", "Abundant" or "Deficient": compare the sum of the
# proper divisors of n (all its positive divisors except n itself) with n.
def classify(n):
    sum = 1
    
    if n == 1:
        return 'Deficient'
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i + ((n // i) if n // i != i else 0)

    if sum > n:
        return 'Abundant'
    elif sum < n:
        return 'Deficient'
    else:
        return 'Perfect'

data = sys.stdin.buffer.read().split()
T = int(data[0])



print("\n".join(classify(int(x)) for x in data[1:1 + T]))