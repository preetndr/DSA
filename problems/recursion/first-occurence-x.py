import sys

sys.setrecursionlimit(200000)


def solve(i, n, x, arr):
    if i == n:
        return -1

    if arr[i] == x:
        return i + 1

    return solve(i + 1, n, x, arr)


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    arr, x = data[1:-1], data[-1]

    sys.stdout.write(str(solve(0, n, x, arr)))


if __name__ == "__main__":
    main()
