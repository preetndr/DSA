import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    q, queries = data[0], data[1:]

    k = 10**6 + 1
    isPrime = [True] * (k)
    isPrime[0], isPrime[1] = (False, False)
    i = 2
    while i * i <= k:
        if isPrime[i]:
            for j in range(i * i, k, i):
                isPrime[j] = False
            # size = (k - 1 - i * i) // i + 1
            # isPrime[i * i : k + 1 : i] = [False] * size
        i += 1

    ans = ["YES" if isPrime[p] else "NO" for p in queries]
    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    solve()
