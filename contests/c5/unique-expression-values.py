import sys

sys.setrecursionlimit(200000)


def solve(i, cal, arr, ans):
    if i == len(arr):
        ans.add(cal)
        return

    solve(i + 1, cal + arr[i], arr, ans)

    solve(i + 1, cal - arr[i], arr, ans)


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, arr = data[0], data[1:]
    ans = set()
    solve(1, arr[0], arr, ans)
    sys.stdout.write(str(len(ans)))


if __name__ == "__main__":
    main()
