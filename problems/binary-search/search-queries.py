import sys

data = list(map(int, sys.stdin.read().split()))

n, x = data[0], data[1]
arr = data[2 : n + 2]
queries = data[n + 2 :]

result = []


def binary_search(q):
    l = 0  # noqa: E741
    r = n - 1
    while l <= r:
        mid = (r + l) // 2

        curr_val = arr[mid]

        if curr_val == q:
            return mid + 1
        elif q > curr_val:
            l = mid + 1  # noqa: E741
        else:
            r = mid - 1

    return -1


for i in queries:
    result.append(str(binary_search(i)))

sys.stdout.write("\n".join(result))
