import sys

sys.setrecursionlimit(100000)


def solve(n, k, ans, curr=None):
    if curr is None:
        curr = []

    if n == 0:
        ans.append(curr.copy())
        return
    if n < 0:
        return

    for i in range(1, k + 1):
        curr.append(str(i))
        solve(n - i, k, ans, curr)
        curr.pop()


def main():
    data = list(map(int, sys.stdin.read().split()))
    ans = []
    solve(data[0], data[1], ans)

    sys.stdout.write("\n".join(" ".join(x) for x in ans))


if __name__ == "__main__":
    main()
