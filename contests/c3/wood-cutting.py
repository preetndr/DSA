import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    n, k, arr = data[0], data[1], data[2:]

    left = 1
    right = max(arr)
    ans = 0
    while left <= right:
        mid = (left + right) // 2

        pieces = sum(i // mid for i in arr)

        if pieces >= k:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    sys.stdout.write(str(ans))


if __name__ == "__main__":
    solve()
