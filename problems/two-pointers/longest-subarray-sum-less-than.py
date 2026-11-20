import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))

    n, k = data[0], data[1]
    arr = data[2:]
    ans = 0
    l = 0
    sum = 0

    for r in range(n):
        sum += arr[r]

        while sum >= k and l <= r:
            sum -= arr[l]
            l += 1

        ans = max(ans, r - l + 1)

    sys.stdout.write(str(ans))


if __name__ == "__main__":
    solve()
