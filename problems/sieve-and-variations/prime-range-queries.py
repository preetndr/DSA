import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    n, q = data[0], data[1]
    queries = data[2:]

    isPrime = [1] * (n + 1)
    isPrime[0], isPrime[1] = [0, 0]
    i = 2
    while i * i <= n:
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = 0
        i += 1

    for i in range(1, n + 1):
        isPrime[i] += isPrime[i - 1]

    ans = []
    for s in range(0, q * 2, 2):
        l = queries[s]
        r = queries[s + 1]

        ans.append(str(isPrime[r] - isPrime[l - 1]))

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    solve()
