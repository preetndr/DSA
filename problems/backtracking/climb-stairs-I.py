import sys

sys.setrecursionlimit(200000)


def solve(n, ans, curr=None):
    if curr is None:
        curr = []

    if n == 0:
        ans.append(curr.copy())
        return
    if n < 0:
        return

    curr.append("1")
    solve(n - 1, ans, curr)
    curr.pop()

    curr.append("2")
    solve(n - 2, ans, curr)
    curr.pop()


def main():
    ans = []
    solve(int(sys.stdin.read().strip()), ans)

    sys.stdout.write("\n".join(" ".join(x) for x in ans))


if __name__ == "__main__":
    main()
