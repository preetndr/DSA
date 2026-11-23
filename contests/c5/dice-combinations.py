import sys

sys.setrecursionlimit(200000)


def solve(s, n, ans, curr):
    if s > n:
        return
    if s == n:
        ans.append(list(curr))
        return

    for i in range(1, 7):
        curr.append(str(i))
        solve(s + i, n, ans, curr)
        curr.pop()


def main():
    n = int(sys.stdin.read().strip())
    ans = []
    solve(0, n, ans, [])
    sys.stdout.write("\n".join(" ".join(x) for x in ans) + "\n")


if __name__ == "__main__":
    main()
