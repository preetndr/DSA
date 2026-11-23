import sys

sys.setrecursionlimit(200000)


def solve(n, arr, ans):
    if n < 0:
        return

    ans.append(str(arr[n]))
    solve(n - 1, arr, ans)

    if n == 0:
        return
    ans.append(str(arr[n]))


def main():
    data = list(map(int, sys.stdin.read().split()))

    n, arr = data[0], data[1:]
    ans = []
    solve(n - 1, arr, ans)

    sys.stdout.write(" ".join(ans))


if __name__ == "__main__":
    main()
