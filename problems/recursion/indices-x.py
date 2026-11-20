import sys

sys.setrecursionlimit(200000)


def solve(i, n, x, arr, ans):
    if i == n:
        return ans if ans else ["-1"]

    if arr[i] == x:
        ans.append(str(i + 1))

    return solve(i + 1, n, x, arr, ans)


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    arr, x = data[1:-1], data[-1]

    sys.stdout.write(" ".join(solve(0, n, x, arr, [])))


if __name__ == "__main__":
    main()
