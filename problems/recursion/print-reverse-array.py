import sys

sys.setrecursionlimit(200000)


def solve(n, arr):
    sys.stdout.write(str(arr[n]) + " ")
    if n == 0:
        return
    solve(n - 1, arr)


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, arr = data[0], data[1:]
    solve(n - 1, arr)


if __name__ == "__main__":
    main()
