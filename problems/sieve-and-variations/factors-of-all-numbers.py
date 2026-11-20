import sys


def solve():
    n = int(sys.stdin.buffer.read().strip())
    ans = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            ans[j].append(i)

    sys.stdout.write("\n".join(" ".join(map(str, x)) for x in ans[1:]))


if __name__ == "__main__":
    solve()
