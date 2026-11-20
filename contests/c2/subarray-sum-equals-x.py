import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))

    n, x = data[0], data[1]

    arr = data[2:]
    sum_set = {0}
    total = 0

    result = "NO"
    for i in range(0, n):
        total += arr[i]

        if total - x in sum_set:
            result = "YES"
            break

        sum_set.add(total)

    sys.stdout.write(result)


if __name__ == "__main__":
    solve()
