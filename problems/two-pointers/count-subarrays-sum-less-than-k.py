import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    n, k, arr = data[0], data[1], data[2:]
    sum = 0
    l = 0
    ans = 0

    for r in range(n):
        sum += arr[r]

        while sum >= k and l <= r:
            sum -= arr[l]
            l += 1

        ans += r - l + 1

    sys.stdout.write(str(ans))


if __name__ == "__main__":
    solve()
