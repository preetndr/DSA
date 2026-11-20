import sys

sys.setrecursionlimit(100000)


def solve(i, j, n, m, bombs, ans, curr=None):
    if curr is None:
        curr = []

    if i > n or j > m or bombs[i - 1][j - 1] == 1:
        return

    if i == n and j == m:
        ans.append(list(curr))
        return

    curr.append("R")
    solve(i, j + 1, n, m, bombs, ans, curr)
    curr.pop()

    curr.append("D")
    solve(i + 1, j, n, m, bombs, ans, curr)
    curr.pop()


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    bombs = []
    for i in range(2, 2 + n * m, m):
        bombs.append(data[i : i + m])

    ans = []
    solve(1, 1, data[0], data[1], bombs, ans)

    sys.stdout.write("\n".join("".join(x) for x in ans))


if __name__ == "__main__":
    main()
