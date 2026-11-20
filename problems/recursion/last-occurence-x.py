import sys

sys.setrecursionlimit(200000)


def solve(n, x, arr):
    if n < 0:
        return -1

    if arr[n] == x:
        return n + 1

    return solve(n - 1, x, arr)


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    arr, x = data[1:-1], data[-1]

    sys.stdout.write(str(solve(n - 1, x, arr)))


if __name__ == "__main__":
    main()
