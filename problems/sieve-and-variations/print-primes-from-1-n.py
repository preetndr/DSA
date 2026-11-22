import sys


def solve():
    n = int(sys.stdin.read().strip())

    isPrime = [True] * (n + 1)
    isPrime[0], isPrime[1] = (False, False)
    i = 2
    while i * i <= n:
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
        i += 1

    ans = [str(p) for p in range(n + 1) if isPrime[p]]
    sys.stdout.write(" ".join(ans) + f"\n{str(len(ans))}")


if __name__ == "__main__":
    solve()
