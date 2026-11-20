import sys

sys.setrecursionlimit(200000)


def solve(n, arr):
    if n == 0:
        return True

    return arr[n] >= arr[n - 1] and solve(n - 1, arr)


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, arr = data[0], data[1:]

    sys.stdout.write("YES" if solve(n - 1, arr) else "NO")


if __name__ == "__main__":
    main()
