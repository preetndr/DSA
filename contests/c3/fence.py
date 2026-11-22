import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    n, k, arr = data[0], data[1], data[2:]

    total = sum(arr[0:k])
    min_total = total
    l = 0
    ans = l + 1
    for r in range(k, n):
        total = total - arr[l] + arr[r]
        l += 1

        if total < min_total:
            min_total = total
            ans = l + 1

    sys.stdout.write(str(ans))


if __name__ == "__main__":
    solve()
