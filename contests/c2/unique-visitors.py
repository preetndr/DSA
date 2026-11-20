import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]

    arr = data[1:]
    hash_set = set()
    result = []
    for n in arr:
        hash_set.add(n)
        result.append(str(len(hash_set)))

    sys.stdout.write(" ".join(result))


if __name__ == "__main__":
    solve()
