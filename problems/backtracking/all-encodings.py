import sys

sys.setrecursionlimit(100000)


def solve(a, n, st, ans, curr):
    if n == len(st):
        ans.append(list(curr))
        return

    curr.append(chr(a + int(st[n]) - 1))
    solve(a, n + 1, st, ans, curr)
    curr.pop()

    if n < len(st) - 1 and int(st[n : n + 2]) <= 26:
        curr.append(chr(a + int(st[n : n + 2]) - 1))
        solve(a, n + 2, st, ans, curr)
        curr.pop()


def main():
    st = sys.stdin.read().strip()
    ans = []
    solve(ord("a"), 0, st, ans, [])
    sys.stdout.write(str(len(ans)) + "\n")

    for a in ans:
        sys.stdout.write("".join(a) + "\n")


if __name__ == "__main__":
    main()
