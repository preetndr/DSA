import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    n, k, arr = data[0], data[1], data[2:]
    check_map = {}
    count = 0
    for i in range(n):
        num = arr[i] * k
        count += check_map.get(arr[i], 0)
        check_map[num] = check_map.get(num, 0) + 1

    sys.stdout.write(str(count))


if __name__ == "__main__":
    solve()
