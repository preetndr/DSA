import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    q, queries = data[0], data[1:]

    k = 10**6 + 1

    h_map = [0] * k
    i = 1
    while i <= k:
        for j in range(i, k, i):
            h_map[j] += 1
        i += 1

    ans = ["YES" if h_map[h_map[q]] == 2 else "NO" for q in queries]
    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    solve()
