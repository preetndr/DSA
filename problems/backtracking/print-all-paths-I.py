import sys

sys.setrecursionlimit(100000)


def solve(i, j, n, m, ans, curr=None):
    if curr is None:
        curr = []

    if i == n and j == m:
        ans.append(list(curr))
        return

    if i > n or j > m:
        return

    curr.append("R")
    solve(i, j + 1, n, m, ans, curr)
    curr.pop()

    curr.append("D")
    solve(i + 1, j, n, m, ans, curr)
    curr.pop()


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    ans = []
    solve(1, 1, data[0], data[1], ans)

    sys.stdout.write("\n".join("".join(x) for x in ans))


if __name__ == "__main__":
    main()
