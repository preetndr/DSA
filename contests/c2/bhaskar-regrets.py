import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    apologies = []
    for i in range(1, n * 3 + 1, 3):
        apologies.append([data[i], data[i + 1], data[i + 2]])

    apologies.sort(key=lambda x: (x[2], -x[0], x[1]))

    sys.stdout.write("\n".join(" ".join(map(str, x)) for x in apologies))


if __name__ == "__main__":
    solve()
