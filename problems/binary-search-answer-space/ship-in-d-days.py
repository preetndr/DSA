import sys

data = list(map(int, sys.stdin.read().split()))

n, d = data[0], data[1]

arr = data[2:]


def search(arr, n, d):
    left = max(arr)
    right = sum(arr)
    ret = None

    while left <= right:
        capacity = (left + right) // 2
        total_weight = 0
        day_counter = 1

        for i in range(n):
            load = arr[i]
            if total_weight + load <= capacity:
                total_weight += load
            else:
                day_counter += 1
                total_weight = load

        if day_counter > d:
            left = capacity + 1
        elif day_counter <= d:
            ret = capacity
            right = capacity - 1

    return ret


sys.stdout.write((str(search(arr, n, d))))
