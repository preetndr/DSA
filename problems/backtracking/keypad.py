import sys

sys.setrecursionlimit(100000)


def solve(key_map, n, ans, curr):
    if not n:
        ans.append(list(curr))
        return

    for c in key_map[int(n[0])]:
        curr.append(c)
        solve(key_map, n[1:], ans, curr)
        curr.pop()


def main():
    n = sys.stdin.read().strip()
    key_map = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }
    ans = []
    solve(key_map, n, ans, [])
    sys.stdout.write(str(len(ans)) + "\n")

    for a in ans:
        sys.stdout.write("".join(a) + "\n")


if __name__ == "__main__":
    main()
