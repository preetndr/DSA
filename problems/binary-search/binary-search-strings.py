import sys

data = list(sys.stdin.read().split())

n = int(data[0])
arr = data[1 : n + 1]
x = data[n + 1]


def binary_search(q):
    l = 0  # noqa: E741
    r = n - 1
    while l <= r:
        mid = (r + l) // 2

        curr_val = arr[mid]

        if curr_val == q:
            return "YES"
        elif q > curr_val:
            l = mid + 1  # noqa: E741
        else:
            r = mid - 1

    return "NO"


sys.stdout.write(binary_search(x))
