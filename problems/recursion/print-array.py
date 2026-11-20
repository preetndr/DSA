import sys

sys.setrecursionlimit(200000)

ans = []


def solve(n, arr):
    if n < 0:
        return
    solve(n - 1, arr)
    ans.append(str(arr[n]))


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, arr = data[0], data[1:]
    solve(n - 1, arr)
    sys.stdout.write(" ".join(ans))


if __name__ == "__main__":
    main()
