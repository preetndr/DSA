import sys


def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


data = list(map(int, sys.stdin.read().split()))
n, k, arr = data[0], data[1], data[2:]

prime_arr = [check_prime(i) for i in arr]
max_count = 0
l = 0
r = k - 1
max_count = sum(prime_arr[l : r + 1])
prime_count = max_count

for i in range(k, n):
    if max_count == k:
        break

    if prime_arr[i - k]:
        prime_count -= 1

    if prime_arr[i]:
        prime_count += 1

    if prime_count > max_count:
        max_count = prime_count
        l = i - k + 1
        r = i

sys.stdout.write(" ".join(map(str, arr[l : r + 1])))
