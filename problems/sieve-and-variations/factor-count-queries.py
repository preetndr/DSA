import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))

    q_count = data[0]
    queries = data[1:]

    k = max(queries)
    lis = [0] * (k + 1)

    ans = []

    for i in range(1, k + 1):
        for j in range(i, k + 1, i):
            lis[j] += 1

    for q in queries:
        ans.append(str(lis[q]))

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    solve()
