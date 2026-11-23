import sys

sys.setrecursionlimit(200000)


def solve(i, j, n, m, arr, ans, curr):

    if i > n or j > m or arr[i - 1][j - 1]:
        return

    if i == n and j == m:
        ans.append(list(curr))
        return

    # move right
    curr.append("R")
    solve(i, j + 1, n, m, arr, ans, curr)
    curr.pop()

    # move down
    curr.append("D")
    solve(i + 1, j, n, m, arr, ans, curr)
    curr.pop()


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    arr = [data[i : i + m] for i in range(2, 2 + n * m, m)]
    ans = []
    solve(1, 1, n, m, arr, ans, [])

    sys.stdout.write("\n".join("".join(x) for x in ans) + "\n")


if __name__ == "__main__":
    main()
