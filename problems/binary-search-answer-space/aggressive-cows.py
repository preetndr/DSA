import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    n, k = data[0], data[1]

    arr = sorted(data[2:])
    ret = None

    d = arr[0]
    for i in range(1, n):
        curr_distance = arr[i] - arr[i - 1]
        if curr_distance < d:
            d = curr_distance

    left = 0  # d
    right = arr[n - 1] - arr[0]
    while left <= right:
        min_distance = (left + right) // 2

        previous_stall = arr[0]
        cows_placed = 1
        for stall in arr[1:]:
            if stall - previous_stall >= min_distance:
                cows_placed += 1
                previous_stall = stall

        if cows_placed < k:
            right = min_distance - 1
        else:
            ret = min_distance
            left = min_distance + 1

    sys.stdout.write(str(ret))


if __name__ == "__main__":
    solve()
