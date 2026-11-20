import sys

sys.setrecursionlimit(100000)


def solve(open, close, n, ans, curr):
    if open == n and close == n:
        ans.append(list(curr))
        return

    if open < n:
        curr.append("(")
        solve(open + 1, close, n, ans, curr)
        curr.pop()

    if close < open:
        curr.append(")")
        solve(open, close + 1, n, ans, curr)
        curr.pop()


def main():
    n = int(sys.stdin.read().strip())

    ans = []
    solve(0, 0, n, ans, [])
    sys.stdout.write(str(len(ans)) + "\n")

    for a in ans:
        sys.stdout.write("".join(a) + "\n")


if __name__ == "__main__":
    main()
